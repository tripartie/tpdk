# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.35
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.parcel import Parcel  # noqa: E501
from tpdk.rest import ApiException

class TestParcel(unittest.TestCase):
    """Parcel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Parcel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Parcel`
        """
        model = tpdk.models.parcel.Parcel()  # noqa: E501
        if include_optional :
            return Parcel(
                id = 56, 
                carrier = 'SwissPost', 
                identifier = '8J001271466474', 
                price = 4.88, 
                currency = 'EUR', 
                status = '', 
                dispute = '', 
                transaction = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
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
