# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.52
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.persona_external_auth import PersonaExternalAuth  # noqa: E501
from tpdk.rest import ApiException

class TestPersonaExternalAuth(unittest.TestCase):
    """PersonaExternalAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PersonaExternalAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaExternalAuth`
        """
        model = tpdk.models.persona_external_auth.PersonaExternalAuth()  # noqa: E501
        if include_optional :
            return PersonaExternalAuth(
                captcha = '', 
                target_url = 'https://next.tripartie.app/?d=01ARZ3NDEKTSV4RRFFQ69G5FAV', 
                plain_password = 'secr$t', 
                email = 'john.doe@gmail.com', 
                mobile_phone_number = '+33745214529'
            )
        else :
            return PersonaExternalAuth(
        )
        """

    def testPersonaExternalAuth(self):
        """Test PersonaExternalAuth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
