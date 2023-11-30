# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.134
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.api.resolution_center_api import ResolutionCenterApi


class TestResolutionCenterApi(unittest.TestCase):
    """ResolutionCenterApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ResolutionCenterApi()

    def tearDown(self) -> None:
        pass

    def test_api_disputes_get_collection(self) -> None:
        """Test case for api_disputes_get_collection

        Retrieves the collection of Dispute resources.
        """
        pass

    def test_api_disputes_post(self) -> None:
        """Test case for api_disputes_post

        Draft a standalone Dispute
        """
        pass

    def test_api_disputes_ulid_delete(self) -> None:
        """Test case for api_disputes_ulid_delete

        Abandon claims on Dispute
        """
        pass

    def test_api_disputes_ulid_get(self) -> None:
        """Test case for api_disputes_ulid_get

        Retrieves a Dispute resource.
        """
        pass

    def test_api_disputes_ulid_patch(self) -> None:
        """Test case for api_disputes_ulid_patch

        Update the Dispute
        """
        pass

    def test_api_disputes_ulidevaluations_post(self) -> None:
        """Test case for api_disputes_ulidevaluations_post

        Submit an Evaluation for the Dispute
        """
        pass

    def test_api_disputes_ulidevidences_get_collection(self) -> None:
        """Test case for api_disputes_ulidevidences_get_collection

        Retrieve all Evidences in Dispute
        """
        pass

    def test_api_disputes_ulidevidences_id_delete(self) -> None:
        """Test case for api_disputes_ulidevidences_id_delete

        Withdraw an Evidence from a Dispute
        """
        pass

    def test_api_disputes_ulidevidences_idmedia_post(self) -> None:
        """Test case for api_disputes_ulidevidences_idmedia_post

        Upload attachment in regard of described Evidence
        """
        pass

    def test_api_disputes_ulidevidences_post(self) -> None:
        """Test case for api_disputes_ulidevidences_post

        Submit an Evidence to the Dispute case
        """
        pass

    def test_api_disputes_ulidparcels_get_collection(self) -> None:
        """Test case for api_disputes_ulidparcels_get_collection

        Retrieves the collection of Parcel resources.
        """
        pass

    def test_api_disputes_ulidparcels_id_delete(self) -> None:
        """Test case for api_disputes_ulidparcels_id_delete

        Removes the Parcel resource.
        """
        pass

    def test_api_disputes_ulidparcels_post(self) -> None:
        """Test case for api_disputes_ulidparcels_post

        Creates a Parcel resource.
        """
        pass

    def test_api_offers_ulidmedias_post(self) -> None:
        """Test case for api_offers_ulidmedias_post

        Upload a picture for a given Offer
        """
        pass


if __name__ == '__main__':
    unittest.main()
