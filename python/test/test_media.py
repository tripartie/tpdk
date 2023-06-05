# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.7
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import tpdk
from tpdk.models.media import Media  # noqa: E501
from tpdk.rest import ApiException

class TestMedia(unittest.TestCase):
    """Media unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Media
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Media`
        """
        model = tpdk.models.media.Media()  # noqa: E501
        if include_optional :
            return Media(
                id = 56, 
                extension = '', 
                filename = '', 
                public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', 
                file = bytes(b'blah'), 
                b64_encoded_tmp_file = '', 
                thumbnail = '', 
                original = '', 
                owner = '', 
                thumbnail_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg'
            )
        else :
            return Media(
                extension = '',
                filename = '',
        )
        """

    def testMedia(self):
        """Test Media"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
