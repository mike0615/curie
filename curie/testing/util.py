# Copyright (c) 2015 Nutanix Inc. All rights reserved.
#
#
# Curie unit test utilities.
#
import json
import logging
import os
import time

import mock

from curie import curie_server_state_pb2
from curie.acropolis_cluster import AcropolisCluster
from curie.cluster import Cluster
from curie.curie_server_state_pb2 import CurieSettings
from curie.generic_vsphere_cluster import GenericVsphereCluster
from curie.hyperv_cluster import HyperVCluster
from curie.node import Node
from curie.nutanix_hyperv_cluster import NutanixHypervCluster
from curie.nutanix_vsphere_cluster import NutanixVsphereCluster
from curie.oob_management_util import OobInterfaceType
from curie.proto_util import proto_patch_encryption_support

log = logging.getLogger(__name__)

proto_patch_encryption_support(CurieSettings)


def run_step(test, phase, step_num):
  steps = test.steps()
  for step in steps:
    proto = step.data
    if proto.phase == phase and proto.step_num == step_num:
      log.info(proto.step_description)
      step.func()
      break


def return_until(before_value, after_value, duration_secs):
  """Get a function to return a value for a while, and then something else.

  Args:
    before_value: Value to return before the time expires.
    after_value: Value to return after the time expires.
    duration_secs (int): Number of seconds from now that the inner function
      will return False.

  Returns: Function.
  """
  end_epoch_secs = time.time() + duration_secs

  def inner_func():
    if time.time() < end_epoch_secs:
      return before_value
    else:
      return after_value
  return inner_func


def mock_cluster(node_count=4, spec=Cluster):
  cluster = mock.Mock(spec=spec)
  cluster_metadata = CurieSettings.Cluster()
  cluster_metadata.cluster_name = "MockCluster"
  nodes = [mock.Mock(spec=Node) for _ in xrange(node_count)]
  for index, node in enumerate(nodes):
    node.node_id.return_value = "169.254.0.%d" % index
    node.node_index.return_value = index
    node.node_ip.return_value = node.node_id()
    curr_node = cluster_metadata.cluster_nodes.add()
    curr_node.id = node.node_id()
    curr_node.node_out_of_band_management_info.interface_type = OobInterfaceType.kIpmi
    curr_node.node_out_of_band_management_info.ip_address = "127.0.0.%d" % index
    curr_node.node_out_of_band_management_info.username = "fake_user"
    curr_node.node_out_of_band_management_info.password = "fake_password"
    node.metadata.return_value = curr_node
  cluster.nodes.return_value = nodes
  cluster.node_count.return_value = len(nodes)
  cluster.metadata.return_value = cluster_metadata
  return cluster


def cluster_from_json(filepath):
  """
  Construct a Cluster from a metis-flavored JSON file.

  Args:
    filepath (str): Path to the JSON file.

  Returns:
    Cluster
  """
  if not os.path.exists(filepath):
    raise ValueError("Cluster configuration file not found '%s'" % filepath)
  log.debug("Using cluster configuration file '%s'", filepath)
  with open(filepath, "r") as f:
    config = json.load(f)

  return cluster_from_metis_config(config)


