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

from tpdk.models.offer_collection_read import OfferCollectionRead  # noqa: E501

class TestOfferCollectionRead(unittest.TestCase):
    """OfferCollectionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OfferCollectionRead:
        """Test OfferCollectionRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferCollectionRead`
        """
        model = OfferCollectionRead()  # noqa: E501
        if include_optional:
            return OfferCollectionRead(
                ulid = '',
                public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold',
                seller = tpdk.models.persona_collection_read.Persona-CollectionRead(
                    id = 56, 
                    first_name = 'John', 
                    last_name = 'Doe', ),
                title = 'ASUS TUF X570-PLUS GAMING Motherboard',
                unit_price = 125.54,
                currency_code = 'EUR',
                item_count = 1,
                condition = 'USED'
            )
        else:
            return OfferCollectionRead(
                ulid = '',
                seller = tpdk.models.persona_collection_read.Persona-CollectionRead(
                    id = 56, 
                    first_name = 'John', 
                    last_name = 'Doe', ),
        )
        """

    def testOfferCollectionRead(self):
        """Test OfferCollectionRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
