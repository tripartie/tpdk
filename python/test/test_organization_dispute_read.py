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

from tpdk.models.organization_dispute_read import OrganizationDisputeRead

class TestOrganizationDisputeRead(unittest.TestCase):
    """OrganizationDisputeRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationDisputeRead:
        """Test OrganizationDisputeRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationDisputeRead`
        """
        model = OrganizationDisputeRead()
        if include_optional:
            return OrganizationDisputeRead(
                name = '',
                website_url = '',
                custom_base_url = '',
                icon = tpdk.models.dispute_media_read.Dispute-Media-Read(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                logo = tpdk.models.dispute_media_read.Dispute-Media-Read(
                    public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ),
                primary_color = '',
                direct_notification_toggle = True,
                persona_auth_portal_toggle = True,
                counter_proposal_toggle = True,
                flat_rate_enabled = True
            )
        else:
            return OrganizationDisputeRead(
                direct_notification_toggle = True,
                persona_auth_portal_toggle = True,
                counter_proposal_toggle = True,
        )
        """

    def testOrganizationDisputeRead(self):
        """Test OrganizationDisputeRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
