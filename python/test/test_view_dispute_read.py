# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.163
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.view_dispute_read import ViewDisputeRead

class TestViewDisputeRead(unittest.TestCase):
    """ViewDisputeRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ViewDisputeRead:
        """Test ViewDisputeRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ViewDisputeRead`
        """
        model = ViewDisputeRead()
        if include_optional:
            return ViewDisputeRead(
                hit_count = 1,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                named_source = 'BUYER'
            )
        else:
            return ViewDisputeRead(
                hit_count = 1,
        )
        """

    def testViewDisputeRead(self):
        """Test ViewDisputeRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
