# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.134
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.offer import Offer

class TestOffer(unittest.TestCase):
    """Offer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Offer:
        """Test Offer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Offer`
        """
        model = Offer()
        if include_optional:
            return Offer(
                id = 56,
                ulid = '',
                public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold',
                enforce_persona_auth = True,
                override_rate_commission_safe_checkout = 1.337,
                redirect_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold?checkout=true',
                url = 'https://next.tripartie.app/?c=01ARZ3NDEKTSV4RRFFQ69G5FAV',
                organization = '',
                seller = '',
                nature = 'physical_item',
                title = 'ASUS TUF X570-PLUS GAMING Motherboard',
                description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                unit_price = 125.54,
                currency_code = 'EUR',
                item_count = 1,
                condition = 'USED',
                weight_in_gram = 56,
                shipping_allowed = True,
                hand_delivery_allowed = True,
                shipping_carriers = [
                    'SwissPost'
                    ],
                ean_code = '4718017388450',
                can_be_sold_separately = True,
                metadata = [
                    tpdk.models.metadata.Metadata(
                        id = 56, 
                        persona = '', 
                        dispute = '', 
                        offer = '', 
                        transaction = '', 
                        key = 'External-ID', 
                        value = '54412', )
                    ],
                medias = [
                    ''
                    ],
                views = [
                    tpdk.models.view.View(
                        id = 56, 
                        ip_address = '', 
                        offer = '', 
                        dispute = '', 
                        persona = '', 
                        user = '', 
                        hit_count = 1, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        named_source = 'BUYER', )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                iri = '',
                half_price_point = 1.337
            )
        else:
            return Offer(
                ulid = '',
                enforce_persona_auth = True,
                url = 'https://next.tripartie.app/?c=01ARZ3NDEKTSV4RRFFQ69G5FAV',
                seller = '',
                nature = 'physical_item',
                shipping_allowed = True,
                hand_delivery_allowed = True,
                can_be_sold_separately = True,
                medias = [
                    ''
                    ],
                views = [
                    tpdk.models.view.View(
                        id = 56, 
                        ip_address = '', 
                        offer = '', 
                        dispute = '', 
                        persona = '', 
                        user = '', 
                        hit_count = 1, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        named_source = 'BUYER', )
                    ],
        )
        """

    def testOffer(self):
        """Test Offer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
