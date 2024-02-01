# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.165
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tpdk.api.safe_checkout_api import SafeCheckoutApi


class TestSafeCheckoutApi(unittest.TestCase):
    """SafeCheckoutApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SafeCheckoutApi()

    def tearDown(self) -> None:
        pass

    def test_api_offers_get_collection(self) -> None:
        """Test case for api_offers_get_collection

        Read issued Offers
        """
        pass

    def test_api_offers_post(self) -> None:
        """Test case for api_offers_post

        Create an Offer and retrieve url
        """
        pass

    def test_api_offers_ulid_get(self) -> None:
        """Test case for api_offers_ulid_get

        Read an Offer
        """
        pass

    def test_api_offers_ulidmedias_id_delete(self) -> None:
        """Test case for api_offers_ulidmedias_id_delete

        Removes the Media resource.
        """
        pass

    def test_api_offers_ulidmedias_post(self) -> None:
        """Test case for api_offers_ulidmedias_post

        Upload a picture for a given Offer
        """
        pass

    def test_api_offers_ulidtransactions_get_collection(self) -> None:
        """Test case for api_offers_ulidtransactions_get_collection

        Retrieve Payment Intents for Offer
        """
        pass

    def test_api_offers_ulidtransactions_idevaluations_post(self) -> None:
        """Test case for api_offers_ulidtransactions_idevaluations_post

        Submit an Evaluation for the Offer
        """
        pass

    def test_api_offers_ulidtransactions_post(self) -> None:
        """Test case for api_offers_ulidtransactions_post

        Create a Payment Intent for Offer
        """
        pass

    def test_api_personas_idoffers_delete(self) -> None:
        """Test case for api_personas_idoffers_delete

        Revoke an Offer for given Persona
        """
        pass

    def test_api_personas_idoffers_get_collection(self) -> None:
        """Test case for api_personas_idoffers_get_collection

        List or Search Offers for given Persona
        """
        pass

    def test_api_personas_idoffers_patch(self) -> None:
        """Test case for api_personas_idoffers_patch

        Update an Offer for given Persona
        """
        pass

    def test_api_personas_idoffers_post(self) -> None:
        """Test case for api_personas_idoffers_post

        Create an Offer for given Persona
        """
        pass

    def test_api_transactions_get_collection(self) -> None:
        """Test case for api_transactions_get_collection

        Retrieves the collection of Transaction resources.
        """
        pass

    def test_api_transactions_uliddispute_delete(self) -> None:
        """Test case for api_transactions_uliddispute_delete

        Abandon claims on Dispute
        """
        pass

    def test_api_transactions_uliddispute_get(self) -> None:
        """Test case for api_transactions_uliddispute_get

        Read Dispute from existing Transaction
        """
        pass

    def test_api_transactions_uliddispute_patch(self) -> None:
        """Test case for api_transactions_uliddispute_patch

        Interact with a Dispute
        """
        pass

    def test_api_transactions_uliddispute_post(self) -> None:
        """Test case for api_transactions_uliddispute_post

        Open a Dispute related to existing Transaction
        """
        pass

    def test_api_transactions_ulidparcels_get_collection(self) -> None:
        """Test case for api_transactions_ulidparcels_get_collection

        Read shipments from Transaction
        """
        pass

    def test_api_transactions_ulidparcels_id_delete(self) -> None:
        """Test case for api_transactions_ulidparcels_id_delete

        Withdraw shipment from Transaction
        """
        pass

    def test_api_transactions_ulidparcels_post(self) -> None:
        """Test case for api_transactions_ulidparcels_post

        Manually declare package shipped for Transaction
        """
        pass


if __name__ == '__main__':
    unittest.main()
