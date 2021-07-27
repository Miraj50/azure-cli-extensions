# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ComplianceStatus(msrest.serialization.Model):
    """Compliance Status details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar compliance_state: The compliance state of the configuration. Possible values include:
     "Pending", "Compliant", "Noncompliant", "Installed", "Failed".
    :vartype compliance_state: str or
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ComplianceStateType
    :param last_config_applied: Datetime the configuration was last applied.
    :type last_config_applied: ~datetime.datetime
    :param message: Message from when the configuration was applied.
    :type message: str
    :param message_level: Level of the message. Possible values include: "Error", "Warning",
     "Information".
    :type message_level: str or
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.MessageLevelType
    """

    _validation = {
        'compliance_state': {'readonly': True},
    }

    _attribute_map = {
        'compliance_state': {'key': 'complianceState', 'type': 'str'},
        'last_config_applied': {'key': 'lastConfigApplied', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'message_level': {'key': 'messageLevel', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ComplianceStatus, self).__init__(**kwargs)
        self.compliance_state = None
        self.last_config_applied = kwargs.get('last_config_applied', None)
        self.message = kwargs.get('message', None)
        self.message_level = kwargs.get('message_level', None)


class ConfigurationIdentity(msrest.serialization.Model):
    """Identity for the managed cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal id of the system assigned identity which is used by the
     configuration.
    :vartype principal_id: str
    :ivar tenant_id: The tenant id of the system assigned identity which is used by the
     configuration.
    :vartype tenant_id: str
    :param type: The type of identity used for the configuration. Type 'SystemAssigned' will use an
     implicitly created identity. Type 'None' will not use Managed Identity for the configuration.
     Possible values include: "SystemAssigned", "None".
    :type type: str or
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Service specific error code which serves as the substatus for the HTTP
     error code.
    :type code: str
    :param message: Required. Description of the error.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar error: Error definition.
    :vartype error: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ErrorDefinition
    """

    _validation = {
        'error': {'readonly': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = None


class Resource(msrest.serialization.Model):
    """The Resource model definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param system_data: Top level metadata
     https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :type system_data: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = kwargs.get('system_data', None)


class ProxyResource(Resource):
    """ARM proxy resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param system_data: Top level metadata
     https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :type system_data: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)


class ExtensionInstance(ProxyResource):
    """The Extension Instance object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param system_data: Top level metadata
     https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :type system_data: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.SystemData
    :param extension_type: Type of the Extension, of which this resource is an instance of.  It
     must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the
     Extension publisher.
    :type extension_type: str
    :param auto_upgrade_minor_version: Flag to note if this instance participates in auto upgrade
     of minor version, or not.
    :type auto_upgrade_minor_version: bool
    :param release_train: ReleaseTrain this extension instance participates in for auto-upgrade
     (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
    :type release_train: str
    :param version: Version of the extension for this extension instance, if it is 'pinned' to a
     specific version. autoUpgradeMinorVersion must be 'false'.
    :type version: str
    :param scope: Scope at which the extension instance is installed.
    :type scope: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.Scope
    :param configuration_settings: Configuration settings, as name-value pairs for configuring this
     instance of the extension.
    :type configuration_settings: dict[str, str]
    :param configuration_protected_settings: Configuration settings that are sensitive, as
     name-value pairs for configuring this instance of the extension.
    :type configuration_protected_settings: dict[str, str]
    :ivar install_state: Status of installation of this instance of the extension. Possible values
     include: "Pending", "Installed", "Failed".
    :vartype install_state: str or
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.InstallStateType
    :param statuses: Status from this instance of the extension.
    :type statuses:
     list[~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ExtensionStatus]
    :ivar creation_time: DateLiteral (per ISO8601) noting the time the resource was created by the
     client (user).
    :vartype creation_time: str
    :ivar last_modified_time: DateLiteral (per ISO8601) noting the time the resource was modified
     by the client (user).
    :vartype last_modified_time: str
    :ivar last_status_time: DateLiteral (per ISO8601) noting the time of last status from the
     agent.
    :vartype last_status_time: str
    :ivar error_info: Error information from the Agent - e.g. errors during installation.
    :vartype error_info:
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ErrorDefinition
    :param identity: The identity of the configuration.
    :type identity:
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ConfigurationIdentity
    :param location: Location of resource type
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'install_state': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'last_status_time': {'readonly': True},
        'error_info': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'extension_type': {'key': 'properties.extensionType', 'type': 'str'},
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'Scope'},
        'configuration_settings': {'key': 'properties.configurationSettings', 'type': '{str}'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': '{str}'},
        'install_state': {'key': 'properties.installState', 'type': 'str'},
        'statuses': {'key': 'properties.statuses', 'type': '[ExtensionStatus]'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'str'},
        'last_status_time': {'key': 'properties.lastStatusTime', 'type': 'str'},
        'error_info': {'key': 'properties.errorInfo', 'type': 'ErrorDefinition'},
        'identity': {'key': 'identity', 'type': 'ConfigurationIdentity'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExtensionInstance, self).__init__(**kwargs)
        self.extension_type = kwargs.get('extension_type', None)
        self.auto_upgrade_minor_version = kwargs.get('auto_upgrade_minor_version', None)
        self.release_train = kwargs.get('release_train', "Stable")
        self.version = kwargs.get('version', None)
        self.scope = kwargs.get('scope', None)
        self.configuration_settings = kwargs.get('configuration_settings', None)
        self.configuration_protected_settings = kwargs.get('configuration_protected_settings', None)
        self.install_state = None
        self.statuses = kwargs.get('statuses', None)
        self.creation_time = None
        self.last_modified_time = None
        self.last_status_time = None
        self.error_info = None
        self.identity = kwargs.get('identity', None)
        self.location = kwargs.get('location', None)


class ExtensionInstancesList(msrest.serialization.Model):
    """Result of the request to list Extension Instances.  It contains a list of ExtensionInstance objects and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Extension Instances within a Kubernetes cluster.
    :vartype value:
     list[~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ExtensionInstance]
    :ivar next_link: URL to get the next set of extension instance objects, if any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ExtensionInstance]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExtensionInstancesList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class ExtensionInstanceUpdate(msrest.serialization.Model):
    """Update Extension Instance request object.

    :param auto_upgrade_minor_version: Flag to note if this instance participates in Extension
     Lifecycle Management or not.
    :type auto_upgrade_minor_version: bool
    :param release_train: ReleaseTrain this extension instance participates in for auto-upgrade
     (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
    :type release_train: str
    :param version: Version number of extension, to 'pin' to a specific version.
     autoUpgradeMinorVersion must be 'false'.
    :type version: str
    """

    _attribute_map = {
        'auto_upgrade_minor_version': {'key': 'properties.autoUpgradeMinorVersion', 'type': 'bool'},
        'release_train': {'key': 'properties.releaseTrain', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExtensionInstanceUpdate, self).__init__(**kwargs)
        self.auto_upgrade_minor_version = kwargs.get('auto_upgrade_minor_version', None)
        self.release_train = kwargs.get('release_train', "Stable")
        self.version = kwargs.get('version', None)


class ExtensionStatus(msrest.serialization.Model):
    """Status from this instance of the extension.

    :param code: Status code provided by the Extension.
    :type code: str
    :param display_status: Short description of status of this instance of the extension.
    :type display_status: str
    :param level: Level of the status. Possible values include: "Error", "Warning", "Information".
     Default value: "Information".
    :type level: str or ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.LevelType
    :param message: Detailed message of the status from the Extension instance.
    :type message: str
    :param time: DateLiteral (per ISO8601) noting the time of installation status.
    :type time: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'display_status': {'key': 'displayStatus', 'type': 'str'},
        'level': {'key': 'level', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'time': {'key': 'time', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExtensionStatus, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.display_status = kwargs.get('display_status', None)
        self.level = kwargs.get('level', "Information")
        self.message = kwargs.get('message', None)
        self.time = kwargs.get('time', None)


class HelmOperatorProperties(msrest.serialization.Model):
    """Properties for Helm operator.

    :param chart_version: Version of the operator Helm chart.
    :type chart_version: str
    :param chart_values: Values override for the operator Helm chart.
    :type chart_values: str
    """

    _attribute_map = {
        'chart_version': {'key': 'chartVersion', 'type': 'str'},
        'chart_values': {'key': 'chartValues', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(HelmOperatorProperties, self).__init__(**kwargs)
        self.chart_version = kwargs.get('chart_version', None)
        self.chart_values = kwargs.get('chart_values', None)


class ResourceProviderOperation(msrest.serialization.Model):
    """Supported operation of this resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param name: Operation name, in format of {provider}/{resource}/{operation}.
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display:
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ResourceProviderOperationDisplay
    :ivar is_data_action: The flag that indicates whether the operation applies to data plane.
    :vartype is_data_action: bool
    """

    _validation = {
        'is_data_action': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.is_data_action = None


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Resource provider: Microsoft KubernetesConfiguration.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description of this operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ResourceProviderOperationList(msrest.serialization.Model):
    """Result of the request to list operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of operations supported by this resource provider.
    :type value:
     list[~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ResourceProviderOperation]
    :ivar next_link: URL to the next set of results, if any.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = None


class Result(msrest.serialization.Model):
    """Sample result definition.

    :param sample_property: Sample property of type string.
    :type sample_property: str
    """

    _attribute_map = {
        'sample_property': {'key': 'sampleProperty', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Result, self).__init__(**kwargs)
        self.sample_property = kwargs.get('sample_property', None)


class Scope(msrest.serialization.Model):
    """Scope of the extensionInstance. It can be either Cluster or Namespace; but not both.

    :param cluster: Specifies that the scope of the extensionInstance is Cluster.
    :type cluster: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ScopeCluster
    :param namespace: Specifies that the scope of the extensionInstance is Namespace.
    :type namespace: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ScopeNamespace
    """

    _attribute_map = {
        'cluster': {'key': 'cluster', 'type': 'ScopeCluster'},
        'namespace': {'key': 'namespace', 'type': 'ScopeNamespace'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Scope, self).__init__(**kwargs)
        self.cluster = kwargs.get('cluster', None)
        self.namespace = kwargs.get('namespace', None)


class ScopeCluster(msrest.serialization.Model):
    """Specifies that the scope of the extensionInstance is Cluster.

    :param release_namespace: Namespace where the extension Release must be placed, for a Cluster
     scoped extensionInstance.  If this namespace does not exist, it will be created.
    :type release_namespace: str
    """

    _attribute_map = {
        'release_namespace': {'key': 'releaseNamespace', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ScopeCluster, self).__init__(**kwargs)
        self.release_namespace = kwargs.get('release_namespace', None)


class ScopeNamespace(msrest.serialization.Model):
    """Specifies that the scope of the extensionInstance is Namespace.

    :param target_namespace: Namespace where the extensionInstance will be created for an Namespace
     scoped extensionInstance.  If this namespace does not exist, it will be created.
    :type target_namespace: str
    """

    _attribute_map = {
        'target_namespace': {'key': 'targetNamespace', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ScopeNamespace, self).__init__(**kwargs)
        self.target_namespace = kwargs.get('target_namespace', None)


class SourceControlConfiguration(ProxyResource):
    """The SourceControl Configuration object returned in Get & Put response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param system_data: Top level metadata
     https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.
    :type system_data: ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.SystemData
    :param repository_url: Url of the SourceControl Repository.
    :type repository_url: str
    :param operator_namespace: The namespace to which this operator is installed to. Maximum of 253
     lower case alphanumeric characters, hyphen and period only.
    :type operator_namespace: str
    :param operator_instance_name: Instance name of the operator - identifying the specific
     configuration.
    :type operator_instance_name: str
    :param operator_type: Type of the operator. Possible values include: "Flux".
    :type operator_type: str or
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.OperatorType
    :param operator_params: Any Parameters for the Operator instance in string format.
    :type operator_params: str
    :param configuration_protected_settings: Name-value pairs of protected configuration settings
     for the configuration.
    :type configuration_protected_settings: dict[str, str]
    :param operator_scope: Scope at which the operator will be installed. Possible values include:
     "cluster", "namespace". Default value: "cluster".
    :type operator_scope: str or
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.OperatorScopeType
    :ivar repository_public_key: Public Key associated with this SourceControl configuration
     (either generated within the cluster or provided by the user).
    :vartype repository_public_key: str
    :param ssh_known_hosts_contents: Base64-encoded known_hosts contents containing public SSH keys
     required to access private Git instances.
    :type ssh_known_hosts_contents: str
    :param enable_helm_operator: Option to enable Helm Operator for this git configuration.
    :type enable_helm_operator: bool
    :param helm_operator_properties: Properties for Helm operator.
    :type helm_operator_properties:
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.HelmOperatorProperties
    :ivar provisioning_state: The provisioning state of the resource provider. Possible values
     include: "Accepted", "Deleting", "Running", "Succeeded", "Failed".
    :vartype provisioning_state: str or
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ProvisioningStateType
    :ivar compliance_status: Compliance Status of the Configuration.
    :vartype compliance_status:
     ~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.ComplianceStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'repository_public_key': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'compliance_status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'repository_url': {'key': 'properties.repositoryUrl', 'type': 'str'},
        'operator_namespace': {'key': 'properties.operatorNamespace', 'type': 'str'},
        'operator_instance_name': {'key': 'properties.operatorInstanceName', 'type': 'str'},
        'operator_type': {'key': 'properties.operatorType', 'type': 'str'},
        'operator_params': {'key': 'properties.operatorParams', 'type': 'str'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': '{str}'},
        'operator_scope': {'key': 'properties.operatorScope', 'type': 'str'},
        'repository_public_key': {'key': 'properties.repositoryPublicKey', 'type': 'str'},
        'ssh_known_hosts_contents': {'key': 'properties.sshKnownHostsContents', 'type': 'str'},
        'enable_helm_operator': {'key': 'properties.enableHelmOperator', 'type': 'bool'},
        'helm_operator_properties': {'key': 'properties.helmOperatorProperties', 'type': 'HelmOperatorProperties'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'compliance_status': {'key': 'properties.complianceStatus', 'type': 'ComplianceStatus'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SourceControlConfiguration, self).__init__(**kwargs)
        self.repository_url = kwargs.get('repository_url', None)
        self.operator_namespace = kwargs.get('operator_namespace', "default")
        self.operator_instance_name = kwargs.get('operator_instance_name', None)
        self.operator_type = kwargs.get('operator_type', None)
        self.operator_params = kwargs.get('operator_params', None)
        self.configuration_protected_settings = kwargs.get('configuration_protected_settings', None)
        self.operator_scope = kwargs.get('operator_scope', "cluster")
        self.repository_public_key = None
        self.ssh_known_hosts_contents = kwargs.get('ssh_known_hosts_contents', None)
        self.enable_helm_operator = kwargs.get('enable_helm_operator', None)
        self.helm_operator_properties = kwargs.get('helm_operator_properties', None)
        self.provisioning_state = None
        self.compliance_status = None


class SourceControlConfigurationList(msrest.serialization.Model):
    """Result of the request to list Source Control Configurations.  It contains a list of SourceControlConfiguration objects and a URL link to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of Source Control Configurations within a Kubernetes cluster.
    :vartype value:
     list[~azure.mgmt.kubernetesconfiguration.v2020_07_01_preview.models.SourceControlConfiguration]
    :ivar next_link: URL to get the next set of configuration objects, if any.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SourceControlConfiguration]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SourceControlConfigurationList, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class SystemData(msrest.serialization.Model):
    """Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar created_by: A string identifier for the identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource: user, application,
     managedIdentity, key.
    :vartype created_by_type: str
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: A string identifier for the identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource: user,
     application, managedIdentity, key.
    :vartype last_modified_by_type: str
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _validation = {
        'created_by': {'readonly': True},
        'created_by_type': {'readonly': True},
        'created_at': {'readonly': True},
        'last_modified_by': {'readonly': True},
        'last_modified_by_type': {'readonly': True},
        'last_modified_at': {'readonly': True},
    }

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = None
        self.created_by_type = None
        self.created_at = None
        self.last_modified_by = None
        self.last_modified_by_type = None
        self.last_modified_at = None
