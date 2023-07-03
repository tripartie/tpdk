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
from tpdk.models.persona_read import PersonaRead  # noqa: E501
from tpdk.rest import ApiException

class TestPersonaRead(unittest.TestCase):
    """PersonaRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PersonaRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaRead`
        """
        model = tpdk.models.persona_read.PersonaRead()  # noqa: E501
        if include_optional :
            return PersonaRead(
                id = 56, 
                first_name = 'John', 
                last_name = 'Doe', 
                gender = 'RATHER_NOT_SAY', 
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                language = 'fr', 
                email = 'john.doe@gmail.com', 
                mobile_phone_number = '+33745214529', 
                address = None, 
                risk_level = 'WEAK', 
                risk_score = 24, 
                external_purchase_count = 56, 
                external_sell_count = 56, 
                metadata = [
                    tpdk.models.metadata_read.Metadata-Read(
                        key = 'External-ID', 
                        value = '54412', )
                    ], 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                offer_count = 4, 
                purchase_count = 42
            )
        else :
            return PersonaRead(
        )
        """

    def testPersonaRead(self):
        """Test PersonaRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
