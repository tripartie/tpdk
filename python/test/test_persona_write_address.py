# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.13
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.persona_write_address import PersonaWriteAddress  # noqa: E501
from tpdk.rest import ApiException

class TestPersonaWriteAddress(unittest.TestCase):
    """PersonaWriteAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PersonaWriteAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaWriteAddress`
        """
        model = tpdk.models.persona_write_address.PersonaWriteAddress()  # noqa: E501
        if include_optional :
            return PersonaWriteAddress(
                company_name = 'Company Tld', 
                country_code = 'FRA', 
                zip_code = '75004', 
                city_name = 'Paris', 
                first_line = '118 avenue des champs élysées', 
                second_line = 'Apt 6E', 
                building_name = 'Electron', 
                building_floor = 'Third floor', 
                gate_or_portal_or_inbox_code = '3124'
            )
        else :
            return PersonaWriteAddress(
        )
        """

    def testPersonaWriteAddress(self):
        """Test PersonaWriteAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
