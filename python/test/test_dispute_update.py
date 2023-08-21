# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.49
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.dispute_update import DisputeUpdate  # noqa: E501
from tpdk.rest import ApiException

class TestDisputeUpdate(unittest.TestCase):
    """DisputeUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DisputeUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputeUpdate`
        """
        model = tpdk.models.dispute_update.DisputeUpdate()  # noqa: E501
        if include_optional :
            return DisputeUpdate(
                item_count = 1, 
                issue_type = 'NOT_AS_DESCRIBED', 
                issue_in_description_type = 'WRONG_COLOUR', 
                issue_mentioned_in_offer = True, 
                issue_details = 'The item received have multiple impacts on the left side, this was not mentioned and I feel a bit sad. Although it is usable as-is, I expected it without flaws.', 
                complainant_stake = 'LOW', 
                chosen_solution = 'PARTIAL_REFUND_WITH_PARTIAL_RETURN', 
                chosen_partial_refund_amount = 40, 
                counter_solution = 'PARTIAL_REFUND_WITH_PARTIAL_RETURN', 
                counter_partial_refund_amount = 30, 
                complainant_approval = True, 
                seller_approval = True
            )
        else :
            return DisputeUpdate(
        )
        """

    def testDisputeUpdate(self):
        """Test DisputeUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
