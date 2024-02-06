# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.172
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.metadata_independent_write import MetadataIndependentWrite

class TestMetadataIndependentWrite(unittest.TestCase):
    """MetadataIndependentWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataIndependentWrite:
        """Test MetadataIndependentWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataIndependentWrite`
        """
        model = MetadataIndependentWrite()
        if include_optional:
            return MetadataIndependentWrite(
                key = 'External-ID',
                value = '54412'
            )
        else:
            return MetadataIndependentWrite(
        )
        """

    def testMetadataIndependentWrite(self):
        """Test MetadataIndependentWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