def cluster_from_metis_config(config):
  """
  Construct a Cluster from a metis-flavored object.

  Args:
    config (dict): Metis data.

  Returns:
    Cluster
  """
  curie_settings = curie_server_state_pb2.CurieSettings()
  cluster = curie_settings.Cluster()
  cluster.cluster_name = config["cluster.name"]
  log.info("Using cluster %s", cluster.cluster_name)

  # Manager.
  if config["manager.type"].lower() == "prism":
    cluster.cluster_hypervisor_info.ahv_info.SetInParent()
    prism_info = cluster.cluster_management_server_info.prism_info
    prism_info.prism_host = config["prism.address"]
    prism_info.prism_username = config["prism.username"]
    prism_info.prism_password = config["prism.password"]
    prism_info.prism_cluster_id = config["prism.cluster"]
    prism_info.prism_container_id = config["prism.container"]
    prism_info.prism_network_id = config["prism.network"]
  elif config["manager.type"].lower() == "vcenter":
    cluster.cluster_hypervisor_info.esx_info.SetInParent()
    vcenter_info = cluster.cluster_management_server_info.vcenter_info
    vcenter_info.vcenter_host = config["vcenter.address"]
    vcenter_info.vcenter_user = config["vcenter.username"]
    vcenter_info.vcenter_password = config["vcenter.password"]
    vcenter_info.vcenter_datacenter_name = config["vcenter.datacenter"]
    vcenter_info.vcenter_cluster_name = config["vcenter.cluster"]
    vcenter_info.vcenter_datastore_name = config["vcenter.datastore"]
    vcenter_info.vcenter_network_name = config["vcenter.network"]
  elif config["manager.type"].lower() == "scvmm":
    cluster.cluster_hypervisor_info.hyperv_info.SetInParent()
    vmm_info = cluster.cluster_management_server_info.vmm_info
    vmm_info.vmm_server = config["scvmm.address"]
    vmm_info.vmm_user = config["scvmm.username"]
    vmm_info.vmm_password = config["scvmm.password"]
    vmm_info.vmm_library_server = config["scvmm.library_server_address"]
    vmm_info.vmm_library_server_share_path = config["scvmm.library_server_share_path"]
    vmm_info.vmm_cluster_name = config["scvmm.cluster"]
    vmm_info.vmm_share_path = config["scvmm.share_path"]
    vmm_info.vmm_network_name = config["scvmm.network"]
  else:
    raise ValueError("Unsupported manager.type '%s'" % config["manager.type"])

  # OoB.
  oob_management_info = curie_settings.ClusterNode.NodeOutOfBandManagementInfo
  oob_interface_types = dict(oob_management_info.InterfaceType.items())
  oob_vendors = dict(oob_management_info.Vendor.items())
  if "k" + config["oob.type"].title() not in oob_interface_types:
    raise ValueError("Unsupported oob.type '%s'" % config["oob.type"])
  if "k" + config["ipmi.vendor"].title() not in oob_vendors:
    raise ValueError("Unsupported ipmi.vendor '%s'" % config["ipmi.vendor"])

  # Nodes.
  for node_config in config["nodes"]:
    cluster_node = cluster.cluster_nodes.add()
    cluster_node.id = node_config["hypervisor_addr"]
    try:
      cluster_node.svm_addr = node_config["svm_addr"]
    except KeyError as err:
      log.warning("Error parsing JSON: %s", err.message)

    cluster_node.node_out_of_band_management_info.SetInParent()
    oob = cluster_node.node_out_of_band_management_info
    oob.interface_type = oob_interface_types["k" + config["oob.type"].title()]
    oob.vendor = oob_vendors["k" + config["ipmi.vendor"].title()]
    oob.username = config["ipmi.username"]
    oob.password = config["ipmi.password"]
    oob.ip_address = node_config["ipmi_addr"]

  # Cluster.
  cluster_software_info = cluster.cluster_software_info
  if config["cluster.type"].lower() == "nutanix":
    cluster_software_info.nutanix_info.SetInParent()
    nutanix_info = cluster_software_info.nutanix_info
    # TODO (jklein): Remove once all of the CI configs have been updated.
    if not config.get("prism.address"):
      raise ValueError("Nutanix cluster is missing required virtual IP")
    nutanix_info.prism_host = config["prism.address"]
    nutanix_info.prism_user = config["prism.username"]
    nutanix_info.prism_password = config["prism.password"]
  elif config["cluster.type"].lower() == "vsan":
    cluster_software_info.vsan_info.SetInParent()
  else:
    cluster_software_info.generic_info.SetInParent()

  if cluster.cluster_hypervisor_info.HasField("esx_info"):
    if cluster.cluster_software_info.HasField("nutanix_info"):
      return NutanixVsphereCluster(cluster)
    else:
      return GenericVsphereCluster(cluster)
  elif cluster.cluster_hypervisor_info.HasField("hyperv_info"):
    if cluster.cluster_software_info.HasField("nutanix_info"):
      return NutanixHypervCluster(cluster)
    else:
      return HyperVCluster(cluster)
  elif cluster.cluster_hypervisor_info.HasField("ahv_info"):
    return AcropolisCluster(cluster)
  else:
    raise ValueError("Unsupported set of hypervisor and cluster type")
