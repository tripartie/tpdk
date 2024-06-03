# coding: utf-8

"""
    Resolution Center

    Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution.

    The version of the OpenAPI document: 2.0.208
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.models.user_email_validation_write import UserEmailValidationWrite

class TestUserEmailValidationWrite(unittest.TestCase):
    """UserEmailValidationWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserEmailValidationWrite:
        """Test UserEmailValidationWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserEmailValidationWrite`
        """
        model = UserEmailValidationWrite()
        if include_optional:
            return UserEmailValidationWrite(
                captcha = '',
                plain_password = 'secr$t',
                email_verification_input = '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127'
            )
        else:
            return UserEmailValidationWrite(
                captcha = '',
                email_verification_input = '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100101102103104105106107108109110111112113114115116117118119120121122123124125126127',
        )
        """

    def testUserEmailValidationWrite(self):
        """Test UserEmailValidationWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
