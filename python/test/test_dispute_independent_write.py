# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.114
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tpdk.models.dispute_independent_write import DisputeIndependentWrite

class TestDisputeIndependentWrite(unittest.TestCase):
    """DisputeIndependentWrite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DisputeIndependentWrite:
        """Test DisputeIndependentWrite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DisputeIndependentWrite`
        """
        model = DisputeIndependentWrite()
        if include_optional:
            return DisputeIndependentWrite(
                transaction = tpdk.models.transaction_independent_write.Transaction-IndependentWrite(
                    offer = tpdk.models.offer_independent_write.Offer-IndependentWrite(
                        public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                        seller = tpdk.models.persona_independent_write.Persona-IndependentWrite(
                            first_name = 'John', 
                            last_name = 'Doe', 
                            gender = 'RATHER_NOT_SAY', 
                            date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            language = 'fr', 
                            email = 'john.doe@gmail.com', 
                            mobile_phone_number = '+33745214529', 
                            address = tpdk.models.address_independent_write.Address-IndependentWrite(
                                company_name = 'Company Tld', 
                                country_code = 'FRA', 
                                zip_code = '75004', 
                                city_name = 'Paris', 
                                first_line = '118 avenue des champs élysées', 
                                second_line = 'Apt 6E', 
                                building_name = 'Electron', 
                                building_floor = 'Third floor', 
                                gate_or_portal_or_inbox_code = '3124', ), 
                            external_purchase_count = 56, 
                            external_sell_count = 56, 
                            metadata = [
                                tpdk.models.metadata_independent_write.Metadata-IndependentWrite(
                                    key = 'External-ID', 
                                    value = '54412', )
                                ], ), 
                        nature = 'physical_item', 
                        title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                        description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 
                        unit_price = 125.54, 
                        currency_code = 'EUR', 
                        item_count = 1, 
                        condition = 'USED', 
                        weight_in_gram = 56, 
                        ean_code = '4718017388450', 
                        metadata = [
                            tpdk.models.metadata_independent_write.Metadata-IndependentWrite(
                                key = 'External-ID', 
                                value = '54412', )
                            ], ), 
                    buyer = tpdk.models.persona_independent_write.Persona-IndependentWrite(
                        first_name = 'John', 
                        last_name = 'Doe', 
                        gender = 'RATHER_NOT_SAY', 
                        date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        language = 'fr', 
                        email = 'john.doe@gmail.com', 
                        mobile_phone_number = '+33745214529', 
                        external_purchase_count = 56, 
                        external_sell_count = 56, ), 
                    fees = 1.337, 
                    metadata = , 
                    parcels = [
                        tpdk.models.parcel_independent_write.Parcel-IndependentWrite(
                            carrier = 'SwissPost', 
                            identifier = '8J001271466474', 
                            price = 4.88, 
                            currency = 'EUR', )
                        ], ),
                redirect_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold?from_dispute=true',
                metadata = [
                    tpdk.models.metadata_independent_write.Metadata-IndependentWrite(
                        key = 'External-ID', 
                        value = '54412', )
                    ]
            )
        else:
            return DisputeIndependentWrite(
                transaction = tpdk.models.transaction_independent_write.Transaction-IndependentWrite(
                    offer = tpdk.models.offer_independent_write.Offer-IndependentWrite(
                        public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                        seller = tpdk.models.persona_independent_write.Persona-IndependentWrite(
                            first_name = 'John', 
                            last_name = 'Doe', 
                            gender = 'RATHER_NOT_SAY', 
                            date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            language = 'fr', 
                            email = 'john.doe@gmail.com', 
                            mobile_phone_number = '+33745214529', 
                            address = tpdk.models.address_independent_write.Address-IndependentWrite(
                                company_name = 'Company Tld', 
                                country_code = 'FRA', 
                                zip_code = '75004', 
                                city_name = 'Paris', 
                                first_line = '118 avenue des champs élysées', 
                                second_line = 'Apt 6E', 
                                building_name = 'Electron', 
                                building_floor = 'Third floor', 
                                gate_or_portal_or_inbox_code = '3124', ), 
                            external_purchase_count = 56, 
                            external_sell_count = 56, 
                            metadata = [
                                tpdk.models.metadata_independent_write.Metadata-IndependentWrite(
                                    key = 'External-ID', 
                                    value = '54412', )
                                ], ), 
                        nature = 'physical_item', 
                        title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                        description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 
                        unit_price = 125.54, 
                        currency_code = 'EUR', 
                        item_count = 1, 
                        condition = 'USED', 
                        weight_in_gram = 56, 
                        ean_code = '4718017388450', 
                        metadata = [
                            tpdk.models.metadata_independent_write.Metadata-IndependentWrite(
                                key = 'External-ID', 
                                value = '54412', )
                            ], ), 
                    buyer = tpdk.models.persona_independent_write.Persona-IndependentWrite(
                        first_name = 'John', 
                        last_name = 'Doe', 
                        gender = 'RATHER_NOT_SAY', 
                        date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        language = 'fr', 
                        email = 'john.doe@gmail.com', 
                        mobile_phone_number = '+33745214529', 
                        external_purchase_count = 56, 
                        external_sell_count = 56, ), 
                    fees = 1.337, 
                    metadata = , 
                    parcels = [
                        tpdk.models.parcel_independent_write.Parcel-IndependentWrite(
                            carrier = 'SwissPost', 
                            identifier = '8J001271466474', 
                            price = 4.88, 
                            currency = 'EUR', )
                        ], ),
        )
        """

    def testDisputeIndependentWrite(self):
        """Test DisputeIndependentWrite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
