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
from tpdk.models.organization_authenticated_read import OrganizationAuthenticatedRead  # noqa: E501
from tpdk.rest import ApiException

class TestOrganizationAuthenticatedRead(unittest.TestCase):
    """OrganizationAuthenticatedRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrganizationAuthenticatedRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationAuthenticatedRead`
        """
        model = tpdk.models.organization_authenticated_read.OrganizationAuthenticatedRead()  # noqa: E501
        if include_optional :
            return OrganizationAuthenticatedRead(
                id = 56, 
                name = '', 
                domain_verified = True, 
                icon = None, 
                logo = None, 
                safe_checkout_toggle = True, 
                resolution_center_toggle = True, 
                internal_messaging_toggle = True, 
                persona_auth_portal_toggle = True, 
                automated_return_toggle = True, 
                flat_rate_enabled = True, 
                rate_commission_safe_checkout = 1.337
            )
        else :
            return OrganizationAuthenticatedRead(
                domain_verified = True,
                safe_checkout_toggle = True,
                resolution_center_toggle = True,
                internal_messaging_toggle = True,
                persona_auth_portal_toggle = True,
                automated_return_toggle = True,
                rate_commission_safe_checkout = 1.337,
        )
        """

    def testOrganizationAuthenticatedRead(self):
        """Test OrganizationAuthenticatedRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
