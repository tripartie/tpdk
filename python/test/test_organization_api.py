# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.39
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import tpdk
from tpdk.api.organization_api import OrganizationApi  # noqa: E501
from tpdk.rest import ApiException


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self):
        self.api = tpdk.api.organization_api.OrganizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_organizations_get_collection(self):
        """Test case for api_organizations_get_collection

        Retrieves the collection of Organization resources.  # noqa: E501
        """
        pass

    def test_api_organizations_id_get(self):
        """Test case for api_organizations_id_get

        Retrieves a Organization resource.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
