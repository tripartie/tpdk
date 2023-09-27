# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.75
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.dispute_collection_read import DisputeCollectionRead  # noqa: E501

class TestDisputeCollectionRead(unittest.TestCase):
    """DisputeCollectionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisputeCollectionRead:
        """Test DisputeCollectionRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputeCollectionRead`
        """
        model = DisputeCollectionRead()  # noqa: E501
        if include_optional:
            return DisputeCollectionRead(
                ulid = '01ARZ3NDEKTSV4RRFFQ69G5FAV',
                transaction = tpdk.models.transaction_collection_read.Transaction-CollectionRead(
                    ulid = '', 
                    offer = tpdk.models.offer_collection_read.Offer-CollectionRead(
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
                        condition = 'USED', ), 
                    buyer = tpdk.models.persona_collection_read.Persona-CollectionRead(
                        id = 56, 
                        first_name = 'John', 
                        last_name = 'Doe', ), ),
                status = 'CREATED',
                item_count = 1,
                issue_type = 'NOT_AS_DESCRIBED',
                issue_in_description_type = 'WRONG_COLOUR',
                issue_mentioned_in_offer = True,
                complainant_stake = 'LOW',
                inferred_stake = 'LOW',
                chosen_solution = 'PARTIAL_REFUND_WITH_PARTIAL_RETURN',
                chosen_partial_refund_amount = 40,
                platform_solution = 'PARTIAL_REFUND_WITH_PARTIAL_RETURN',
                platform_partial_refund_amount = 0,
                platform_approval = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status_expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                awaited_party = 'BUYER',
                iri = '',
                message_count = 6
            )
        else:
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
