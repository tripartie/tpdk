# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.9
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import tpdk
from tpdk.api.notification_api import NotificationApi  # noqa: E501
from tpdk.rest import ApiException


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    def setUp(self):
        self.api = tpdk.api.notification_api.NotificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_personas_idnotifications_get_collection(self):
        """Test case for api_personas_idnotifications_get_collection

        Retrieve pending notifications for Persona  # noqa: E501
        """
        pass

    def test_api_personas_persona_idnotifications_id_patch(self):
        """Test case for api_personas_persona_idnotifications_id_patch

        Mark as read/unread a notification for Persona  # noqa: E501
        """
        pass

    def test_api_users_idnotifications_get_collection(self):
        """Test case for api_users_idnotifications_get_collection

        Retrieves the collection of Notification resources.  # noqa: E501
        """
        pass

    def test_api_users_user_idnotifications_id_patch(self):
        """Test case for api_users_user_idnotifications_id_patch

        Mark as read/unread a notification for User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
