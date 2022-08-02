# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from .example_steps import step_create
from .example_steps import step_show
from .example_steps import step_list
from .example_steps import step_list2
from .example_steps import step_update
from .example_steps import step_link_notification_hub
from .example_steps import step_list_key
from .example_steps import step_regenerate_key
from .example_steps import step_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg_2, rg):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg_2, rg):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg_2, rg):
    setup_scenario(test, rg_2, rg)
    step_create(test, rg_2, rg, checks=[
        test.check("name", "{myCommunicationService}", case_sensitive=False),
        test.check("location", "Global", case_sensitive=False),
        test.check("dataLocation", "United States", case_sensitive=False),
    ])
    step_show(test, rg_2, rg, checks=[
        test.check("name", "{myCommunicationService}", case_sensitive=False),
        test.check("location", "Global", case_sensitive=False),
        test.check("dataLocation", "United States", case_sensitive=False),
    ])
    step_list(test, rg_2, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_update(test, rg_2, rg, checks=[
        test.check("name", "{myCommunicationService}", case_sensitive=False),
        test.check("location", "Global", case_sensitive=False),
        test.check("dataLocation", "United States", case_sensitive=False),
        test.check("tags.newTag", "newVal", case_sensitive=False),
    ])
    step_link_notification_hub(test, rg_2, rg, checks=[])
    step_list_key(test, rg_2, rg, checks=[])
    step_regenerate_key(test, rg_2, rg, checks=[])
    step_delete(test, rg_2, rg, checks=[])
    cleanup_scenario(test, rg_2, rg)


# Test class for Scenario
@try_manual
class CommunicationScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(CommunicationScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myCommunicationService': self.create_random_name(prefix='MyCommunicationResource'[:11], length=23),
        })


    @AllowLargeResponse()
    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyOtherResourceGroup'[:7], key='rg_2',
                           parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestcommunication_MyResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_communication_Scenario(self, rg_2, rg):
        call_scenario(self, rg_2, rg)
        calc_coverage(__file__)
        raise_if()

