# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sentinel incident list",
    is_experimental=True,
)
class List(AAZCommand):
    """Get all incidents.
    """

    _aaz_info = {
        "version": "2022-06-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.operationalinsights/workspaces/{}/providers/microsoft.securityinsights/incidents", "2022-06-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["-w", "--workspace-name"],
            help="The name of the workspace.",
            required=True,
            is_experimental=True,
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="Filters the results, based on a Boolean condition. Optional.",
        )
        _args_schema.orderby = AAZStrArg(
            options=["--orderby"],
            help="Sorts the results. Optional.",
        )
        _args_schema.skip_token = AAZStrArg(
            options=["--skip-token"],
            help="Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.",
        )
        _args_schema.top = AAZIntArg(
            options=["--top"],
            help="Returns only the first n results. Optional.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.IncidentsList(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class IncidentsList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/incidents",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$orderby", self.ctx.args.orderby,
                ),
                **self.serialize_query_param(
                    "$skipToken", self.ctx.args.skip_token,
                ),
                **self.serialize_query_param(
                    "$top", self.ctx.args.top,
                ),
                **self.serialize_query_param(
                    "api-version", "2022-06-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType()
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.additional_data = AAZObjectType(
                serialized_name="additionalData",
                flags={"read_only": True},
            )
            properties.classification = AAZStrType()
            properties.classification_comment = AAZStrType(
                serialized_name="classificationComment",
            )
            properties.classification_reason = AAZStrType(
                serialized_name="classificationReason",
            )
            properties.created_time_utc = AAZStrType(
                serialized_name="createdTimeUtc",
                flags={"read_only": True},
            )
            properties.description = AAZStrType()
            properties.first_activity_time_utc = AAZStrType(
                serialized_name="firstActivityTimeUtc",
            )
            properties.incident_number = AAZIntType(
                serialized_name="incidentNumber",
                flags={"read_only": True},
            )
            properties.incident_url = AAZStrType(
                serialized_name="incidentUrl",
                flags={"read_only": True},
            )
            properties.labels = AAZListType()
            properties.last_activity_time_utc = AAZStrType(
                serialized_name="lastActivityTimeUtc",
            )
            properties.last_modified_time_utc = AAZStrType(
                serialized_name="lastModifiedTimeUtc",
                flags={"read_only": True},
            )
            properties.owner = AAZObjectType()
            properties.provider_incident_id = AAZStrType(
                serialized_name="providerIncidentId",
            )
            properties.provider_name = AAZStrType(
                serialized_name="providerName",
            )
            properties.related_analytic_rule_ids = AAZListType(
                serialized_name="relatedAnalyticRuleIds",
                flags={"read_only": True},
            )
            properties.severity = AAZStrType(
                flags={"required": True},
            )
            properties.status = AAZStrType(
                flags={"required": True},
            )
            properties.team_information = AAZObjectType(
                serialized_name="teamInformation",
            )
            properties.title = AAZStrType(
                flags={"required": True},
            )

            additional_data = cls._schema_on_200.value.Element.properties.additional_data
            additional_data.alert_product_names = AAZListType(
                serialized_name="alertProductNames",
                flags={"read_only": True},
            )
            additional_data.alerts_count = AAZIntType(
                serialized_name="alertsCount",
                flags={"read_only": True},
            )
            additional_data.bookmarks_count = AAZIntType(
                serialized_name="bookmarksCount",
                flags={"read_only": True},
            )
            additional_data.comments_count = AAZIntType(
                serialized_name="commentsCount",
                flags={"read_only": True},
            )
            additional_data.provider_incident_url = AAZStrType(
                serialized_name="providerIncidentUrl",
                flags={"read_only": True},
            )
            additional_data.tactics = AAZListType(
                flags={"read_only": True},
            )
            additional_data.techniques = AAZListType(
                flags={"read_only": True},
            )

            alert_product_names = cls._schema_on_200.value.Element.properties.additional_data.alert_product_names
            alert_product_names.Element = AAZStrType(
                flags={"read_only": True},
            )

            tactics = cls._schema_on_200.value.Element.properties.additional_data.tactics
            tactics.Element = AAZStrType(
                flags={"read_only": True},
            )

            techniques = cls._schema_on_200.value.Element.properties.additional_data.techniques
            techniques.Element = AAZStrType(
                flags={"read_only": True},
            )

            labels = cls._schema_on_200.value.Element.properties.labels
            labels.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.labels.Element
            _element.label_name = AAZStrType(
                serialized_name="labelName",
                flags={"required": True},
            )
            _element.label_type = AAZStrType(
                serialized_name="labelType",
                flags={"read_only": True},
            )

            owner = cls._schema_on_200.value.Element.properties.owner
            owner.assigned_to = AAZStrType(
                serialized_name="assignedTo",
            )
            owner.email = AAZStrType()
            owner.object_id = AAZStrType(
                serialized_name="objectId",
            )
            owner.owner_type = AAZStrType(
                serialized_name="ownerType",
            )
            owner.user_principal_name = AAZStrType(
                serialized_name="userPrincipalName",
            )

            related_analytic_rule_ids = cls._schema_on_200.value.Element.properties.related_analytic_rule_ids
            related_analytic_rule_ids.Element = AAZStrType(
                flags={"read_only": True},
            )

            team_information = cls._schema_on_200.value.Element.properties.team_information
            team_information.description = AAZStrType(
                flags={"read_only": True},
            )
            team_information.name = AAZStrType(
                flags={"read_only": True},
            )
            team_information.primary_channel_url = AAZStrType(
                serialized_name="primaryChannelUrl",
                flags={"read_only": True},
            )
            team_information.team_creation_time_utc = AAZStrType(
                serialized_name="teamCreationTimeUtc",
                flags={"read_only": True},
            )
            team_information.team_id = AAZStrType(
                serialized_name="teamId",
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            return cls._schema_on_200


__all__ = ["List"]
