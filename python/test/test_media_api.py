# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.163
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.api.media_api import MediaApi


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MediaApi()

    def tearDown(self) -> None:
        pass

    def test_api_medias_id_get(self) -> None:
        """Test case for api_medias_id_get

        Retrieves a Media resource.
        """
        pass


if __name__ == '__main__':
    unittest.main()
