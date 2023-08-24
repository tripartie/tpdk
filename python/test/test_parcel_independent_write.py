# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.52
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.parcel_independent_write import ParcelIndependentWrite  # noqa: E501
from tpdk.rest import ApiException

class TestParcelIndependentWrite(unittest.TestCase):
    """ParcelIndependentWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelIndependentWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParcelIndependentWrite`
        """
        model = tpdk.models.parcel_independent_write.ParcelIndependentWrite()  # noqa: E501
        if include_optional :
            return ParcelIndependentWrite(
                carrier = 'SwissPost', 
                identifier = '8J001271466474', 
                price = 4.88, 
                currency = 'EUR'
            )
        else :
            return ParcelIndependentWrite(
                carrier = 'SwissPost',
                identifier = '8J001271466474',
        )
        """

    def testParcelIndependentWrite(self):
        """Test ParcelIndependentWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
