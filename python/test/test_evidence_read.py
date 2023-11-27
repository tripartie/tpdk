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

from tpdk.models.evidence_read import EvidenceRead

class TestEvidenceRead(unittest.TestCase):
    """EvidenceRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EvidenceRead:
        """Test EvidenceRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EvidenceRead`
        """
        model = EvidenceRead()
        if include_optional:
            return EvidenceRead(
                id = 56,
                status = 'SUBMITTED',
                media = tpdk.models.media_read.Media-Read(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                additional_information = 'The motherboard I received have a minor scratch at the bottom, here is the proof.',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                publisher = 'BUYER'
            )
        else:
            return EvidenceRead(
                status = 'SUBMITTED',
        )
        """

    def testEvidenceRead(self):
        """Test EvidenceRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
