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

from tpdk.models.persona_register import PersonaRegister

class TestPersonaRegister(unittest.TestCase):
    """PersonaRegister unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonaRegister:
        """Test PersonaRegister
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaRegister`
        """
        model = PersonaRegister()
        if include_optional:
            return PersonaRegister(
                captcha = '',
                plain_password = 'secr$t',
                first_name = 'John',
                last_name = 'Doe',
                gender = 'RATHER_NOT_SAY',
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                language = 'fr',
                email = 'john.doe@gmail.com',
                mobile_phone_number = '+33745214529'
            )
        else:
            return PersonaRegister(
                first_name = 'John',
                last_name = 'Doe',
                gender = 'RATHER_NOT_SAY',
        )
        """

    def testPersonaRegister(self):
        """Test PersonaRegister"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
