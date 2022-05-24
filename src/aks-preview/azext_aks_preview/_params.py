# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long,too-many-statements

import os.path
import platform

from argcomplete.completers import FilesCompleter
from azure.cli.core.commands.parameters import (
    edge_zone_type,
    file_type,
    get_enum_type,
    get_resource_name_completion_list,
    get_three_state_flag,
    name_type,
    tags_type,
    zones_type,
)
from knack.arguments import CLIArgumentType

from ._completers import (
    get_k8s_upgrades_completion_list,
    get_k8s_versions_completion_list,
    get_vm_size_completion_list,
)
from ._consts import (
    CONST_CREDENTIAL_FORMAT_AZURE,
    CONST_CREDENTIAL_FORMAT_EXEC,
    CONST_GPU_INSTANCE_PROFILE_MIG1_G,
    CONST_GPU_INSTANCE_PROFILE_MIG2_G,
    CONST_GPU_INSTANCE_PROFILE_MIG3_G,
    CONST_GPU_INSTANCE_PROFILE_MIG4_G,
    CONST_GPU_INSTANCE_PROFILE_MIG7_G,
    CONST_LOAD_BALANCER_SKU_BASIC,
    CONST_LOAD_BALANCER_SKU_STANDARD,
    CONST_NETWORK_PLUGIN_AZURE,
    CONST_NETWORK_PLUGIN_KUBENET,
    CONST_NETWORK_PLUGIN_NONE,
    CONST_NODE_IMAGE_UPGRADE_CHANNEL,
    CONST_NODEPOOL_MODE_SYSTEM,
    CONST_NODEPOOL_MODE_USER,
    CONST_NONE_UPGRADE_CHANNEL,
    CONST_OS_DISK_TYPE_EPHEMERAL,
    CONST_OS_DISK_TYPE_MANAGED,
    CONST_OS_SKU_CBLMARINER,
    CONST_OS_SKU_UBUNTU,
    CONST_OS_SKU_WINDOWS2019,
    CONST_OS_SKU_WINDOWS2022,
    CONST_OUTBOUND_TYPE_LOAD_BALANCER,
    CONST_OUTBOUND_TYPE_MANAGED_NAT_GATEWAY,
    CONST_OUTBOUND_TYPE_USER_ASSIGNED_NAT_GATEWAY,
    CONST_OUTBOUND_TYPE_USER_DEFINED_ROUTING,
    CONST_PATCH_UPGRADE_CHANNEL,
    CONST_RAPID_UPGRADE_CHANNEL,
    CONST_SCALE_DOWN_MODE_DEALLOCATE,
    CONST_SCALE_DOWN_MODE_DELETE,
    CONST_SCALE_SET_PRIORITY_REGULAR,
    CONST_SCALE_SET_PRIORITY_SPOT,
    CONST_SPOT_EVICTION_POLICY_DEALLOCATE,
    CONST_SPOT_EVICTION_POLICY_DELETE,
    CONST_STABLE_UPGRADE_CHANNEL,
    CONST_WORKLOAD_RUNTIME_OCI_CONTAINER,
    CONST_WORKLOAD_RUNTIME_WASM_WASI,
)
from ._validators import (
    validate_acr,
    validate_addon,
    validate_addons,
    validate_apiserver_subnet_id,
    validate_assign_identity,
    validate_assign_kubelet_identity,
    validate_azure_keyvault_kms_key_id,
    validate_cluster_id,
    validate_cluster_snapshot_id,
    validate_create_parameters,
    validate_crg_id,
    validate_eviction_policy,
    validate_host_group_id,
    validate_ip_ranges,
    validate_k8s_version,
    validate_linux_host_name,
    validate_load_balancer_idle_timeout,
    validate_load_balancer_outbound_ip_prefixes,
    validate_load_balancer_outbound_ips,
    validate_load_balancer_outbound_ports,
    validate_load_balancer_sku,
    validate_max_surge,
    validate_message_of_the_day,
    validate_nat_gateway_idle_timeout,
    validate_nat_gateway_managed_outbound_ip_count,
    validate_nodepool_id,
    validate_nodepool_labels,
    validate_nodepool_name,
    validate_nodepool_tags,
    validate_nodes_count,
    validate_pod_identity_pod_labels,
    validate_pod_identity_resource_name,
    validate_pod_identity_resource_namespace,
    validate_pod_subnet_id,
    validate_priority,
    validate_snapshot_id,
    validate_snapshot_name,
    validate_spot_max_price,
    validate_ssh_key,
    validate_taints,
    validate_user,
    validate_vm_set_type,
    validate_vnet_subnet_id,
)

