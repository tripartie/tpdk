# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.39
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.offer_read import OfferRead  # noqa: E501
from tpdk.rest import ApiException

class TestOfferRead(unittest.TestCase):
    """OfferRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferRead`
        """
        model = tpdk.models.offer_read.OfferRead()  # noqa: E501
        if include_optional :
            return OfferRead(
                ulid = '', 
                public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                organization = None, 
                seller = '', 
                nature = 'physical_item', 
                title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 
                unit_price = 125.54, 
                currency_code = 'EUR', 
                item_count = 1, 
                condition = 'USED', 
                medias = [
                    tpdk.models.media_read.Media-Read(
                        public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', )
                    ]
            )
        else :
            return OfferRead(
                ulid = '',
                seller = '',
                nature = 'physical_item',
                medias = [
                    tpdk.models.media_read.Media-Read(
                        public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', )
                    ],
        )
        """

    def testOfferRead(self):
        """Test OfferRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
