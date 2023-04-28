# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0-b1
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.address_independent_write import AddressIndependentWrite  # noqa: E501
from tpdk.rest import ApiException

class TestAddressIndependentWrite(unittest.TestCase):
    """AddressIndependentWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddressIndependentWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddressIndependentWrite`
        """
        model = tpdk.models.address_independent_write.AddressIndependentWrite()  # noqa: E501
        if include_optional :
            return AddressIndependentWrite(
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
            return AddressIndependentWrite(
        )
        """

    def testAddressIndependentWrite(self):
        """Test AddressIndependentWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
