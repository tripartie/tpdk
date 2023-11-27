# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.114
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.dispute_post_creation_read import DisputePostCreationRead

class TestDisputePostCreationRead(unittest.TestCase):
    """DisputePostCreationRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisputePostCreationRead:
        """Test DisputePostCreationRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputePostCreationRead`
        """
        model = DisputePostCreationRead()
        if include_optional:
            return DisputePostCreationRead(
                ulid = '01ARZ3NDEKTSV4RRFFQ69G5FAV',
                url = 'https://next.tripartie.app/?d=01ARZ3NDEKTSV4RRFFQ69G5FAV',
                buyer_id = 42,
                seller_id = 58,
                offer_ulid = '01H9QDHBE084BQJN7ME31QSVWS'
            )
        else:
            return DisputePostCreationRead(
        )
        """

    def testDisputePostCreationRead(self):
        """Test DisputePostCreationRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
