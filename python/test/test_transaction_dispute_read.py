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
import datetime

from tpdk.models.transaction_dispute_read import TransactionDisputeRead

class TestTransactionDisputeRead(unittest.TestCase):
    """TransactionDisputeRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionDisputeRead:
        """Test TransactionDisputeRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionDisputeRead`
        """
        model = TransactionDisputeRead()
        if include_optional:
            return TransactionDisputeRead(
                ulid = '',
                offer = tpdk.models.offer_dispute/read.Offer-dispute.read(
                    ulid = '', 
                    public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                    organization = tpdk.models.organization_dispute/read.Organization-dispute.read(
                        name = '', 
                        website_url = '', 
                        custom_base_url = '', 
                        icon = tpdk.models.media_read.Media-Read(
                            public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ), 
                        logo = tpdk.models.media_read.Media-Read(
                            public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ), 
                        primary_color = '', 
                        secondary_color = '', 
                        accent_color = '', 
                        error_color = '', 
                        info_color = '', 
                        success_color = '', 
                        warning_color = '', 
                        direct_notification_toggle = True, 
                        persona_auth_portal_toggle = True, 
                        flat_rate_enabled = True, 
                        rate_commission_safe_checkout = 1.337, ), 
                    seller = tpdk.models.persona_read.Persona-Read(
                        id = 56, 
                        first_name = 'John', 
                        last_name = 'Doe', 
                        language = 'fr', 
                        email = 'john.doe@gmail.com', 
                        mobile_phone_number = '+33745214529', ), 
                    nature = 'physical_item', 
                    title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                    description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 
                    unit_price = 125.54, 
                    currency_code = 'EUR', 
                    item_count = 1, 
                    condition = 'USED', 
                    medias = [
                        
                        ], ),
                buyer = tpdk.models.persona_read.Persona-Read(
                    id = 56, 
                    first_name = 'John', 
                    last_name = 'Doe', 
                    language = 'fr', 
                    email = 'john.doe@gmail.com', 
                    mobile_phone_number = '+33745214529', ),
                fees = 1.337,
                refundable_fees = True,
                metadata = [
                    tpdk.models.metadata_independent_write.Metadata-IndependentWrite(
                        key = 'External-ID', 
                        value = '54412', )
                    ],
                parcels = [
                    tpdk.models.parcel_dispute/read.Parcel-dispute.read(
                        carrier = 'SwissPost', 
                        identifier = '8J001271466474', 
                        price = 4.88, 
                        refundable = True, 
                        currency = 'EUR', 
                        status = 'CREATED', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return TransactionDisputeRead(
                ulid = '',
                offer = tpdk.models.offer_dispute/read.Offer-dispute.read(
                    ulid = '', 
                    public_url = 'https://marketplace.tld/offers/that-special-item-i-wish-to-sold', 
                    organization = tpdk.models.organization_dispute/read.Organization-dispute.read(
                        name = '', 
                        website_url = '', 
                        custom_base_url = '', 
                        icon = tpdk.models.media_read.Media-Read(
                            public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ), 
                        logo = tpdk.models.media_read.Media-Read(
                            public_url = 'https://cdn.tripartie.app/b15e64db-fbd2-442b-afee-69ee45e2959b.jpg', ), 
                        primary_color = '', 
                        secondary_color = '', 
                        accent_color = '', 
                        error_color = '', 
                        info_color = '', 
                        success_color = '', 
                        warning_color = '', 
                        direct_notification_toggle = True, 
                        persona_auth_portal_toggle = True, 
                        flat_rate_enabled = True, 
                        rate_commission_safe_checkout = 1.337, ), 
                    seller = tpdk.models.persona_read.Persona-Read(
                        id = 56, 
                        first_name = 'John', 
                        last_name = 'Doe', 
                        language = 'fr', 
                        email = 'john.doe@gmail.com', 
                        mobile_phone_number = '+33745214529', ), 
                    nature = 'physical_item', 
                    title = 'ASUS TUF X570-PLUS GAMING Motherboard', 
                    description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 
                    unit_price = 125.54, 
                    currency_code = 'EUR', 
                    item_count = 1, 
                    condition = 'USED', 
                    medias = [
                        
                        ], ),
                buyer = tpdk.models.persona_read.Persona-Read(
                    id = 56, 
                    first_name = 'John', 
                    last_name = 'Doe', 
                    language = 'fr', 
                    email = 'john.doe@gmail.com', 
                    mobile_phone_number = '+33745214529', ),
        )
        """

    def testTransactionDisputeRead(self):
        """Test TransactionDisputeRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
