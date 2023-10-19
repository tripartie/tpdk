# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.92
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.api.branding_api import BrandingApi  # noqa: E501


class TestBrandingApi(unittest.TestCase):
    """BrandingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BrandingApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_api_organizations_id_patch(self) -> None:
        """Test case for api_organizations_id_patch

        Update your Organization details, branding or parameters  # noqa: E501
        """
        pass

    def test_api_organizations_idicon_delete(self) -> None:
        """Test case for api_organizations_idicon_delete

        Unset your Organization Icon  # noqa: E501
        """
        pass

    def test_api_organizations_idicon_post(self) -> None:
        """Test case for api_organizations_idicon_post

        Upload your Organization Icon  # noqa: E501
        """
        pass

    def test_api_organizations_idlogo_delete(self) -> None:
        """Test case for api_organizations_idlogo_delete

        Unset your Organization Logo  # noqa: E501
        """
        pass

    def test_api_organizations_idlogo_post(self) -> None:
        """Test case for api_organizations_idlogo_post

        Upload your Organization logo  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
