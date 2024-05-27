# coding: utf-8

# flake8: noqa
"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.204
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from tpdk.models.access_error import AccessError
from tpdk.models.address import Address
from tpdk.models.api_client_post_creation_read import ApiClientPostCreationRead
from tpdk.models.api_client_read import ApiClientRead
from tpdk.models.api_client_write import ApiClientWrite
from tpdk.models.auth_error import AuthError
from tpdk.models.dispute_address_independent_write import DisputeAddressIndependentWrite
from tpdk.models.dispute_collection_read import DisputeCollectionRead
from tpdk.models.dispute_dispute_read import DisputeDisputeRead
from tpdk.models.dispute_independent_write import DisputeIndependentWrite
from tpdk.models.dispute_media_read import DisputeMediaRead
from tpdk.models.dispute_metadata_independent_write import DisputeMetadataIndependentWrite
from tpdk.models.dispute_metadata_read import DisputeMetadataRead
from tpdk.models.dispute_offer_collection_read import DisputeOfferCollectionRead
from tpdk.models.dispute_offer_independent_write import DisputeOfferIndependentWrite
from tpdk.models.dispute_offer_read import DisputeOfferRead
from tpdk.models.dispute_organization_read import DisputeOrganizationRead
from tpdk.models.dispute_parcel_independent_write import DisputeParcelIndependentWrite
from tpdk.models.dispute_parcel_read import DisputeParcelRead
from tpdk.models.dispute_persona_collection_read import DisputePersonaCollectionRead
from tpdk.models.dispute_persona_independent_write import DisputePersonaIndependentWrite
from tpdk.models.dispute_persona_read import DisputePersonaRead
from tpdk.models.dispute_post_creation_read import DisputePostCreationRead
from tpdk.models.dispute_read import DisputeRead
from tpdk.models.dispute_transaction_collection_read import DisputeTransactionCollectionRead
from tpdk.models.dispute_transaction_independent_write import DisputeTransactionIndependentWrite
from tpdk.models.dispute_transaction_read import DisputeTransactionRead
from tpdk.models.dispute_update import DisputeUpdate
from tpdk.models.dispute_view_read import DisputeViewRead
from tpdk.models.dispute_workflow_event_read import DisputeWorkflowEventRead
from tpdk.models.evaluation_read import EvaluationRead
from tpdk.models.evaluation_write import EvaluationWrite
from tpdk.models.evidence import Evidence
from tpdk.models.evidence_media_read import EvidenceMediaRead
from tpdk.models.evidence_read import EvidenceRead
from tpdk.models.evidence_write import EvidenceWrite
from tpdk.models.generic_error import GenericError
from tpdk.models.invalid_query_error import InvalidQueryError
from tpdk.models.media import Media
from tpdk.models.media_dispute_read import MediaDisputeRead
from tpdk.models.media_read import MediaRead
from tpdk.models.media_user_read import MediaUserRead
from tpdk.models.message_error import MessageError
from tpdk.models.metadata import Metadata
from tpdk.models.metadata_dispute_read import MetadataDisputeRead
from tpdk.models.not_found_error import NotFoundError
from tpdk.models.notification_read import NotificationRead
from tpdk.models.notification_update import NotificationUpdate
from tpdk.models.offer_dispute_read import OfferDisputeRead
from tpdk.models.organization_address_update import OrganizationAddressUpdate
from tpdk.models.organization_collection_read import OrganizationCollectionRead
from tpdk.models.organization_dispute_read import OrganizationDisputeRead
from tpdk.models.organization_media_collection_read import OrganizationMediaCollectionRead
from tpdk.models.organization_media_read import OrganizationMediaRead
from tpdk.models.organization_read import OrganizationRead
from tpdk.models.organization_update import OrganizationUpdate
from tpdk.models.organization_user_read import OrganizationUserRead
from tpdk.models.parcel import Parcel
from tpdk.models.parcel_dispute_read import ParcelDisputeRead
from tpdk.models.parcel_write import ParcelWrite
from tpdk.models.persona import Persona
from tpdk.models.persona_address_read import PersonaAddressRead
from tpdk.models.persona_address_update import PersonaAddressUpdate
from tpdk.models.persona_address_write import PersonaAddressWrite
from tpdk.models.persona_auth_return import PersonaAuthReturn
from tpdk.models.persona_collection_read import PersonaCollectionRead
from tpdk.models.persona_dispute_read import PersonaDisputeRead
from tpdk.models.persona_external_auth import PersonaExternalAuth
from tpdk.models.persona_metadata_read import PersonaMetadataRead
from tpdk.models.persona_metadata_update import PersonaMetadataUpdate
from tpdk.models.persona_metadata_write import PersonaMetadataWrite
from tpdk.models.persona_post_auth_read import PersonaPostAuthRead
from tpdk.models.persona_read import PersonaRead
from tpdk.models.persona_register import PersonaRegister
from tpdk.models.persona_token_write import PersonaTokenWrite
from tpdk.models.persona_update import PersonaUpdate
from tpdk.models.persona_write import PersonaWrite
from tpdk.models.rate_limit_error import RateLimitError
from tpdk.models.transaction_dispute_read import TransactionDisputeRead
from tpdk.models.unprocessable_entity import UnprocessableEntity
from tpdk.models.unprocessable_entity_violations_inner import UnprocessableEntityViolationsInner
from tpdk.models.user import User
from tpdk.models.user_address_write import UserAddressWrite
from tpdk.models.user_authenticated_read import UserAuthenticatedRead
from tpdk.models.user_collection_read import UserCollectionRead
from tpdk.models.user_email_validation_write import UserEmailValidationWrite
from tpdk.models.user_invite import UserInvite
from tpdk.models.user_jwt_created import UserJwtCreated
from tpdk.models.user_jwt_write import UserJwtWrite
from tpdk.models.user_media_authenticated_read import UserMediaAuthenticatedRead
from tpdk.models.user_media_collection_read import UserMediaCollectionRead
from tpdk.models.user_media_read import UserMediaRead
from tpdk.models.user_organization_authenticated_read import UserOrganizationAuthenticatedRead
from tpdk.models.user_organization_collection_read import UserOrganizationCollectionRead
from tpdk.models.user_organization_read import UserOrganizationRead
from tpdk.models.user_organization_write import UserOrganizationWrite
from tpdk.models.user_post_register_read import UserPostRegisterRead
from tpdk.models.user_totp_setup_read import UserTotpSetupRead
from tpdk.models.user_totp_toggle_write import UserTotpToggleWrite
from tpdk.models.user_update import UserUpdate
from tpdk.models.user_user_email_update import UserUserEmailUpdate
from tpdk.models.user_user_password_update import UserUserPasswordUpdate
from tpdk.models.user_user_read import UserUserRead
from tpdk.models.user_user_subscribed import UserUserSubscribed
from tpdk.models.user_write import UserWrite
from tpdk.models.view import View
from tpdk.models.view_dispute_read import ViewDisputeRead
from tpdk.models.webhook import Webhook
from tpdk.models.webhook_history_collection_read import WebhookHistoryCollectionRead
from tpdk.models.webhook_history_read import WebhookHistoryRead
from tpdk.models.webhook_object import WebhookObject
from tpdk.models.webhook_subscription_read import WebhookSubscriptionRead
from tpdk.models.webhook_subscription_write import WebhookSubscriptionWrite
from tpdk.models.workflow_event_dispute_read import WorkflowEventDisputeRead
