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

from tpdk.api.notification_api import NotificationApi


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotificationApi()

    def tearDown(self) -> None:
        pass

    def test_api_personas_idnotifications_get_collection(self) -> None:
        """Test case for api_personas_idnotifications_get_collection

        Retrieve pending notifications for Persona
        """
        pass

    def test_api_personas_persona_idnotifications_id_patch(self) -> None:
        """Test case for api_personas_persona_idnotifications_id_patch

        Mark as read/unread a notification for Persona
        """
        pass

    def test_api_users_idnotifications_get_collection(self) -> None:
        """Test case for api_users_idnotifications_get_collection

        Retrieves the collection of Notification resources.
        """
        pass

    def test_api_users_user_idnotifications_id_patch(self) -> None:
        """Test case for api_users_user_idnotifications_id_patch

        Mark as read/unread a notification for User
        """
        pass


if __name__ == '__main__':
    unittest.main()
