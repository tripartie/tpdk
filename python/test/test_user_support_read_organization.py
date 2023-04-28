# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0.b1
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.user_support_read_organization import UserSupportReadOrganization  # noqa: E501
from tpdk.rest import ApiException

class TestUserSupportReadOrganization(unittest.TestCase):
    """UserSupportReadOrganization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserSupportReadOrganization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserSupportReadOrganization`
        """
        model = tpdk.models.user_support_read_organization.UserSupportReadOrganization()  # noqa: E501
        if include_optional :
            return UserSupportReadOrganization(
                id = 56, 
                name = ''
            )
        else :
            return UserSupportReadOrganization(
        )
        """

    def testUserSupportReadOrganization(self):
        """Test UserSupportReadOrganization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
