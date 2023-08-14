# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.39
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import tpdk
from tpdk.api.resolution_center_api import ResolutionCenterApi  # noqa: E501
from tpdk.rest import ApiException


class TestResolutionCenterApi(unittest.TestCase):
    """ResolutionCenterApi unit test stubs"""

    def setUp(self):
        self.api = tpdk.api.resolution_center_api.ResolutionCenterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_disputes_get_collection(self):
        """Test case for api_disputes_get_collection

        Retrieves the collection of Dispute resources.  # noqa: E501
        """
        pass

    def test_api_disputes_post(self):
        """Test case for api_disputes_post

        Draft a standalone Dispute  # noqa: E501
        """
        pass

    def test_api_disputes_ulid_delete(self):
        """Test case for api_disputes_ulid_delete

        Abandon claims on Dispute  # noqa: E501
        """
        pass

    def test_api_disputes_ulid_get(self):
        """Test case for api_disputes_ulid_get

        Retrieves a Dispute resource.  # noqa: E501
        """
        pass

    def test_api_disputes_ulid_patch(self):
        """Test case for api_disputes_ulid_patch

        Update the Dispute  # noqa: E501
        """
        pass

    def test_api_disputes_ulidevaluations_post(self):
        """Test case for api_disputes_ulidevaluations_post

        Submit an Evaluation for the Dispute  # noqa: E501
        """
        pass

    def test_api_disputes_ulidevidences_get_collection(self):
        """Test case for api_disputes_ulidevidences_get_collection

        Retrieve all Evidences in Dispute  # noqa: E501
        """
        pass

    def test_api_disputes_ulidevidences_id_delete(self):
        """Test case for api_disputes_ulidevidences_id_delete

        Withdraw an Evidence from a Dispute  # noqa: E501
        """
        pass

    def test_api_disputes_ulidevidences_idmedia_post(self):
        """Test case for api_disputes_ulidevidences_idmedia_post

        Upload attachment in regard of described Evidence  # noqa: E501
        """
        pass

    def test_api_disputes_ulidevidences_post(self):
        """Test case for api_disputes_ulidevidences_post

        Submit an Evidence to the Dispute case  # noqa: E501
        """
        pass

    def test_api_disputes_ulidparcels_get_collection(self):
        """Test case for api_disputes_ulidparcels_get_collection

        Retrieves the collection of Parcel resources.  # noqa: E501
        """
        pass

    def test_api_disputes_ulidparcels_id_delete(self):
        """Test case for api_disputes_ulidparcels_id_delete

        Removes the Parcel resource.  # noqa: E501
        """
        pass

    def test_api_disputes_ulidparcels_id_get(self):
        """Test case for api_disputes_ulidparcels_id_get

        Read single parcel state  # noqa: E501
        """
        pass

    def test_api_disputes_ulidparcels_post(self):
        """Test case for api_disputes_ulidparcels_post

        Creates a Parcel resource.  # noqa: E501
        """
        pass

    def test_api_offers_ulidmedias_post(self):
        """Test case for api_offers_ulidmedias_post

        Upload a picture for a given Offer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
