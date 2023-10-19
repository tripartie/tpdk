# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.92
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.organization_collection_read import OrganizationCollectionRead  # noqa: E501

class TestOrganizationCollectionRead(unittest.TestCase):
    """OrganizationCollectionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationCollectionRead:
        """Test OrganizationCollectionRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationCollectionRead`
        """
        model = OrganizationCollectionRead()  # noqa: E501
        if include_optional:
            return OrganizationCollectionRead(
                id = 56,
                name = '',
                vat_number = '',
                commercial_registry_number = '',
                website_url = '',
                icon = tpdk.models.media_collection_read.Media-CollectionRead(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                logo = tpdk.models.media_collection_read.Media-CollectionRead(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                direct_notification_toggle = True,
                safe_checkout_toggle = True,
                resolution_center_toggle = True,
                internal_messaging_toggle = True,
                persona_auth_portal_toggle = True,
                automated_return_toggle = True,
                flat_rate_enabled = True,
                rate_commission_safe_checkout = 1.337
            )
        else:
            return OrganizationCollectionRead(
                direct_notification_toggle = True,
                safe_checkout_toggle = True,
                resolution_center_toggle = True,
                internal_messaging_toggle = True,
                persona_auth_portal_toggle = True,
                automated_return_toggle = True,
                rate_commission_safe_checkout = 1.337,
        )
        """

    def testOrganizationCollectionRead(self):
        """Test OrganizationCollectionRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