# candidates for enumeration
# consts for AgentPool
node_priorities = [CONST_SCALE_SET_PRIORITY_REGULAR, CONST_SCALE_SET_PRIORITY_SPOT]
node_eviction_policies = [CONST_SPOT_EVICTION_POLICY_DELETE, CONST_SPOT_EVICTION_POLICY_DEALLOCATE]
node_os_disk_types = [CONST_OS_DISK_TYPE_MANAGED, CONST_OS_DISK_TYPE_EPHEMERAL]
node_mode_types = [CONST_NODEPOOL_MODE_SYSTEM, CONST_NODEPOOL_MODE_USER]
node_os_skus = [CONST_OS_SKU_UBUNTU, CONST_OS_SKU_CBLMARINER, CONST_OS_SKU_WINDOWS2019, CONST_OS_SKU_WINDOWS2022]
scale_down_modes = [CONST_SCALE_DOWN_MODE_DELETE, CONST_SCALE_DOWN_MODE_DEALLOCATE]
workload_runtimes = [CONST_WORKLOAD_RUNTIME_OCI_CONTAINER, CONST_WORKLOAD_RUNTIME_WASM_WASI]
gpu_instance_profiles = [
    CONST_GPU_INSTANCE_PROFILE_MIG1_G,
    CONST_GPU_INSTANCE_PROFILE_MIG2_G,
    CONST_GPU_INSTANCE_PROFILE_MIG3_G,
    CONST_GPU_INSTANCE_PROFILE_MIG4_G,
    CONST_GPU_INSTANCE_PROFILE_MIG7_G,
]

# consts for ManagedCluster
load_balancer_skus = [CONST_LOAD_BALANCER_SKU_BASIC, CONST_LOAD_BALANCER_SKU_STANDARD]
network_plugins = [CONST_NETWORK_PLUGIN_KUBENET, CONST_NETWORK_PLUGIN_AZURE, CONST_NETWORK_PLUGIN_NONE]
outbound_types = [
    CONST_OUTBOUND_TYPE_LOAD_BALANCER,
    CONST_OUTBOUND_TYPE_USER_DEFINED_ROUTING,
    CONST_OUTBOUND_TYPE_MANAGED_NAT_GATEWAY,
    CONST_OUTBOUND_TYPE_USER_ASSIGNED_NAT_GATEWAY,
]
auto_upgrade_channels = [
    CONST_RAPID_UPGRADE_CHANNEL,
    CONST_STABLE_UPGRADE_CHANNEL,
    CONST_PATCH_UPGRADE_CHANNEL,
    CONST_NODE_IMAGE_UPGRADE_CHANNEL,
    CONST_NONE_UPGRADE_CHANNEL,
]

# consts for credential
credential_formats = [CONST_CREDENTIAL_FORMAT_AZURE, CONST_CREDENTIAL_FORMAT_EXEC]


