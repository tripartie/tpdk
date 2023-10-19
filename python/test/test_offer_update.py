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

from tpdk.models.offer_update import OfferUpdate  # noqa: E501

class TestOfferUpdate(unittest.TestCase):
    """OfferUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OfferUpdate:
        """Test OfferUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferUpdate`
        """
        model = OfferUpdate()  # noqa: E501
        if include_optional:
            return OfferUpdate(
                public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold',
                enforce_persona_auth = True,
                override_rate_commission_safe_checkout = 1.337,
                redirect_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold?checkout=true',
                title = 'ASUS TUF X570-PLUS GAMING Motherboard',
                description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                unit_price = 125.54,
                currency_code = 'EUR',
                item_count = 1,
                weight_in_gram = 56,
                shipping_allowed = True,
                hand_delivery_allowed = True,
                shipping_carriers = [
                    'SwissPost'
                    ],
                ean_code = '4718017388450',
                can_be_sold_separately = True,
                metadata = [
                    tpdk.models.metadata_update.Metadata-Update(
                        key = 'External-ID', 
                        value = '54412', )
                    ]
            )
        else:
            return OfferUpdate(
        )
        """

    def testOfferUpdate(self):
        """Test OfferUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
