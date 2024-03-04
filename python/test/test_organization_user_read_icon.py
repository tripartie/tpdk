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

from tpdk.models.organization_user_read_icon import OrganizationUserReadIcon

class TestOrganizationUserReadIcon(unittest.TestCase):
    """OrganizationUserReadIcon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationUserReadIcon:
        """Test OrganizationUserReadIcon
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationUserReadIcon`
        """
        model = OrganizationUserReadIcon()
        if include_optional:
            return OrganizationUserReadIcon(
                public_url = https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg
            )
        else:
            return OrganizationUserReadIcon(
                public_url = https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg,
        )
        """

    def testOrganizationUserReadIcon(self):
        """Test OrganizationUserReadIcon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
