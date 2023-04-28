# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0-b1
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.webhook_subscription_write import WebhookSubscriptionWrite  # noqa: E501
from tpdk.rest import ApiException

class TestWebhookSubscriptionWrite(unittest.TestCase):
    """WebhookSubscriptionWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WebhookSubscriptionWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookSubscriptionWrite`
        """
        model = tpdk.models.webhook_subscription_write.WebhookSubscriptionWrite()  # noqa: E501
        if include_optional :
            return WebhookSubscriptionWrite(
                event = 'dispute.opened', 
                callback_url = 'https://company.tld/webhook/tripartie'
            )
        else :
            return WebhookSubscriptionWrite(
                event = 'dispute.opened',
                callback_url = 'https://company.tld/webhook/tripartie',
        )
        """

    def testWebhookSubscriptionWrite(self):
        """Test WebhookSubscriptionWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
