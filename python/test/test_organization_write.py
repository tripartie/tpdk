# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.91
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.organization_write import OrganizationWrite  # noqa: E501

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
        model = OrganizationWrite()  # noqa: E501
        if include_optional:
            return OrganizationWrite(
                id = 56,
                name = '',
                vat_number = '',
                commercial_registry_number = '',
                website_url = '',
                billing_address = tpdk.models.address_write.Address-Write(
                    company_name = 'Company Tld', 
                    country_code = 'FRA', 
                    zip_code = '75004', 
                    city_name = 'Paris', 
                    first_line = '118 avenue des champs élysées', 
                    second_line = 'Apt 6E', 
                    building_name = 'Electron', 
                    building_floor = 'Third floor', 
                    gate_or_portal_or_inbox_code = '3124', )
            )
        else:
            return OrganizationWrite(
        )
        """

    def testOrganizationWrite(self):
        """Test OrganizationWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
