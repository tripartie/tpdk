# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0.b1
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.unprocessable_entity import UnprocessableEntity  # noqa: E501
from tpdk.rest import ApiException

class TestUnprocessableEntity(unittest.TestCase):
    """UnprocessableEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UnprocessableEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnprocessableEntity`
        """
        model = tpdk.models.unprocessable_entity.UnprocessableEntity()  # noqa: E501
        if include_optional :
            return UnprocessableEntity(
                type = 'https://tools.ietf.org/html/rfc2616#section-10', 
                title = 'An error occurred', 
                detail = 'firstName: This value should not be blank.
lastName: This value should not be blank.
email: This value should not be null.
plainPassword: This value should not be null.
originCountry: This value should not be null.
preferredLanguage: This value should not be null.', 
                violations = [
                    tpdk.models.unprocessable_entity_violations_inner.UnprocessableEntity_violations_inner(
                        property_path = 'firstName', 
                        message = 'This value should not be blank.', 
                        code = 'c1051bb4-d103-4f74-8988-acbcafc7fdc3', )
                    ]
            )
        else :
            return UnprocessableEntity(
        )
        """

    def testUnprocessableEntity(self):
        """Test UnprocessableEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()