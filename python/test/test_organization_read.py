# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.86
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.organization_read import OrganizationRead  # noqa: E501

class TestOrganizationRead(unittest.TestCase):
    """OrganizationRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationRead:
        """Test OrganizationRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationRead`
        """
        model = OrganizationRead()  # noqa: E501
        if include_optional:
            return OrganizationRead(
                name = '',
                website_url = '',
                custom_base_url = '',
                icon = tpdk.models.media_read.Media-Read(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                logo = tpdk.models.media_read.Media-Read(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                primary_color = '',
                secondary_color = '',
                accent_color = '',
                error_color = '',
                info_color = '',
                success_color = '',
                warning_color = '',
                direct_notification_toggle = True,
                persona_auth_portal_toggle = True,
                flat_rate_enabled = True,
                rate_commission_safe_checkout = 1.337
            )
        else:
            return OrganizationRead(
                direct_notification_toggle = True,
                persona_auth_portal_toggle = True,
                rate_commission_safe_checkout = 1.337,
        )
        """

    def testOrganizationRead(self):
        """Test OrganizationRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
