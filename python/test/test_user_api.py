# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.22
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import tpdk
from tpdk.api.user_api import UserApi  # noqa: E501
from tpdk.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = tpdk.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_api_clients_get_collection(self):
        """Test case for api_api_clients_get_collection

        Retrieves the collection of ApiClient resources.  # noqa: E501
        """
        pass

    def test_api_api_clients_identifier_delete(self):
        """Test case for api_api_clients_identifier_delete

        Removes the ApiClient resource.  # noqa: E501
        """
        pass

    def test_api_api_clients_identifier_get(self):
        """Test case for api_api_clients_identifier_get

        Retrieves a ApiClient resource.  # noqa: E501
        """
        pass

    def test_api_api_clients_post(self):
        """Test case for api_api_clients_post

        Creates a ApiClient resource.  # noqa: E501
        """
        pass

    def test_api_me_get(self):
        """Test case for api_me_get

        Retrieves a User resource.  # noqa: E501
        """
        pass

    def test_api_personasauthentication_post(self):
        """Test case for api_personasauthentication_post

        Persona Authentication  # noqa: E501
        """
        pass

    def test_api_personasregister_post(self):
        """Test case for api_personasregister_post

        Persona external registration  # noqa: E501
        """
        pass

    def test_api_register_post(self):
        """Test case for api_register_post

        Organization onboarding  # noqa: E501
        """
        pass

    def test_api_users_get_collection(self):
        """Test case for api_users_get_collection

        Retrieves the collection of User resources.  # noqa: E501
        """
        pass

    def test_api_users_id_get(self):
        """Test case for api_users_id_get

        Retrieves a User resource.  # noqa: E501
        """
        pass

    def test_api_users_id_patch(self):
        """Test case for api_users_id_patch

        Updates the User resource.  # noqa: E501
        """
        pass

    def test_api_users_idemail_validation_patch(self):
        """Test case for api_users_idemail_validation_patch

        Validate email ownership  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
