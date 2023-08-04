# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.28
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import tpdk
from tpdk.api.persona_api import PersonaApi  # noqa: E501
from tpdk.rest import ApiException


class TestPersonaApi(unittest.TestCase):
    """PersonaApi unit test stubs"""

    def setUp(self):
        self.api = tpdk.api.persona_api.PersonaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_personas_get_collection(self):
        """Test case for api_personas_get_collection

        Retrieves the collection of Persona resources.  # noqa: E501
        """
        pass

    def test_api_personas_id_delete(self):
        """Test case for api_personas_id_delete

        Unregister a Persona (Your customer)  # noqa: E501
        """
        pass

    def test_api_personas_id_get(self):
        """Test case for api_personas_id_get

        Retrieves a Persona resource.  # noqa: E501
        """
        pass

    def test_api_personas_id_patch(self):
        """Test case for api_personas_id_patch

        Updates the Persona resource.  # noqa: E501
        """
        pass

    def test_api_personas_idtoken_post(self):
        """Test case for api_personas_idtoken_post

        Issue authenticated URL for single end-user  # noqa: E501
        """
        pass

    def test_api_personas_post(self):
        """Test case for api_personas_post

        Register a Persona (Your customer)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
