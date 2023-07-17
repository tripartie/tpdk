# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.26
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.organization_update import OrganizationUpdate  # noqa: E501
from tpdk.rest import ApiException

class TestOrganizationUpdate(unittest.TestCase):
    """OrganizationUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrganizationUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationUpdate`
        """
        model = tpdk.models.organization_update.OrganizationUpdate()  # noqa: E501
        if include_optional :
            return OrganizationUpdate(
                name = '', 
                vat_number = '', 
                commercial_registry_number = '', 
                webhook_url = '', 
                website_url = '', 
                custom_base_url = '', 
                billing_address = None, 
                primary_color = '', 
                secondary_color = '', 
                accent_color = '', 
                error_color = '', 
                info_color = '', 
                success_color = '', 
                warning_color = '', 
                direct_notification_toggle = True, 
                anonymity_level = 'PARTIAL_FIRST_NAME', 
                flat_rate_enabled = True, 
                rate_commission_safe_checkout = 1.337
            )
        else :
            return OrganizationUpdate(
                name = '',
                vat_number = '',
                commercial_registry_number = '',
        )
        """

    def testOrganizationUpdate(self):
        """Test OrganizationUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