def load_arguments(self, _):

    acr_arg_type = CLIArgumentType(metavar='ACR_NAME_OR_RESOURCE_ID')

    # AKS command argument configuration
    with self.argument_context('aks') as c:
        c.argument('resource_name', name_type, help='Name of the managed cluster.',
                   completer=get_resource_name_completion_list('Microsoft.ContainerService/ManagedClusters'))
        c.argument('name', name_type, help='Name of the managed cluster.',
                   completer=get_resource_name_completion_list('Microsoft.ContainerService/ManagedClusters'))
        c.argument('kubernetes_version', options_list=[
                   '--kubernetes-version', '-k'], validator=validate_k8s_version)
        c.argument('node_count', options_list=['--node-count', '-c'], type=int)
        c.argument('tags', tags_type)

    with self.argument_context('aks create') as c:
        # managed cluster paramerters
        c.argument('name', validator=validate_linux_host_name)
        c.argument('kubernetes_version',
                   completer=get_k8s_versions_completion_list)
        c.argument('dns_name_prefix', options_list=['--dns-name-prefix', '-p'])
        c.argument('node_osdisk_diskencryptionset_id', options_list=['--node-osdisk-diskencryptionset-id', '-d'])
        c.argument('disable_local_accounts', action='store_true')
        c.argument('disable_rbac', action='store_true')
        c.argument('enable_rbac', action='store_true', options_list=['--enable-rbac', '-r'],
                   deprecate_info=c.deprecate(redirect="--disable-rbac", hide="2.0.45"))
        c.argument('edge_zone', edge_zone_type)
        c.argument('admin_username', options_list=['--admin-username', '-u'], default='azureuser')
        c.argument('generate_ssh_keys', action='store_true', validator=validate_create_parameters)
        c.argument('ssh_key_value', required=False, type=file_type, default=os.path.join('~', '.ssh', 'id_rsa.pub'),
                   completer=FilesCompleter(), validator=validate_ssh_key)
        c.argument('no_ssh_key', options_list=['--no-ssh-key', '-x'])
        c.argument('dns_service_ip')
        c.argument('docker_bridge_address')
        c.argument('pod_cidrs')
        c.argument('service_cidrs')
        c.argument('load_balancer_sku', arg_type=get_enum_type(load_balancer_skus), validator=validate_load_balancer_sku)
        c.argument('load_balancer_managed_outbound_ip_count', type=int)
        c.argument('load_balancer_managed_outbound_ipv6_count', type=int)
        c.argument('load_balancer_outbound_ips', validator=validate_load_balancer_outbound_ips)
        c.argument('load_balancer_outbound_ip_prefixes', validator=validate_load_balancer_outbound_ip_prefixes)
        c.argument('load_balancer_outbound_ports', type=int, validator=validate_load_balancer_outbound_ports)
        c.argument('load_balancer_idle_timeout', type=int, validator=validate_load_balancer_idle_timeout)
        c.argument('nat_gateway_managed_outbound_ip_count', type=int, validator=validate_nat_gateway_managed_outbound_ip_count)
        c.argument('nat_gateway_idle_timeout', type=int, validator=validate_nat_gateway_idle_timeout)
        c.argument('outbound_type', arg_type=get_enum_type(outbound_types))
        c.argument('network_plugin', arg_type=get_enum_type(network_plugins))
        c.argument('network_policy')
        c.argument('auto_upgrade_channel', arg_type=get_enum_type(auto_upgrade_channels))
        c.argument('cluster_autoscaler_profile', nargs='+')
        c.argument('uptime_sla', action='store_true')
        c.argument('fqdn_subdomain')
        c.argument('api_server_authorized_ip_ranges', validator=validate_ip_ranges)
        c.argument('enable_private_cluster', action='store_true')
        c.argument('private_dns_zone')
        c.argument('disable_public_fqdn', action='store_true')
        c.argument('service_principal')
        c.argument('client_secret')
        c.argument('enable_managed_identity', action='store_true')
        c.argument('assign_identity', validator=validate_assign_identity)
        c.argument('assign_kubelet_identity', validator=validate_assign_kubelet_identity)
        c.argument('enable_aad', action='store_true')
        c.argument('enable_azure_rbac', action='store_true')
        c.argument('aad_client_app_id')
        c.argument('aad_server_app_id')
        c.argument('aad_server_app_secret')
        c.argument('aad_tenant_id')
        c.argument('aad_admin_group_object_ids')
        c.argument('windows_admin_username')
        c.argument('windows_admin_password')
        c.argument('enable_ahub')
        c.argument('disable_ahub')
        c.argument('gmsa_dns_server')
        c.argument('gmsa_root_domain_name')
        c.argument('attach_acr', acr_arg_type)
        c.argument('skip_subnet_role_assignment', action='store_true')
        # addons
        c.argument('enable_addons', options_list=['--enable-addons', '-a'], validator=validate_addons)
        c.argument('workspace_resource_id')
        c.argument('enable_msi_auth_for_monitoring', arg_type=get_three_state_flag(), is_preview=True)
        c.argument('aci_subnet_name')
        c.argument('appgw_name', arg_group='Application Gateway')
        c.argument('appgw_subnet_prefix', arg_group='Application Gateway', deprecate_info=c.deprecate(redirect='--appgw-subnet-cidr', hide=True))
        c.argument('appgw_subnet_cidr', arg_group='Application Gateway')
        c.argument('appgw_id', arg_group='Application Gateway')
        c.argument('appgw_subnet_id', arg_group='Application Gateway')
        c.argument('appgw_watch_namespace', arg_group='Application Gateway')
        c.argument('enable_secret_rotation', action='store_true')
        c.argument('rotation_poll_interval')
        c.argument('enable_sgxquotehelper', action='store_true')
        # nodepool paramerters
        c.argument('nodepool_name', default='nodepool1',
                   help='Node pool name, upto 12 alphanumeric characters', validator=validate_nodepool_name)
        c.argument('node_vm_size', options_list=[
                   '--node-vm-size', '-s'], completer=get_vm_size_completion_list)
        c.argument('os_sku', arg_type=get_enum_type(node_os_skus))
        c.argument('vnet_subnet_id', validator=validate_vnet_subnet_id)
        c.argument('pod_subnet_id', validator=validate_pod_subnet_id)
        c.argument('enable_node_public_ip', action='store_true')
        c.argument('node_public_ip_prefix_id')
        c.argument('enable_cluster_autoscaler', action='store_true')
        c.argument('min_count', type=int, validator=validate_nodes_count)
        c.argument('max_count', type=int, validator=validate_nodes_count)
        c.argument('nodepool_tags', nargs='*', validator=validate_nodepool_tags,
                   help='space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.')
        c.argument('nodepool_labels', nargs='*', validator=validate_nodepool_labels,
                   help='space-separated labels: key[=value] [key[=value] ...]. See https://aka.ms/node-labels for syntax of labels.')
        c.argument('node_osdisk_type', arg_type=get_enum_type(node_os_disk_types))
        c.argument('node_osdisk_size', type=int)
        c.argument('max_pods', type=int, options_list=['--max-pods', '-m'])
        c.argument('vm_set_type', validator=validate_vm_set_type)
        c.argument('enable_vmss', action='store_true', help='To be deprecated. Use vm_set_type instead.', deprecate_info=c.deprecate(redirect='--vm-set-type', hide=True))
        c.argument('node_zones', zones_type, options_list=['--node-zones'], help='(--node-zones will be deprecated) Space-separated list of availability zones where agent nodes will be placed.', deprecate_info=c.deprecate(redirect='--zones', hide='2.37.0'))
        c.argument('zones', zones_type, options_list=['--zones', '-z'], help='Space-separated list of availability zones where agent nodes will be placed.')
        c.argument('ppg')
        c.argument('enable_encryption_at_host', arg_type=get_three_state_flag(), help='Enable EncryptionAtHost.')
        c.argument('enable_ultra_ssd', action='store_true')
        c.argument('enable_fips_image', action='store_true')
        c.argument('snapshot_id', validator=validate_snapshot_id)
        c.argument('kubelet_config')
        c.argument('linux_os_config')
        c.argument('disable_disk_driver', arg_type=get_three_state_flag())
        c.argument('disable_file_driver', arg_type=get_three_state_flag())
        c.argument('disable_snapshot_controller', arg_type=get_three_state_flag())
        c.argument('yes', options_list=[
                   '--yes', '-y'], help='Do not prompt for confirmation.', action='store_true')
        c.argument('aks_custom_headers')
        # extensions
        # managed cluster
        c.argument('node_resource_group')
        c.argument('ip_families')
        c.argument('http_proxy_config')
        c.argument('enable_pod_security_policy', action='store_true')
        c.argument('enable_pod_identity', action='store_true')
        c.argument('enable_workload_identity', arg_type=get_three_state_flag(), is_preview=True)
        c.argument('enable_oidc_issuer', action='store_true', is_preview=True)
        c.argument('enable_azure_keyvault_kms', action='store_true', is_preview=True)
        c.argument('azure_keyvault_kms_key_id', validator=validate_azure_keyvault_kms_key_id, is_preview=True)
        c.argument('cluster_snapshot_id', validator=validate_cluster_snapshot_id, is_preview=True)
        # nodepool
        c.argument('host_group_id', validator=validate_host_group_id, is_preview=True)
        c.argument('crg_id', validator=validate_crg_id, is_preview=True)
        # no validation for aks create because it already only supports Linux.
        c.argument('message_of_the_day')
        c.argument('gpu_instance_profile', arg_type=get_enum_type(gpu_instance_profiles))
        c.argument('workload_runtime', arg_type=get_enum_type(workload_runtimes), default=CONST_WORKLOAD_RUNTIME_OCI_CONTAINER)
        c.argument('enable_apiserver_vnet_integration', action='store_true', is_preview=True)
        c.argument('apiserver_subnet_id', validator=validate_apiserver_subnet_id, is_preview=True)

    with self.argument_context('aks update') as c:
        # managed cluster paramerters
        c.argument('disable_local_accounts', action='store_true')
        c.argument('enable_local_accounts', action='store_true')
        c.argument('load_balancer_managed_outbound_ip_count', type=int)
        c.argument('load_balancer_managed_outbound_ipv6_count', type=int)
        c.argument('load_balancer_outbound_ips', validator=validate_load_balancer_outbound_ips)
        c.argument('load_balancer_outbound_ip_prefixes', validator=validate_load_balancer_outbound_ip_prefixes)
        c.argument('load_balancer_outbound_ports', type=int, validator=validate_load_balancer_outbound_ports)
        c.argument('load_balancer_idle_timeout', type=int, validator=validate_load_balancer_idle_timeout)
        c.argument('nat_gateway_managed_outbound_ip_count', type=int, validator=validate_nat_gateway_managed_outbound_ip_count)
        c.argument('nat_gateway_idle_timeout', type=int, validator=validate_nat_gateway_idle_timeout)
        c.argument('auto_upgrade_channel', arg_type=get_enum_type(auto_upgrade_channels))
        c.argument('cluster_autoscaler_profile', nargs='+')
        c.argument('uptime_sla', action='store_true')
        c.argument('no_uptime_sla', action='store_true')
        c.argument('api_server_authorized_ip_ranges', validator=validate_ip_ranges)
        c.argument('enable_public_fqdn', action='store_true')
        c.argument('disable_public_fqdn', action='store_true')
        c.argument('enable_managed_identity', action='store_true')
        c.argument('assign_identity', validator=validate_assign_identity)
        c.argument('assign_kubelet_identity', validator=validate_assign_kubelet_identity)
        c.argument('enable_aad', action='store_true')
        c.argument('enable_azure_rbac', action='store_true')
        c.argument('disable_azure_rbac', action='store_true')
        c.argument('aad_tenant_id')
        c.argument('aad_admin_group_object_ids')
        c.argument('windows_admin_password')
        c.argument('enable_ahub')
        c.argument('disable_ahub')
        c.argument('enable_windows_gmsa', action='store_true')
        c.argument('gmsa_dns_server')
        c.argument('gmsa_root_domain_name')
        c.argument('enable_disk_driver', arg_type=get_three_state_flag())
        c.argument('disable_disk_driver', arg_type=get_three_state_flag())
        c.argument('enable_file_driver', arg_type=get_three_state_flag())
        c.argument('disable_file_driver', arg_type=get_three_state_flag())
        c.argument('enable_snapshot_controller', arg_type=get_three_state_flag())
        c.argument('disable_snapshot_controller', arg_type=get_three_state_flag())
        c.argument('attach_acr', acr_arg_type, validator=validate_acr)
        c.argument('detach_acr', acr_arg_type, validator=validate_acr)
        # addons
        c.argument('enable_secret_rotation', action='store_true')
        c.argument('disable_secret_rotation', action='store_true')
        c.argument('rotation_poll_interval')
        # nodepool paramerters
        c.argument('enable_cluster_autoscaler', options_list=[
                   "--enable-cluster-autoscaler", "-e"], action='store_true')
        c.argument('disable_cluster_autoscaler', options_list=[
                   "--disable-cluster-autoscaler", "-d"], action='store_true')
        c.argument('update_cluster_autoscaler', options_list=[
                   "--update-cluster-autoscaler", "-u"], action='store_true')
        c.argument('min_count', type=int, validator=validate_nodes_count)
        c.argument('max_count', type=int, validator=validate_nodes_count)
        c.argument('nodepool_labels', nargs='*', validator=validate_nodepool_labels,
                   help='space-separated labels: key[=value] [key[=value] ...]. See https://aka.ms/node-labels for syntax of labels.')
        c.argument('yes', options_list=[
                   '--yes', '-y'], help='Do not prompt for confirmation.', action='store_true')
        c.argument('aks_custom_headers')
        # extensions
        # managed cluster
        c.argument('http_proxy_config')
        c.argument('enable_pod_security_policy', action='store_true')
        c.argument('disable_pod_security_policy', action='store_true')
        c.argument('enable_pod_identity', action='store_true')
        c.argument('disable_pod_identity', action='store_true')
        c.argument('enable_workload_identity', arg_type=get_three_state_flag(), is_preview=True)
        c.argument('disable_workload_identity', arg_type=get_three_state_flag(), is_preview=True)
        c.argument('enable_oidc_issuer', action='store_true', is_preview=True)
        c.argument('enable_azure_keyvault_kms', action='store_true', is_preview=True)
        c.argument('azure_keyvault_kms_key_id', validator=validate_azure_keyvault_kms_key_id, is_preview=True)
        c.argument('enable_apiserver_vnet_integration', action='store_true', is_preview=True)
        c.argument('apiserver_subnet_id', validator=validate_apiserver_subnet_id, is_preview=True)

    with self.argument_context('aks scale') as c:
        c.argument('nodepool_name',
                   help='Node pool name, upto 12 alphanumeric characters', validator=validate_nodepool_name)

    with self.argument_context('aks upgrade') as c:
        c.argument('kubernetes_version',
                   completer=get_k8s_upgrades_completion_list)
        c.argument('yes', options_list=[
                   '--yes', '-y'], help='Do not prompt for confirmation.', action='store_true')

    with self.argument_context('aks maintenanceconfiguration') as c:
        c.argument('cluster_name', help='The cluster name.')

    for scope in ['aks maintenanceconfiguration add', 'aks maintenanceconfiguration update']:
        with self.argument_context(scope) as c:
            c.argument('config_name', options_list=[
                       '--name', '-n'], help='The config name.')
            c.argument('config_file', options_list=[
                       '--config-file'], help='The config json file.', required=False)
            c.argument('weekday', options_list=[
                       '--weekday'], help='weekday on which maintenance can happen. e.g. Monday', required=False)
            c.argument('start_hour', type=int, options_list=[
                       '--start-hour'], help='maintenance start hour of 1 hour window on the weekday. e.g. 1 means 1:00am - 2:00am', required=False)

    for scope in ['aks maintenanceconfiguration show', 'aks maintenanceconfiguration delete']:
        with self.argument_context(scope) as c:
            c.argument('config_name', options_list=[
                       '--name', '-n'], help='The config name.')

    with self.argument_context('aks nodepool') as c:
        c.argument('cluster_name', help='The cluster name.')

    for scope in ['aks nodepool add']:
        with self.argument_context(scope) as c:
            c.argument('nodepool_name', options_list=[
                       '--name', '-n'], validator=validate_nodepool_name, help='The node pool name.')
            c.argument('node_vm_size', options_list=[
                       '--node-vm-size', '-s'], completer=get_vm_size_completion_list)
            c.argument('os_type')
            c.argument('os_sku', arg_type=get_enum_type(node_os_skus))
            c.argument('vnet_subnet_id',
                       validator=validate_vnet_subnet_id)
            c.argument('pod_subnet_id',
                       validator=validate_pod_subnet_id)
            c.argument('enable_node_public_ip', action='store_true')
            c.argument('node_public_ip_prefix_id')
            c.argument('enable_cluster_autoscaler', options_list=[
                       "--enable-cluster-autoscaler", "-e"], action='store_true')
            c.argument('min_count', type=int, validator=validate_nodes_count)
            c.argument('max_count', type=int, validator=validate_nodes_count)
            c.argument('priority', arg_type=get_enum_type(node_priorities), validator=validate_priority)
            c.argument('eviction_policy', arg_type=get_enum_type(node_eviction_policies), validator=validate_eviction_policy)
            c.argument('spot_max_price', type=float,
                       validator=validate_spot_max_price)
            c.argument('labels', nargs='*', validator=validate_nodepool_labels)
            c.argument('tags', tags_type)
            c.argument('node_taints', validator=validate_taints)
            c.argument('node_osdisk_type', arg_type=get_enum_type(node_os_disk_types))
            c.argument('node_osdisk_size', type=int)
            c.argument('mode', arg_type=get_enum_type(node_mode_types))
            c.argument('scale_down_mode', arg_type=get_enum_type(scale_down_modes))
            c.argument('max_surge', validator=validate_max_surge)
            c.argument('max_pods', type=int, options_list=['--max-pods', '-m'])
            c.argument('node_zones', zones_type, options_list=['--node-zones'], help='(--node-zones will be deprecated) Space-separated list of availability zones where agent nodes will be placed.', deprecate_info=c.deprecate(redirect='--zones', hide='2.37.0'))
            c.argument('zones', zones_type, options_list=['--zones', '-z'], help='Space-separated list of availability zones where agent nodes will be placed.')
            c.argument('ppg')
            c.argument('enable_encryption_at_host', options_list=[
                       '--enable-encryption-at-host'], action='store_true')
            c.argument('enable_ultra_ssd', action='store_true')
            c.argument('enable_fips_image', action='store_true')
            c.argument('snapshot_id', validator=validate_snapshot_id)
            c.argument('kubelet_config')
            c.argument('linux_os_config')
            c.argument('aks_custom_headers')
            # extensions
            c.argument('host_group_id', validator=validate_host_group_id, is_preview=True)
            c.argument('crg_id', validator=validate_crg_id, is_preview=True)
            c.argument('message_of_the_day', validator=validate_message_of_the_day)
            c.argument('workload_runtime', arg_type=get_enum_type(workload_runtimes), default=CONST_WORKLOAD_RUNTIME_OCI_CONTAINER)
            c.argument('gpu_instance_profile', arg_type=get_enum_type(gpu_instance_profiles))

    for scope in ['aks nodepool show', 'aks nodepool scale', 'aks nodepool upgrade', 'aks nodepool update']:
        with self.argument_context(scope) as c:
            c.argument('nodepool_name', options_list=[
                       '--name', '-n'], validator=validate_nodepool_name, help='The node pool name.')

    with self.argument_context('aks nodepool delete') as c:
        c.argument('nodepool_name', options_list=[
            '--name', '-n'], validator=validate_nodepool_name, help='The node pool name.')
        c.argument('ignore_pod_disruption_budget', options_list=[
                   "--ignore-pod-disruption-budget", "-i"], action=get_three_state_flag(), is_preview=True,
                   help='delete an AKS nodepool by ignoring PodDisruptionBudget setting')

    with self.argument_context('aks nodepool upgrade') as c:
        c.argument('max_surge', validator=validate_max_surge)
        c.argument('aks_custom_headers')
        c.argument('snapshot_id', validator=validate_snapshot_id)

    with self.argument_context('aks nodepool update') as c:
        c.argument('enable_cluster_autoscaler', options_list=[
                   "--enable-cluster-autoscaler", "-e"], action='store_true')
        c.argument('disable_cluster_autoscaler', options_list=[
                   "--disable-cluster-autoscaler", "-d"], action='store_true')
        c.argument('update_cluster_autoscaler', options_list=[
                   "--update-cluster-autoscaler", "-u"], action='store_true')
        c.argument('min_count', type=int, validator=validate_nodes_count)
        c.argument('max_count', type=int, validator=validate_nodes_count)
        c.argument('labels', nargs='*', validator=validate_nodepool_labels)
        c.argument('tags', tags_type)
        c.argument('node_taints', validator=validate_taints)
        c.argument('mode', arg_type=get_enum_type(node_mode_types))
        c.argument('scale_down_mode', arg_type=get_enum_type(scale_down_modes))
        c.argument('max_surge', validator=validate_max_surge)

    with self.argument_context('aks addon show') as c:
        c.argument('addon', options_list=[
                   '--addon', '-a'], validator=validate_addon)

    with self.argument_context('aks addon enable') as c:
        c.argument('addon', options_list=[
                   '--addon', '-a'], validator=validate_addon)
        c.argument('subnet_name', options_list=['--subnet-name', '-s'])
        c.argument('enable_sgxquotehelper', action='store_true')
        c.argument('osm_mesh_name', options_list=['--osm-mesh-name'])
        c.argument('appgw_name', options_list=[
                   '--appgw-name'], arg_group='Application Gateway')
        c.argument('appgw_subnet_prefix', options_list=[
                   '--appgw-subnet-prefix'], arg_group='Application Gateway', deprecate_info=c.deprecate(redirect='--appgw-subnet-cidr', hide=True))
        c.argument('appgw_subnet_cidr', options_list=[
                   '--appgw-subnet-cidr'], arg_group='Application Gateway')
        c.argument('appgw_id', options_list=[
                   '--appgw-id'], arg_group='Application Gateway')
        c.argument('appgw_subnet_id', options_list=[
                   '--appgw-subnet-id'], arg_group='Application Gateway')
        c.argument('appgw_watch_namespace', options_list=[
                   '--appgw-watch-namespace'], arg_group='Application Gateway')
        c.argument('enable_secret_rotation', action='store_true')
        c.argument('rotation_poll_interval')
        c.argument('workspace_resource_id')
        c.argument('enable_msi_auth_for_monitoring',
                   arg_type=get_three_state_flag(), is_preview=True)

    with self.argument_context('aks addon disable') as c:
        c.argument('addon', options_list=[
                   '--addon', '-a'], validator=validate_addon)

    with self.argument_context('aks addon update') as c:
        c.argument('addon', options_list=[
                   '--addon', '-a'], validator=validate_addon)
        c.argument('subnet_name', options_list=['--subnet-name', '-s'])
        c.argument('enable_sgxquotehelper', action='store_true')
        c.argument('osm_mesh_name', options_list=['--osm-mesh-name'])
        c.argument('appgw_name', options_list=[
                   '--appgw-name'], arg_group='Application Gateway')
        c.argument('appgw_subnet_prefix', options_list=[
                   '--appgw-subnet-prefix'], arg_group='Application Gateway', deprecate_info=c.deprecate(redirect='--appgw-subnet-cidr', hide=True))
        c.argument('appgw_subnet_cidr', options_list=[
                   '--appgw-subnet-cidr'], arg_group='Application Gateway')
        c.argument('appgw_id', options_list=[
                   '--appgw-id'], arg_group='Application Gateway')
        c.argument('appgw_subnet_id', options_list=[
                   '--appgw-subnet-id'], arg_group='Application Gateway')
        c.argument('appgw_watch_namespace', options_list=[
                   '--appgw-watch-namespace'], arg_group='Application Gateway')
        c.argument('enable_secret_rotation', action='store_true')
        c.argument('rotation_poll_interval')
        c.argument('workspace_resource_id')
        c.argument('enable_msi_auth_for_monitoring',
                   arg_type=get_three_state_flag(), is_preview=True)

    with self.argument_context('aks disable-addons') as c:
        c.argument('addons', options_list=[
                   '--addons', '-a'], validator=validate_addons)

    with self.argument_context('aks enable-addons') as c:
        c.argument('addons', options_list=[
                   '--addons', '-a'], validator=validate_addons)
        c.argument('subnet_name', options_list=['--subnet-name', '-s'])
        c.argument('enable_sgxquotehelper', action='store_true')
        c.argument('osm_mesh_name', options_list=['--osm-mesh-name'])
        c.argument('appgw_name', options_list=[
                   '--appgw-name'], arg_group='Application Gateway')
        c.argument('appgw_subnet_prefix', options_list=[
                   '--appgw-subnet-prefix'], arg_group='Application Gateway', deprecate_info=c.deprecate(redirect='--appgw-subnet-cidr', hide=True))
        c.argument('appgw_subnet_cidr', options_list=[
                   '--appgw-subnet-cidr'], arg_group='Application Gateway')
        c.argument('appgw_id', options_list=[
                   '--appgw-id'], arg_group='Application Gateway')
        c.argument('appgw_subnet_id', options_list=[
                   '--appgw-subnet-id'], arg_group='Application Gateway')
        c.argument('appgw_watch_namespace', options_list=[
                   '--appgw-watch-namespace'], arg_group='Application Gateway')
        c.argument('enable_secret_rotation', action='store_true')
        c.argument('rotation_poll_interval')
        c.argument('workspace_resource_id')
        c.argument('enable_msi_auth_for_monitoring',
                   arg_type=get_three_state_flag(), is_preview=True)

    with self.argument_context('aks get-credentials') as c:
        c.argument('admin', options_list=['--admin', '-a'], default=False)
        c.argument('context_name', options_list=['--context'],
                   help='If specified, overwrite the default context name.')
        c.argument('user', options_list=[
                   '--user', '-u'], default='clusterUser', validator=validate_user)
        c.argument('path', options_list=['--file', '-f'], type=file_type, completer=FilesCompleter(),
                   default=os.path.join(os.path.expanduser('~'), '.kube', 'config'))
        c.argument('public_fqdn', default=False, action='store_true')
        c.argument('credential_format', options_list=['--format'], arg_type=get_enum_type(credential_formats))

    with self.argument_context('aks pod-identity') as c:
        c.argument('cluster_name', help='The cluster name.')

    with self.argument_context('aks pod-identity add') as c:
        c.argument('identity_name', options_list=['--name', '-n'], default=None, required=False,
                   help='The pod identity name. Generate if not specified.',
                   validator=validate_pod_identity_resource_name('identity_name', required=False))
        c.argument('identity_namespace', options_list=[
                   '--namespace'], help='The pod identity namespace.')
        c.argument('identity_resource_id', options_list=[
                   '--identity-resource-id'], help='Resource id of the identity to use.')
        c.argument('binding_selector', options_list=[
                   '--binding-selector'], help='Optional binding selector to use.')

    with self.argument_context('aks pod-identity delete') as c:
        c.argument('identity_name', options_list=['--name', '-n'], default=None, required=True,
                   help='The pod identity name.',
                   validator=validate_pod_identity_resource_name('identity_name', required=True))
        c.argument('identity_namespace', options_list=[
                   '--namespace'], help='The pod identity namespace.')

    with self.argument_context('aks pod-identity exception add') as c:
        c.argument('exc_name', options_list=['--name', '-n'], default=None, required=False,
                   help='The pod identity exception name. Generate if not specified.',
                   validator=validate_pod_identity_resource_name('exc_name', required=False))
        c.argument('exc_namespace', options_list=['--namespace'], required=True,
                   help='The pod identity exception namespace.',
                   validator=validate_pod_identity_resource_namespace)
        c.argument('pod_labels', nargs='*', required=True,
                   help='space-separated labels: key=value [key=value ...].',
                   validator=validate_pod_identity_pod_labels)

    with self.argument_context('aks pod-identity exception delete') as c:
        c.argument('exc_name', options_list=['--name', '-n'], required=True,
                   help='The pod identity exception name to remove.',
                   validator=validate_pod_identity_resource_name('exc_name', required=True))
        c.argument('exc_namespace', options_list=['--namespace'], required=True,
                   help='The pod identity exception namespace to remove.',
                   validator=validate_pod_identity_resource_namespace)

    with self.argument_context('aks pod-identity exception update') as c:
        c.argument('exc_name', options_list=['--name', '-n'], required=True,
                   help='The pod identity exception name to remove.',
                   validator=validate_pod_identity_resource_name('exc_name', required=True))
        c.argument('exc_namespace', options_list=['--namespace'], required=True,
                   help='The pod identity exception namespace to remove.',
                   validator=validate_pod_identity_resource_namespace)
        c.argument('pod_labels', nargs='*', required=True,
                   help='pod labels in key=value [key=value ...].',
                   validator=validate_pod_identity_pod_labels)

    for scope in ['aks nodepool snapshot create']:
        with self.argument_context(scope) as c:
            c.argument('snapshot_name', options_list=[
                       '--name', '-n'], required=True, help='The nodepool snapshot name.', validator=validate_snapshot_name)
            c.argument('tags', tags_type)
            c.argument('nodepool_id', required=True,
                       help='The nodepool id.', validator=validate_nodepool_id)
            c.argument('aks_custom_headers')

    for scope in ['aks nodepool snapshot show', 'aks nodepool snapshot delete']:
        with self.argument_context(scope) as c:
            c.argument('snapshot_name', options_list=[
                       '--name', '-n'], required=True, help='The nodepool snapshot name.', validator=validate_snapshot_name)
            c.argument('yes', options_list=[
                       '--yes', '-y'], help='Do not prompt for confirmation.', action='store_true')

    for scope in ['aks snapshot create']:
        with self.argument_context(scope) as c:
            c.argument('snapshot_name', options_list=[
                       '--name', '-n'], required=True, help='The cluster snapshot name.', validator=validate_snapshot_name)
            c.argument('tags', tags_type)
            c.argument('cluster_id', required=True,
                       validator=validate_cluster_id, help='The cluster id.')
            c.argument('aks_custom_headers')

    for scope in ['aks snapshot show', 'aks snapshot delete']:
        with self.argument_context(scope) as c:
            c.argument('snapshot_name', options_list=[
                       '--name', '-n'], required=True, help='The cluster snapshot name.', validator=validate_snapshot_name)
            c.argument('yes', options_list=[
                       '--yes', '-y'], help='Do not prompt for confirmation.', action='store_true')


def _get_default_install_location(exe_name):
    system = platform.system()
    if system == 'Windows':
        home_dir = os.environ.get('USERPROFILE')
        if not home_dir:
            return None
        install_location = os.path.join(
            home_dir, r'.azure-{0}\{0}.exe'.format(exe_name))
    elif system in ('Linux', 'Darwin'):
        install_location = '/usr/local/bin/{}'.format(exe_name)
    else:
        install_location = None
    return install_location
