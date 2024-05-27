# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.204
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_api_api_clients_get_collection(self) -> None:
        """Test case for api_api_clients_get_collection

        Retrieves the collection of ApiClient resources.
        """
        pass

    def test_api_api_clients_identifier_delete(self) -> None:
        """Test case for api_api_clients_identifier_delete

        Removes the ApiClient resource.
        """
        pass

    def test_api_api_clients_identifier_get(self) -> None:
        """Test case for api_api_clients_identifier_get

        Retrieves a ApiClient resource.
        """
        pass

    def test_api_api_clients_post(self) -> None:
        """Test case for api_api_clients_post

        Creates a ApiClient resource.
        """
        pass

    def test_api_invite_post(self) -> None:
        """Test case for api_invite_post

        Organization invite
        """
        pass

    def test_api_me_get(self) -> None:
        """Test case for api_me_get

        Retrieves a User resource.
        """
        pass

    def test_api_personasauthentication_post(self) -> None:
        """Test case for api_personasauthentication_post

        Persona Authentication
        """
        pass

    def test_api_personasme_get(self) -> None:
        """Test case for api_personasme_get

        Retrieve your authenticated Persona
        """
        pass

    def test_api_personasregister_post(self) -> None:
        """Test case for api_personasregister_post

        Persona external registration
        """
        pass

    def test_api_register_post(self) -> None:
        """Test case for api_register_post

        Organization onboarding
        """
        pass

    def test_api_users_get_collection(self) -> None:
        """Test case for api_users_get_collection

        Retrieves the collection of User resources.
        """
        pass

    def test_api_users_id_delete(self) -> None:
        """Test case for api_users_id_delete

        Removes the User resource.
        """
        pass

    def test_api_users_id_get(self) -> None:
        """Test case for api_users_id_get

        Retrieves a User resource.
        """
        pass

    def test_api_users_id_patch(self) -> None:
        """Test case for api_users_id_patch

        Updates the User resource.
        """
        pass

    def test_api_users_idavatar_delete(self) -> None:
        """Test case for api_users_idavatar_delete

        Unset your personal avatar
        """
        pass

    def test_api_users_idavatar_post(self) -> None:
        """Test case for api_users_idavatar_post

        Upload your personal avatar
        """
        pass

    def test_api_users_idemail_patch(self) -> None:
        """Test case for api_users_idemail_patch

        Update user email
        """
        pass

    def test_api_users_idemail_validation_patch(self) -> None:
        """Test case for api_users_idemail_validation_patch

        Validate email ownership
        """
        pass

    def test_api_users_idenable_patch(self) -> None:
        """Test case for api_users_idenable_patch

        Updates the User resource.
        """
        pass

    def test_api_users_idpassword_patch(self) -> None:
        """Test case for api_users_idpassword_patch

        Updates the User resource.
        """
        pass

    def test_api_users_idtotp_setup_patch(self) -> None:
        """Test case for api_users_idtotp_setup_patch

        Updates the User resource.
        """
        pass

    def test_api_users_idtotp_toggle_patch(self) -> None:
        """Test case for api_users_idtotp_toggle_patch

        Updates the User resource.
        """
        pass

    def test_authentication_post(self) -> None:
        """Test case for authentication_post

        User authentication
        """
        pass


if __name__ == '__main__':
    unittest.main()
