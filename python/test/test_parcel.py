# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.167
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.parcel import Parcel

class TestParcel(unittest.TestCase):
    """Parcel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Parcel:
        """Test Parcel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Parcel`
        """
        model = Parcel()
        if include_optional:
            return Parcel(
                id = 56,
                carrier = 'SwissPost',
                identifier = '8J001271466474',
                price = 4.88,
                refundable = True,
                currency = 'EUR',
                status = 'CREATED',
                dispute = 'https://example.com/',
                transaction = 'https://example.com/',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Parcel(
                carrier = 'SwissPost',
                identifier = '8J001271466474',
        )
        """

    def testParcel(self):
        """Test Parcel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
