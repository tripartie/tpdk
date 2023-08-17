# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.46
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.persona_auth_return import PersonaAuthReturn  # noqa: E501
from tpdk.rest import ApiException

class TestPersonaAuthReturn(unittest.TestCase):
    """PersonaAuthReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PersonaAuthReturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaAuthReturn`
        """
        model = tpdk.models.persona_auth_return.PersonaAuthReturn()  # noqa: E501
        if include_optional :
            return PersonaAuthReturn(
                auth_url = 'https://next.tripartie.app/?d=01ARZ3NDEKTSV4RRFFQ69G5FAV&t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTIzNDU2Nzg5LCJuYW1lIjoiSm9zZXBoIn0.OpOSSw7e485LOP5PrzScxHb7SR6sAOMRckfFwi4rp7o', 
                expire_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return PersonaAuthReturn(
        )
        """

    def testPersonaAuthReturn(self):
        """Test PersonaAuthReturn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
