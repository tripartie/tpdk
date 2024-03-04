# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.179
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.models.user_totp_setup_read import UserTotpSetupRead

class TestUserTotpSetupRead(unittest.TestCase):
    """UserTotpSetupRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserTotpSetupRead:
        """Test UserTotpSetupRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserTotpSetupRead`
        """
        model = UserTotpSetupRead()
        if include_optional:
            return UserTotpSetupRead(
                totp_uri = ''
            )
        else:
            return UserTotpSetupRead(
        )
        """

    def testUserTotpSetupRead(self):
        """Test UserTotpSetupRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
