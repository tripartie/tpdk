# coding: utf-8

"""
    Resolution Center

    Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution.

    The version of the OpenAPI document: 2.0.208
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.models.organization_media_read import OrganizationMediaRead

class TestOrganizationMediaRead(unittest.TestCase):
    """OrganizationMediaRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationMediaRead:
        """Test OrganizationMediaRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationMediaRead`
        """
        model = OrganizationMediaRead()
        if include_optional:
            return OrganizationMediaRead(
                public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg'
            )
        else:
            return OrganizationMediaRead(
                public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg',
        )
        """

    def testOrganizationMediaRead(self):
        """Test OrganizationMediaRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()