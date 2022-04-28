# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import DataShareManagementClientConfiguration
from .operations import AccountsOperations
from .operations import ConsumerInvitationsOperations
from .operations import DataSetsOperations
from .operations import DataSetMappingsOperations
from .operations import EmailRegistrationsOperations
from .operations import InvitationsOperations
from .operations import Operations
from .operations import SharesOperations
from .operations import ProviderShareSubscriptionsOperations
from .operations import ShareSubscriptionsOperations
from .operations import ConsumerSourceDataSetsOperations
from .operations import SynchronizationSettingsOperations
from .operations import TriggersOperations
from .. import models


class DataShareManagementClient(object):
    """Creates a Microsoft.DataShare management client.

    :ivar accounts: AccountsOperations operations
    :vartype accounts: azure.mgmt.datashare.aio.operations.AccountsOperations
    :ivar consumer_invitations: ConsumerInvitationsOperations operations
    :vartype consumer_invitations: azure.mgmt.datashare.aio.operations.ConsumerInvitationsOperations
    :ivar data_sets: DataSetsOperations operations
    :vartype data_sets: azure.mgmt.datashare.aio.operations.DataSetsOperations
    :ivar data_set_mappings: DataSetMappingsOperations operations
    :vartype data_set_mappings: azure.mgmt.datashare.aio.operations.DataSetMappingsOperations
    :ivar email_registrations: EmailRegistrationsOperations operations
    :vartype email_registrations: azure.mgmt.datashare.aio.operations.EmailRegistrationsOperations
    :ivar invitations: InvitationsOperations operations
    :vartype invitations: azure.mgmt.datashare.aio.operations.InvitationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datashare.aio.operations.Operations
    :ivar shares: SharesOperations operations
    :vartype shares: azure.mgmt.datashare.aio.operations.SharesOperations
    :ivar provider_share_subscriptions: ProviderShareSubscriptionsOperations operations
    :vartype provider_share_subscriptions: azure.mgmt.datashare.aio.operations.ProviderShareSubscriptionsOperations
    :ivar share_subscriptions: ShareSubscriptionsOperations operations
    :vartype share_subscriptions: azure.mgmt.datashare.aio.operations.ShareSubscriptionsOperations
    :ivar consumer_source_data_sets: ConsumerSourceDataSetsOperations operations
    :vartype consumer_source_data_sets: azure.mgmt.datashare.aio.operations.ConsumerSourceDataSetsOperations
    :ivar synchronization_settings: SynchronizationSettingsOperations operations
    :vartype synchronization_settings: azure.mgmt.datashare.aio.operations.SynchronizationSettingsOperations
    :ivar triggers: TriggersOperations operations
    :vartype triggers: azure.mgmt.datashare.aio.operations.TriggersOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataShareManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.accounts = AccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.consumer_invitations = ConsumerInvitationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_sets = DataSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_set_mappings = DataSetMappingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.email_registrations = EmailRegistrationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invitations = InvitationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.shares = SharesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.provider_share_subscriptions = ProviderShareSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_subscriptions = ShareSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.consumer_source_data_sets = ConsumerSourceDataSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.synchronization_settings = SynchronizationSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.triggers = TriggersOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DataShareManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
