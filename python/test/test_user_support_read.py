# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.20
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.user_support_read import UserSupportRead  # noqa: E501
from tpdk.rest import ApiException

class TestUserSupportRead(unittest.TestCase):
    """UserSupportRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserSupportRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSupportRead`
        """
        model = tpdk.models.user_support_read.UserSupportRead()  # noqa: E501
        if include_optional :
            return UserSupportRead(
                id = '', 
                first_name = 'Jacob', 
                last_name = 'TAHRI', 
                public_name = 'Nickname', 
                role_in_company = 'Accounting Dpt', 
                email = '', 
                intl_phone_number = '+33700000000', 
                last_successful_log_in = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                avatar = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                organization = None
            )
        else :
            return UserSupportRead(
        )
        """

    def testUserSupportRead(self):
        """Test UserSupportRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
