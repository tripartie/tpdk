# coding: utf-8

"""
    Resolution Center

    Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution.

    The version of the OpenAPI document: 2.0.208
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.models.dispute_parcel_read import DisputeParcelRead

class TestDisputeParcelRead(unittest.TestCase):
    """DisputeParcelRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisputeParcelRead:
        """Test DisputeParcelRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputeParcelRead`
        """
        model = DisputeParcelRead()
        if include_optional:
            return DisputeParcelRead(
                carrier = 'SwissPost',
                identifier = '8J001271466474',
                price = 4.88,
                refundable = True,
                currency = 'EUR',
                status = 'CREATED',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DisputeParcelRead(
                carrier = 'SwissPost',
                identifier = '8J001271466474',
        )
        """

    def testDisputeParcelRead(self):
        """Test DisputeParcelRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
