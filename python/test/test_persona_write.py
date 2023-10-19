# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.92
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.persona_write import PersonaWrite  # noqa: E501

class TestPersonaWrite(unittest.TestCase):
    """PersonaWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonaWrite:
        """Test PersonaWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaWrite`
        """
        model = PersonaWrite()  # noqa: E501
        if include_optional:
            return PersonaWrite(
                first_name = 'John',
                last_name = 'Doe',
                gender = 'RATHER_NOT_SAY',
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                language = 'fr',
                email = 'john.doe@gmail.com',
                mobile_phone_number = '+33745214529',
                address = tpdk.models.address_write.Address-Write(
                    company_name = 'Company Tld', 
                    country_code = 'FRA', 
                    zip_code = '75004', 
                    city_name = 'Paris', 
                    first_line = '118 avenue des champs élysées', 
                    second_line = 'Apt 6E', 
                    building_name = 'Electron', 
                    building_floor = 'Third floor', 
                    gate_or_portal_or_inbox_code = '3124', ),
                external_purchase_count = 0,
                external_sell_count = 0,
                metadata = [
                    tpdk.models.metadata_write.Metadata-Write(
                        key = 'External-ID', 
                        value = '54412', )
                    ]
            )
        else:
            return PersonaWrite(
                first_name = 'John',
                last_name = 'Doe',
                gender = 'RATHER_NOT_SAY',
        )
        """

    def testPersonaWrite(self):
        """Test PersonaWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
