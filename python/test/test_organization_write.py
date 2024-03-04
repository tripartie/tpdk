# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.179
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.models.organization_write import OrganizationWrite

class TestOrganizationWrite(unittest.TestCase):
    """OrganizationWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationWrite:
        """Test OrganizationWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationWrite`
        """
        model = OrganizationWrite()
        if include_optional:
            return OrganizationWrite(
                id = 56,
                name = '',
                vat_number = '',
                commercial_registry_number = '',
                website_url = '',
                billing_address = None
            )
        else:
            return OrganizationWrite(
                name = '',
                vat_number = '',
                commercial_registry_number = '',
        )
        """

    def testOrganizationWrite(self):
        """Test OrganizationWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
