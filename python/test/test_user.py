# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.52
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.user import User  # noqa: E501
from tpdk.rest import ApiException

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `User`
        """
        model = tpdk.models.user.User()  # noqa: E501
        if include_optional :
            return User(
                id = '', 
                captcha = '', 
                first_name = 'Jacob', 
                last_name = 'TAHRI', 
                public_name = 'Nickname', 
                role_in_company = 'Accounting Dpt', 
                birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                email = 'john.doe@company.tld', 
                roles = ["ROLE_ORGANIZATION_OWNER"], 
                password = '', 
                plain_password = 'secr$t', 
                intl_phone_number = '+33700000000', 
                origin_country = 'FRA', 
                preferred_language = 'fr', 
                last_successful_log_in = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                email_verification_code = '', 
                email_verification_input = '', 
                phone_verification_code = '', 
                phone_verification_input = '', 
                avatar = '', 
                notifications = [
                    ''
                    ], 
                medias = [
                    ''
                    ], 
                views = [
                    tpdk.models.view.View(
                        id = 56, 
                        ip_address = '', 
                        offer = '', 
                        dispute = '', 
                        persona = '', 
                        user = '', 
                        hit_count = 1, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                consent_mail_notification = True, 
                consent_mail_ads = True, 
                keys = [
                    ''
                    ], 
                organization = '', 
                username = '', 
                salt = '', 
                user_identifier = ''
            )
        else :
            return User(
                birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                roles = ["ROLE_ORGANIZATION_OWNER"],
                password = '',
                views = [
                    tpdk.models.view.View(
                        id = 56, 
                        ip_address = '', 
                        offer = '', 
                        dispute = '', 
                        persona = '', 
                        user = '', 
                        hit_count = 1, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                consent_mail_notification = True,
                consent_mail_ads = True,
                keys = [
                    ''
                    ],
        )
        """

    def testUser(self):
        """Test User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
