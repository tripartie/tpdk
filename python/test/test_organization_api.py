# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.167
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.api.organization_api import OrganizationApi


class TestOrganizationApi(unittest.TestCase):
    """OrganizationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationApi()

    def tearDown(self) -> None:
        pass

    def test_api_organizations_get_collection(self) -> None:
        """Test case for api_organizations_get_collection

        Retrieves the collection of Organization resources.
        """
        pass

    def test_api_organizations_id_get(self) -> None:
        """Test case for api_organizations_id_get

        Retrieves a Organization resource.
        """
        pass


if __name__ == '__main__':
    unittest.main()
