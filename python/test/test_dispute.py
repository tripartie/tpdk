# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.26
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.dispute import Dispute  # noqa: E501
from tpdk.rest import ApiException

class TestDispute(unittest.TestCase):
    """Dispute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Dispute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Dispute`
        """
        model = tpdk.models.dispute.Dispute()  # noqa: E501
        if include_optional :
            return Dispute(
                id = 56, 
                ulid = '01ARZ3NDEKTSV4RRFFQ69G5FAV', 
                url = 'https://next.tripartie.app/?d=01ARZ3NDEKTSV4RRFFQ69G5FAV', 
                transaction = '', 
                status = 'CREATED', 
                redirect_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold?from_dispute=true', 
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
                    ''
                    ], 
                messages = [
                    tpdk.models.message.Message(
                        id = 56, 
                        dispute = '', 
                        agent = '', 
                        from = '', 
                        to = '', 
                        body = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
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
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
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
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                iri = '', 
                message_count = 6
            )
        else :
            return Dispute(
                ulid = '01ARZ3NDEKTSV4RRFFQ69G5FAV',
                status = 'CREATED',
                complainant_truthfulness_score = 100,
                seller_truthfulness_score = 100,
                parcels = [
                    ''
                    ],
                messages = [
                    tpdk.models.message.Message(
                        id = 56, 
                        dispute = '', 
                        agent = '', 
                        from = '', 
                        to = '', 
                        body = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
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
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
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
        )
        """

    def testDispute(self):
        """Test Dispute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
