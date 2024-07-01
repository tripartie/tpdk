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

from tpdk.models.dispute_workflow_event_read import DisputeWorkflowEventRead

class TestDisputeWorkflowEventRead(unittest.TestCase):
    """DisputeWorkflowEventRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisputeWorkflowEventRead:
        """Test DisputeWorkflowEventRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputeWorkflowEventRead`
        """
        model = DisputeWorkflowEventRead()
        if include_optional:
            return DisputeWorkflowEventRead(
                label = '',
                var_from = '',
                to = '',
                event = 'dispute.opened',
                occurred_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                initiator = 'https://example.com/'
            )
        else:
            return DisputeWorkflowEventRead(
                label = '',
        )
        """

    def testDisputeWorkflowEventRead(self):
        """Test DisputeWorkflowEventRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()