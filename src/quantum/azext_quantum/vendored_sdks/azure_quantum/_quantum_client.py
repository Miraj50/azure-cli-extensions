# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import PipelineClient

from . import models
from ._configuration import QuantumClientConfiguration
from .operations import JobsOperations, ProvidersOperations, QuotasOperations, StorageOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest, HttpResponse

class QuantumClient(object):
    """Azure Quantum REST API client.

    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.quantum._client.operations.JobsOperations
    :ivar providers: ProvidersOperations operations
    :vartype providers: azure.quantum._client.operations.ProvidersOperations
    :ivar storage: StorageOperations operations
    :vartype storage: azure.quantum._client.operations.StorageOperations
    :ivar quotas: QuotasOperations operations
    :vartype quotas: azure.quantum._client.operations.QuotasOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g.
     00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param workspace_name: Name of the workspace.
    :type workspace_name: str
    :param base_url: Service URL. Default value is "https://quantum.azure.com".
    :type base_url: str
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        resource_group_name,  # type: str
        workspace_name,  # type: str
        base_url="https://quantum.azure.com",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self._config = QuantumClientConfiguration(credential=credential, subscription_id=subscription_id, resource_group_name=resource_group_name, workspace_name=workspace_name, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.jobs = JobsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.providers = ProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.storage = StorageOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.quotas = QuotasOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> QuantumClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
