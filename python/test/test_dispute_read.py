# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.74
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.dispute_read import DisputeRead  # noqa: E501

class TestDisputeRead(unittest.TestCase):
    """DisputeRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisputeRead:
        """Test DisputeRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputeRead`
        """
        model = DisputeRead()  # noqa: E501
        if include_optional:
            return DisputeRead(
                ulid = '01ARZ3NDEKTSV4RRFFQ69G5FAV',
                transaction = tpdk.models.transaction_read.Transaction-Read(
                    ulid = '', 
                    offer = tpdk.models.offer_read.Offer-Read(
                        ulid = '', 
                        public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                        organization = tpdk.models.organization_read.Organization-Read(
                            name = '', 
                            website_url = '', 
                            custom_base_url = '', 
                            icon = tpdk.models.media_read.Media-Read(
                                public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ), 
                            logo = tpdk.models.media_read.Media-Read(
                                public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ), 
                            primary_color = '', 
                            secondary_color = '', 
                            accent_color = '', 
                            error_color = '', 
                            info_color = '', 
                            success_color = '', 
                            warning_color = '', 
                            direct_notification_toggle = True, 
                            persona_auth_portal_toggle = True, 
                            flat_rate_enabled = True, 
                            rate_commission_safe_checkout = 1.337, ), 
                        seller = '', 
                        nature = 'physical_item', 
                        title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                        description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 
                        unit_price = 125.54, 
                        currency_code = 'EUR', 
                        item_count = 1, 
                        condition = 'USED', 
                        medias = [
                            
                            ], ), 
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
                            status = 'CREATED', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                status = 'CREATED',
                redirect_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold?from_dispute=true',
                item_count = 1,
                issue_type = 'NOT_AS_DESCRIBED',
                issue_in_description_type = 'WRONG_COLOUR',
                issue_mentioned_in_offer = True,
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
                        status = 'CREATED', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                metadata = [
                    tpdk.models.metadata_read.Metadata-Read(
                        key = 'External-ID', 
                        value = '54412', )
                    ],
                events = [
                    tpdk.models.workflow_event_read.WorkflowEvent-Read(
                        label = '', 
                        from = '', 
                        to = '', 
                        event = 'dispute.opened', 
                        occurred_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        initiator = '', )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status_expiration = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                awaited_party = 'BUYER',
                iri = '',
                message_count = 6
            )
        else:
            return DisputeRead(
                ulid = '01ARZ3NDEKTSV4RRFFQ69G5FAV',
                status = 'CREATED',
                complainant_truthfulness_score = 100,
                seller_truthfulness_score = 100,
                parcels = [
                    tpdk.models.parcel_read.Parcel-Read(
                        carrier = 'SwissPost', 
                        identifier = '8J001271466474', 
                        price = 4.88, 
                        currency = 'EUR', 
                        status = 'CREATED', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                metadata = [
                    tpdk.models.metadata_read.Metadata-Read(
                        key = 'External-ID', 
                        value = '54412', )
                    ],
        )
        """

    def testDisputeRead(self):
        """Test DisputeRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
