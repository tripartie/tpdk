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

from tpdk.models.user_collection_read import UserCollectionRead  # noqa: E501

class TestUserCollectionRead(unittest.TestCase):
    """UserCollectionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserCollectionRead:
        """Test UserCollectionRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCollectionRead`
        """
        model = UserCollectionRead()  # noqa: E501
        if include_optional:
            return UserCollectionRead(
                id = '',
                first_name = 'Jacob',
                last_name = 'TAHRI',
                public_name = 'Nickname',
                role_in_company = 'Accounting Dpt',
                email = 'john.doe@company.tld',
                roles = ["ROLE_ORGANIZATION_OWNER"],
                intl_phone_number = '+33700000000',
                last_successful_log_in = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                avatar = tpdk.models.media_collection_read.Media-CollectionRead(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                organization = tpdk.models.organization_collection_read.Organization-CollectionRead(
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
                    rate_commission_safe_checkout = 1.337, )
            )
        else:
            return UserCollectionRead(
                roles = ["ROLE_ORGANIZATION_OWNER"],
        )
        """

    def testUserCollectionRead(self):
        """Test UserCollectionRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
