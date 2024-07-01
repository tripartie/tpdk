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

from tpdk.models.webhook_subscription_read import WebhookSubscriptionRead

class TestWebhookSubscriptionRead(unittest.TestCase):
    """WebhookSubscriptionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookSubscriptionRead:
        """Test WebhookSubscriptionRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookSubscriptionRead`
        """
        model = WebhookSubscriptionRead()
        if include_optional:
            return WebhookSubscriptionRead(
                id = 56,
                event = 'dispute.opened',
                callback_url = 'https://company.tld/webhook/tripartie',
                webhook_secret = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return WebhookSubscriptionRead(
                webhook_secret = '',
        )
        """

    def testWebhookSubscriptionRead(self):
        """Test WebhookSubscriptionRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
