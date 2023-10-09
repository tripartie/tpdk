# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.86
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.persona import Persona  # noqa: E501

class TestPersona(unittest.TestCase):
    """Persona unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Persona:
        """Test Persona
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Persona`
        """
        model = Persona()  # noqa: E501
        if include_optional:
            return Persona(
                id = 56,
                captcha = '',
                organization = '',
                target_url = 'https://next.tripartie.app/?d=01ARZ3NDEKTSV4RRFFQ69G5FAV',
                auth_url = 'https://next.tripartie.app/?d=01ARZ3NDEKTSV4RRFFQ69G5FAV&t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIzNDU2Nzg5LCJuYW1lIjoiSm9zZXBoIn0.OpOSSw7e485LOP5PrzScxHb7SR6sAOMRckfFwi4rp7o',
                expire_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                password = '',
                plain_password = 'secr$t',
                first_name = 'John',
                last_name = 'Doe',
                gender = 'RATHER_NOT_SAY',
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                language = 'fr',
                email = 'john.doe@gmail.com',
                mobile_phone_number = '+33745214529',
                address = tpdk.models.address.Address(
                    id = 56, 
                    company_name = 'Company Tld', 
                    country_code = 'FRA', 
                    zip_code = '75004', 
                    city_name = 'Paris', 
                    first_line = '118 avenue des champs élysées', 
                    second_line = 'Apt 6E', 
                    building_name = 'Electron', 
                    building_floor = 'Third floor', 
                    gate_or_portal_or_inbox_code = '3124', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                risk_level = 'WEAK',
                risk_score = 24,
                external_purchase_count = 56,
                external_sell_count = 56,
                metadata = [
                    tpdk.models.metadata.Metadata(
                        id = 56, 
                        persona = '', 
                        dispute = '', 
                        offer = '', 
                        transaction = '', 
                        key = 'External-ID', 
                        value = '54412', )
                    ],
                offers = [
                    ''
                    ],
                purchases = [
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
                offer_count = 4,
                purchase_count = 42,
                roles = [
                    ''
                    ],
                user_identifier = ''
            )
        else:
            return Persona(
                offers = [
                    ''
                    ],
                purchases = [
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
        )
        """

    def testPersona(self):
        """Test Persona"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
