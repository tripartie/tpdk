# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.199
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.models.evaluation_write import EvaluationWrite

class TestEvaluationWrite(unittest.TestCase):
    """EvaluationWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EvaluationWrite:
        """Test EvaluationWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EvaluationWrite`
        """
        model = EvaluationWrite()
        if include_optional:
            return EvaluationWrite(
                rating = 7,
                comment = 'quickly handled and despite a minor issue, everything did go well enough!'
            )
        else:
            return EvaluationWrite(
                rating = 7,
        )
        """

    def testEvaluationWrite(self):
        """Test EvaluationWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
