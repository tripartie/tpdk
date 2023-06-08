# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.13
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.webhook_object import WebhookObject  # noqa: E501
from tpdk.rest import ApiException

class TestWebhookObject(unittest.TestCase):
    """WebhookObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WebhookObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookObject`
        """
        model = tpdk.models.webhook_object.WebhookObject()  # noqa: E501
        if include_optional :
            return WebhookObject(
                ulid = '', 
                transaction = tpdk.models.transaction_read.Transaction-Read(
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
                        ], ), 
                status = 'CREATED', 
                item_count = 1, 
                issue_type = 'NOT_AS_DESCRIBED', 
                issue_in_description_type = 'WRONG_COLOUR', 
                issue_details = 'The item received have multiple impacts on the left side, this was not mentioned and I feel a bit sad. Although it is usable as-is, I expected it without flaws.', 
                complainant_truthfulness_score = 100, 
                seller_truthfulness_score = 100, 
                complainant_stake = 'LOW', 
                inferred_stake = 'LOW', 
                recommended_solution = 'PARTIAL_REFUND_WITH_PARTIAL_RETURN', 
                recommended_partial_refund_amount = 35, 
                chosen_solution = 'PARTIAL_REFUND_WITH_PARTIAL_RETURN', 
                chosen_partial_refund_amount = 40, 
                counter_solution = 'PARTIAL_REFUND_WITH_PARTIAL_RETURN', 
                counter_partial_refund_amount = 30, 
                complainant_approval = True, 
                seller_approval = True, 
                platform_solution = 'PARTIAL_REFUND_WITH_PARTIAL_RETURN', 
                platform_partial_refund_amount = 0, 
                platform_approval = True, 
                arbitration_by = '', 
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
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                iri = '', 
                message_count = 6, 
                id = 56, 
                first_name = 'John', 
                last_name = 'Doe', 
                gender = 'RATHER_NOT_SAY', 
                date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                language = 'fr', 
                email = 'john.doe@gmail.com', 
                mobile_phone_number = '+33745214529', 
                address = None, 
                risk_level = 'WEAK', 
                risk_score = 24, 
                external_purchase_count = 56, 
                external_sell_count = 56, 
                metadata = [
                    tpdk.models.metadata_read.Metadata-Read(
                        key = 'External-ID', 
                        value = '54412', )
                    ], 
                offer_count = 4, 
                purchase_count = 42, 
                public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                nature = 'physical_item', 
                title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 
                unit_price = 125.54, 
                currency_code = 'EUR', 
                condition = 'USED'
            )
        else :
            return WebhookObject(
                ulid = '',
                status = 'CREATED',
                item_count = 1,
                issue_type = 'NOT_AS_DESCRIBED',
                complainant_truthfulness_score = 100,
                seller_truthfulness_score = 100,
                complainant_stake = 'LOW',
                seller_approval = True,
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
                metadata = [
                    tpdk.models.metadata_read.Metadata-Read(
                        key = 'External-ID', 
                        value = '54412', )
                    ],
                nature = 'physical_item',
                condition = 'USED',
        )
        """

    def testWebhookObject(self):
        """Test WebhookObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
