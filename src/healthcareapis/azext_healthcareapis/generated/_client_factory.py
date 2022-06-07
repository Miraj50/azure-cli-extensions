# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_healthcareapis_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.healthcareapis import HealthcareApisManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   HealthcareApisManagementClient)


def cf_service(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).services


def cf_operation_result(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).operation_results


def cf_private_endpoint_connection(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).private_endpoint_connections


def cf_private_link_resource(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).private_link_resources


def cf_workspace(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).workspaces


def cf_dicom_service(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).dicom_services


def cf_iot_connector(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).iot_connectors


def cf_fhir_destination(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).fhir_destinations


def cf_iot_connector_fhir_destination(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).iot_connector_fhir_destination


def cf_fhir_service(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).fhir_services


def cf_workspace_private_endpoint_connection(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).workspace_private_endpoint_connections


def cf_workspace_private_link_resource(cli_ctx, *_):
    return cf_healthcareapis_cl(cli_ctx).workspace_private_link_resources
