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
from tpdk.api.safe_checkout_api import SafeCheckoutApi  # noqa: E501
from tpdk.rest import ApiException


class TestSafeCheckoutApi(unittest.TestCase):
    """SafeCheckoutApi unit test stubs"""

    def setUp(self):
        self.api = tpdk.api.safe_checkout_api.SafeCheckoutApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_offers_get_collection(self):
        """Test case for api_offers_get_collection

        Read issued Offers  # noqa: E501
        """
        pass

    def test_api_offers_post(self):
        """Test case for api_offers_post

        Create an Offer and retrieve url  # noqa: E501
        """
        pass

    def test_api_offers_ulid_get(self):
        """Test case for api_offers_ulid_get

        Read an Offer  # noqa: E501
        """
        pass

    def test_api_offers_ulidmedias_id_delete(self):
        """Test case for api_offers_ulidmedias_id_delete

        Removes the Media resource.  # noqa: E501
        """
        pass

    def test_api_offers_ulidmedias_post(self):
        """Test case for api_offers_ulidmedias_post

        Upload a picture for a given Offer  # noqa: E501
        """
        pass

    def test_api_offers_ulidtransactions_get_collection(self):
        """Test case for api_offers_ulidtransactions_get_collection

        Retrieve Payment Intents for Offer  # noqa: E501
        """
        pass

    def test_api_offers_ulidtransactions_idevaluations_post(self):
        """Test case for api_offers_ulidtransactions_idevaluations_post

        Submit an Evaluation for the Offer  # noqa: E501
        """
        pass

    def test_api_offers_ulidtransactions_post(self):
        """Test case for api_offers_ulidtransactions_post

        Create a Payment Intent for Offer  # noqa: E501
        """
        pass

    def test_api_personas_idoffers_delete(self):
        """Test case for api_personas_idoffers_delete

        Revoke an Offer for given Persona  # noqa: E501
        """
        pass

    def test_api_personas_idoffers_get_collection(self):
        """Test case for api_personas_idoffers_get_collection

        List or Search Offers for given Persona  # noqa: E501
        """
        pass

    def test_api_personas_idoffers_patch(self):
        """Test case for api_personas_idoffers_patch

        Update an Offer for given Persona  # noqa: E501
        """
        pass

    def test_api_personas_idoffers_post(self):
        """Test case for api_personas_idoffers_post

        Create an Offer for given Persona  # noqa: E501
        """
        pass

    def test_api_transactions_get_collection(self):
        """Test case for api_transactions_get_collection

        Retrieves the collection of Transaction resources.  # noqa: E501
        """
        pass

    def test_api_transactions_uliddispute_delete(self):
        """Test case for api_transactions_uliddispute_delete

        Abandon claims on Dispute  # noqa: E501
        """
        pass

    def test_api_transactions_uliddispute_get(self):
        """Test case for api_transactions_uliddispute_get

        Read Dispute from existing Transaction  # noqa: E501
        """
        pass

    def test_api_transactions_uliddispute_patch(self):
        """Test case for api_transactions_uliddispute_patch

        Interact with a Dispute  # noqa: E501
        """
        pass

    def test_api_transactions_uliddispute_post(self):
        """Test case for api_transactions_uliddispute_post

        Open a Dispute related to existing Transaction  # noqa: E501
        """
        pass

    def test_api_transactions_ulidparcels_get(self):
        """Test case for api_transactions_ulidparcels_get

        Read single parcel state  # noqa: E501
        """
        pass

    def test_api_transactions_ulidparcels_id_delete(self):
        """Test case for api_transactions_ulidparcels_id_delete

        Withdraw shipment from Transaction  # noqa: E501
        """
        pass

    def test_api_transactions_ulidparcels_post(self):
        """Test case for api_transactions_ulidparcels_post

        Manually declare package shipped for Transaction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
