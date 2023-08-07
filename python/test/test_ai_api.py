# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.29
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import tpdk
from tpdk.api.ai_api import AIApi  # noqa: E501
from tpdk.rest import ApiException


class TestAIApi(unittest.TestCase):
    """AIApi unit test stubs"""

    def setUp(self):
        self.api = tpdk.api.ai_api.AIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_ai_hints_post(self):
        """Test case for api_ai_hints_post

        Dedicated endpoint for our artificial intelligence bot  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
