# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.22
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.dispute_collection_read import DisputeCollectionRead  # noqa: E501
from tpdk.rest import ApiException

class TestDisputeCollectionRead(unittest.TestCase):
    """DisputeCollectionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DisputeCollectionRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputeCollectionRead`
        """
        model = tpdk.models.dispute_collection_read.DisputeCollectionRead()  # noqa: E501
        if include_optional :
            return DisputeCollectionRead(
                ulid = '01ARZ3NDEKTSV4RRFFQ69G5FAV', 
                transaction = tpdk.models.transaction_collection_read.Transaction-CollectionRead(
                    ulid = '', 
                    offer = tpdk.models.offer_collection_read.Offer-CollectionRead(
                        ulid = '', 
                        public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                        title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                        unit_price = 125.54, 
                        currency_code = 'EUR', 
                        item_count = 1, 
                        condition = 'USED', ), ), 
                status = 'CREATED', 
                item_count = 1, 
                issue_type = 'NOT_AS_DESCRIBED', 
                issue_in_description_type = 'WRONG_COLOUR', 
                complainant_stake = 'LOW', 
                inferred_stake = 'LOW', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                iri = '', 
                message_count = 6
            )
        else :
            return DisputeCollectionRead(
                ulid = '01ARZ3NDEKTSV4RRFFQ69G5FAV',
                status = 'CREATED',
        )
        """

    def testDisputeCollectionRead(self):
        """Test DisputeCollectionRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
