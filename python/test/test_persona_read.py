# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.139
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.persona_read import PersonaRead

class TestPersonaRead(unittest.TestCase):
    """PersonaRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonaRead:
        """Test PersonaRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaRead`
        """
        model = PersonaRead()
        if include_optional:
            return PersonaRead(
                id = 56,
                first_name = 'John',
                last_name = 'Doe',
                language = 'fr',
                email = 'john.doe@gmail.com',
                mobile_phone_number = '+33745214529'
            )
        else:
            return PersonaRead(
        )
        """

    def testPersonaRead(self):
        """Test PersonaRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
