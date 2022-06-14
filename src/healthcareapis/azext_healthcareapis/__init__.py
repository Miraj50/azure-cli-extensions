# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=unused-import

import azext_healthcareapis._help
from azure.cli.core import AzCommandsLoader


class HealthcareApisManagementClientCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_healthcareapis.generated._client_factory import cf_healthcareapis_cl
        healthcareapis_custom = CliCommandType(
            operations_tmpl='azext_healthcareapis.custom#{}',
            client_factory=cf_healthcareapis_cl)
        parent = super(HealthcareApisManagementClientCommandsLoader, self)
        parent.__init__(cli_ctx=cli_ctx, custom_command_type=healthcareapis_custom)

    def load_command_table(self, args):
        from azext_healthcareapis.generated.commands import load_command_table
        load_command_table(self, args)
        try:
            from azext_healthcareapis.manual.commands import load_command_table as load_command_table_manual
            load_command_table_manual(self, args)
        except ImportError as e:
            if e.name.endswith('manual.commands'):
                pass
            else:
                raise e
        return self.command_table

    def load_arguments(self, command):
        from azext_healthcareapis.generated._params import load_arguments
        load_arguments(self, command)
        try:
            from azext_healthcareapis.manual._params import load_arguments as load_arguments_manual
            load_arguments_manual(self, command)
        except ImportError as e:
            if e.name.endswith('manual._params'):
                pass
            else:
                raise e


COMMAND_LOADER_CLS = HealthcareApisManagementClientCommandsLoader
