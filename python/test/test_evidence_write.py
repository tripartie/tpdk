# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.165
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.evidence_write import EvidenceWrite

class TestEvidenceWrite(unittest.TestCase):
    """EvidenceWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EvidenceWrite:
        """Test EvidenceWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EvidenceWrite`
        """
        model = EvidenceWrite()
        if include_optional:
            return EvidenceWrite(
                additional_information = 'The motherboard I received have a minor scratch at the bottom, here is the proof.'
            )
        else:
            return EvidenceWrite(
                additional_information = 'The motherboard I received have a minor scratch at the bottom, here is the proof.',
        )
        """

    def testEvidenceWrite(self):
        """Test EvidenceWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
