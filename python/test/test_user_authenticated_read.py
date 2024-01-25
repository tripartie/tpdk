# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.161
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.user_authenticated_read import UserAuthenticatedRead

class TestUserAuthenticatedRead(unittest.TestCase):
    """UserAuthenticatedRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserAuthenticatedRead:
        """Test UserAuthenticatedRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserAuthenticatedRead`
        """
        model = UserAuthenticatedRead()
        if include_optional:
            return UserAuthenticatedRead(
                id = 'https://example.com/',
                first_name = 'Jacob',
                last_name = 'TAHRI',
                public_name = 'Nickname',
                role_in_company = 'Accounting Dpt',
                birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email = 'john.doe@company.tld',
                roles = [ROLE_ORGANIZATION_OWNER],
                totp_enabled = True,
                intl_phone_number = '+33700000000',
                origin_country = 'FRA',
                preferred_language = 'fr',
                last_successful_log_in = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                avatar = tpdk.models.media_read.Media-Read(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                consent_mail_notification = True,
                consent_mail_ads = True,
                organization = tpdk.models.organization_authenticated_read.Organization-AuthenticatedRead(
                    id = 56, 
                    name = '', 
                    domain_verified = True, 
                    icon = tpdk.models.media_read.Media-Read(
                        public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ), 
                    logo = tpdk.models.media_read.Media-Read(
                        public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ), 
                    safe_checkout_toggle = True, 
                    resolution_center_toggle = True, 
                    internal_messaging_toggle = True, 
                    persona_auth_portal_toggle = True, 
                    automated_return_toggle = True, 
                    flat_rate_enabled = True, 
                    rate_commission_safe_checkout = 1.337, )
            )
        else:
            return UserAuthenticatedRead(
                roles = [ROLE_ORGANIZATION_OWNER],
                consent_mail_notification = True,
                consent_mail_ads = True,
        )
        """

    def testUserAuthenticatedRead(self):
        """Test UserAuthenticatedRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
