# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0-b2
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.offer_independent_write_seller import OfferIndependentWriteSeller  # noqa: E501
from tpdk.rest import ApiException

class TestOfferIndependentWriteSeller(unittest.TestCase):
    """OfferIndependentWriteSeller unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferIndependentWriteSeller
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferIndependentWriteSeller`
        """
        model = tpdk.models.offer_independent_write_seller.OfferIndependentWriteSeller()  # noqa: E501
        if include_optional :
            return OfferIndependentWriteSeller(
                first_name = 'John', 
                last_name = 'Doe', 
                gender = 'RATHER_NOT_SAY', 
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                language = 'FR', 
                email = 'john.doe@gmail.com', 
                mobile_phone_number = '+33700000000', 
                address = None, 
                external_purchase_count = 56, 
                external_sell_count = 56, 
                metadata = [
                    tpdk.models.metadata_independent_write.Metadata-IndependentWrite(
                        key = 'External-ID', 
                        value = '54412', )
                    ]
            )
        else :
            return OfferIndependentWriteSeller(
                metadata = [
                    tpdk.models.metadata_independent_write.Metadata-IndependentWrite(
                        key = 'External-ID', 
                        value = '54412', )
                    ],
        )
        """

    def testOfferIndependentWriteSeller(self):
        """Test OfferIndependentWriteSeller"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
