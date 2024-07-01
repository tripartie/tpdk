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

from tpdk.models.persona_metadata_update import PersonaMetadataUpdate

class TestPersonaMetadataUpdate(unittest.TestCase):
    """PersonaMetadataUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PersonaMetadataUpdate:
        """Test PersonaMetadataUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PersonaMetadataUpdate`
        """
        model = PersonaMetadataUpdate()
        if include_optional:
            return PersonaMetadataUpdate(
                key = 'External-ID',
                value = '54412'
            )
        else:
            return PersonaMetadataUpdate(
        )
        """

    def testPersonaMetadataUpdate(self):
        """Test PersonaMetadataUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
