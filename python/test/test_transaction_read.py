# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.7
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.transaction_read import TransactionRead  # noqa: E501
from tpdk.rest import ApiException

class TestTransactionRead(unittest.TestCase):
    """TransactionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TransactionRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRead`
        """
        model = tpdk.models.transaction_read.TransactionRead()  # noqa: E501
        if include_optional :
            return TransactionRead(
                ulid = '', 
                offer = tpdk.models.offer_read.Offer-Read(
                    ulid = '', 
                    public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                    nature = 'physical_item', 
                    title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                    description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 
                    unit_price = 125.54, 
                    currency_code = 'EUR', 
                    item_count = 1, 
                    condition = 'USED', ), 
                buyer = '', 
                fees = 1.337, 
                metadata = [
                    tpdk.models.metadata_read.Metadata-Read(
                        key = 'External-ID', 
                        value = '54412', )
                    ], 
                parcels = [
                    tpdk.models.parcel_read.Parcel-Read(
                        carrier = 'SwissPost', 
                        identifier = '8J001271466474', 
                        price = 4.88, 
                        currency = 'EUR', 
                        status = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return TransactionRead(
                ulid = '',
                metadata = [
                    tpdk.models.metadata_read.Metadata-Read(
                        key = 'External-ID', 
                        value = '54412', )
                    ],
                parcels = [
                    tpdk.models.parcel_read.Parcel-Read(
                        carrier = 'SwissPost', 
                        identifier = '8J001271466474', 
                        price = 4.88, 
                        currency = 'EUR', 
                        status = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testTransactionRead(self):
        """Test TransactionRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
