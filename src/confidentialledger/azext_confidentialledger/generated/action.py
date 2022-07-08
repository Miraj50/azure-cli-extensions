# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# pylint: disable=protected-access

# pylint: disable=no-self-use


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddAadBasedSecurityPrincipals(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAadBasedSecurityPrincipals, self).__call__(
            parser, namespace, action, option_string
        )

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split("=", 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError("usage error: {} [KEY=VALUE ...]".format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == "principal-id":
                d["principal_id"] = v[0]

            elif kl == "tenant-id":
                d["tenant_id"] = v[0]

            elif kl == "ledger-role-name":
                d["ledger_role_name"] = v[0]

            else:
                raise CLIError(
                    "Unsupported Key {} is provided for parameter aad-based-security-principals. All possible keys are: principal-id, tenant-id, ledger-role-name".format(
                        k
                    )
                )

        return d


class AddCertBasedSecurityPrincipals(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCertBasedSecurityPrincipals, self).__call__(
            parser, namespace, action, option_string
        )

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split("=", 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError("usage error: {} [KEY=VALUE ...]".format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == "cert":
                d["cert"] = v[0]

            elif kl == "ledger-role-name":
                d["ledger_role_name"] = v[0]

            else:
                raise CLIError(
                    "Unsupported Key {} is provided for parameter cert-based-security-principals. All possible keys are: cert, ledger-role-name".format(
                        k
                    )
                )

        return d
