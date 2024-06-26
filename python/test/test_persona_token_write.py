# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.204
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.models.persona_token_write import PersonaTokenWrite

class TestPersonaTokenWrite(unittest.TestCase):
    """PersonaTokenWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonaTokenWrite:
        """Test PersonaTokenWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaTokenWrite`
        """
        model = PersonaTokenWrite()
        if include_optional:
            return PersonaTokenWrite(
                target_url = 'https://next.tripartie.app/?d=01ARZ3NDEKTSV4RRFFQ69G5FAV'
            )
        else:
            return PersonaTokenWrite(
                target_url = 'https://next.tripartie.app/?d=01ARZ3NDEKTSV4RRFFQ69G5FAV',
        )
        """

    def testPersonaTokenWrite(self):
        """Test PersonaTokenWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
