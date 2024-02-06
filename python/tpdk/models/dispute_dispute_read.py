# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.172
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from tpdk.models.metadata_dispute_read import MetadataDisputeRead
from tpdk.models.parcel_dispute_read import ParcelDisputeRead
from tpdk.models.transaction_dispute_read import TransactionDisputeRead
from tpdk.models.view_dispute_read import ViewDisputeRead
from tpdk.models.workflow_event_dispute_read import WorkflowEventDisputeRead
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DisputeDisputeRead(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.
    """ # noqa: E501
    ulid: StrictStr
    transaction: Optional[TransactionDisputeRead] = None
    status: StrictStr
    redirect_url: Optional[StrictStr] = Field(default=None, description="Fill-in that field IF you intend to redirect your customer instead of using a WebView.", alias="redirectUrl")
    item_count: Optional[StrictInt] = Field(default=None, description="The dispute may concern only PART of the package. Specify it there.", alias="itemCount")
    issue_type: Optional[StrictStr] = Field(default=None, alias="issueType")
    issue_in_description_type: Optional[StrictStr] = Field(default=None, description="To be set only in conjunction of issueType = NOT_AS_DESCRIBED.", alias="issueInDescriptionType")
    issue_mentioned_in_offer: Optional[StrictBool] = Field(default=None, alias="issueMentionedInOffer")
    issue_details: Optional[StrictStr] = Field(default=None, alias="issueDetails")
    complainant_truthfulness_score: StrictInt = Field(alias="complainantTruthfulnessScore")
    seller_truthfulness_score: StrictInt = Field(alias="sellerTruthfulnessScore")
    complainant_stake: Optional[StrictStr] = Field(default=None, alias="complainantStake")
    inferred_stake: Optional[StrictStr] = Field(default=None, alias="inferredStake")
    recommended_solution: Optional[StrictStr] = Field(default=None, alias="recommendedSolution")
    recommended_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="recommendedPartialRefundAmount")
    chosen_solution: Optional[StrictStr] = Field(default=None, alias="chosenSolution")
    chosen_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="chosenPartialRefundAmount")
    counter_solution: Optional[StrictStr] = Field(default=None, alias="counterSolution")
    counter_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="counterPartialRefundAmount")
    seller_notes: Optional[StrictStr] = Field(default=None, alias="sellerNotes")
    seller_rejection_reason: Optional[StrictStr] = Field(default=None, alias="sellerRejectionReason")
    complainant_approval: Optional[StrictBool] = Field(default=None, alias="complainantApproval")
    seller_approval: Optional[StrictBool] = Field(default=None, alias="sellerApproval")
    platform_solution: Optional[StrictStr] = Field(default=None, alias="platformSolution")
    platform_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="platformPartialRefundAmount")
    platform_approval: Optional[StrictBool] = Field(default=None, alias="platformApproval")
    platform_actor_type: Optional[StrictStr] = Field(default=None, alias="platformActorType")
    platform_reasoning: Optional[StrictStr] = Field(default=None, description="Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care.", alias="platformReasoning")
    arbitration_by: Optional[StrictStr] = Field(default=None, alias="arbitrationBy")
    parcels: List[ParcelDisputeRead]
    views: List[ViewDisputeRead]
    metadata: List[MetadataDisputeRead]
    events: Optional[List[WorkflowEventDisputeRead]] = None
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    view_count: Optional[StrictInt] = Field(default=None, alias="viewCount")
    status_expiration: Optional[datetime] = Field(default=None, description="Yield if eligible the date-time at which the dispute state expire.", alias="statusExpiration")
    awaited_party: Optional[StrictStr] = Field(default=None, description="Determine who is awaited (actor) for the next transition", alias="awaitedParty")
    iri: Optional[StrictStr] = None
    message_count: Optional[StrictInt] = Field(default=None, alias="messageCount")
    closed_in_favor_of: Optional[StrictStr] = Field(default=None, description="Determine who won the case, if not specified, then it is ongoing.", alias="closedInFavorOf")
    disbursed_by_buyer: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total amount disbursed by the buyer to acquire the item.", alias="disbursedByBuyer")
    max_refundable_for_buyer: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="How much the buyer can actually receive back in case of a full refund.", alias="maxRefundableForBuyer")
    __properties: ClassVar[List[str]] = ["ulid", "transaction", "status", "redirectUrl", "itemCount", "issueType", "issueInDescriptionType", "issueMentionedInOffer", "issueDetails", "complainantTruthfulnessScore", "sellerTruthfulnessScore", "complainantStake", "inferredStake", "recommendedSolution", "recommendedPartialRefundAmount", "chosenSolution", "chosenPartialRefundAmount", "counterSolution", "counterPartialRefundAmount", "sellerNotes", "sellerRejectionReason", "complainantApproval", "sellerApproval", "platformSolution", "platformPartialRefundAmount", "platformApproval", "platformActorType", "platformReasoning", "arbitrationBy", "parcels", "views", "metadata", "events", "createdAt", "updatedAt", "viewCount", "statusExpiration", "awaitedParty", "iri", "messageCount", "closedInFavorOf", "disbursedByBuyer", "maxRefundableForBuyer"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CREATED', 'SUBMITTED', 'OPENED', 'ABANDONED', 'OBJECTED', 'PENDING_SHIPMENT', 'SHIPPED', 'IN_TRANSIT', 'RETURNED', 'DISMISSED', 'RESOLVED', 'PENDING'):
            raise ValueError("must be one of enum values ('CREATED', 'SUBMITTED', 'OPENED', 'ABANDONED', 'OBJECTED', 'PENDING_SHIPMENT', 'SHIPPED', 'IN_TRANSIT', 'RETURNED', 'DISMISSED', 'RESOLVED', 'PENDING')")
        return value

    @field_validator('issue_type')
    def issue_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NOT_AS_DESCRIBED', 'DOES_NOT_WORK', 'IS_INCOMPLETE', 'DELIVERY_ISSUE', 'ALLEGED_FRAUD', 'null'):
            raise ValueError("must be one of enum values ('NOT_AS_DESCRIBED', 'DOES_NOT_WORK', 'IS_INCOMPLETE', 'DELIVERY_ISSUE', 'ALLEGED_FRAUD', 'null')")
        return value

    @field_validator('issue_in_description_type')
    def issue_in_description_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('WRONG_COLOUR', 'DAMAGED_OR_USED', 'INCORRECT_FORMAT_OR_SIZE', 'DIFFERENT_MATERIAL', 'null'):
            raise ValueError("must be one of enum values ('WRONG_COLOUR', 'DAMAGED_OR_USED', 'INCORRECT_FORMAT_OR_SIZE', 'DIFFERENT_MATERIAL', 'null')")
        return value

    @field_validator('complainant_stake')
    def complainant_stake_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('LOW', 'MEDIUM', 'HIGH', 'null'):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH', 'null')")
        return value

    @field_validator('inferred_stake')
    def inferred_stake_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('LOW', 'MEDIUM', 'HIGH', 'null'):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH', 'null')")
        return value

    @field_validator('recommended_solution')
    def recommended_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @field_validator('chosen_solution')
    def chosen_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @field_validator('counter_solution')
    def counter_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @field_validator('seller_rejection_reason')
    def seller_rejection_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('UNJUSTIFIED_REQUEST', 'ABUSIVE_REQUEST', 'FRAUD_ATTEMPT', 'OTHER', 'null'):
            raise ValueError("must be one of enum values ('UNJUSTIFIED_REQUEST', 'ABUSIVE_REQUEST', 'FRAUD_ATTEMPT', 'OTHER', 'null')")
        return value

    @field_validator('platform_solution')
    def platform_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @field_validator('platform_actor_type')
    def platform_actor_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('RULING', 'AI', 'CUSTOMER_CARE', 'PLATFORM_SUPPORT', 'null'):
            raise ValueError("must be one of enum values ('RULING', 'AI', 'CUSTOMER_CARE', 'PLATFORM_SUPPORT', 'null')")
        return value

    @field_validator('awaited_party')
    def awaited_party_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BUYER', 'PLATFORM', 'SELLER'):
            raise ValueError("must be one of enum values ('BUYER', 'PLATFORM', 'SELLER')")
        return value

    @field_validator('closed_in_favor_of')
    def closed_in_favor_of_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BUYER', 'SELLER'):
            raise ValueError("must be one of enum values ('BUYER', 'SELLER')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DisputeDisputeRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "updated_at",
                "view_count",
                "status_expiration",
                "awaited_party",
                "iri",
                "message_count",
                "closed_in_favor_of",
                "disbursed_by_buyer",
                "max_refundable_for_buyer",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in parcels (list)
        _items = []
        if self.parcels:
            for _item in self.parcels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parcels'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item in self.views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['views'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        # set to None if redirect_url (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_url is None and "redirect_url" in self.model_fields_set:
            _dict['redirectUrl'] = None

        # set to None if item_count (nullable) is None
        # and model_fields_set contains the field
        if self.item_count is None and "item_count" in self.model_fields_set:
            _dict['itemCount'] = None

        # set to None if issue_type (nullable) is None
        # and model_fields_set contains the field
        if self.issue_type is None and "issue_type" in self.model_fields_set:
            _dict['issueType'] = None

        # set to None if issue_in_description_type (nullable) is None
        # and model_fields_set contains the field
        if self.issue_in_description_type is None and "issue_in_description_type" in self.model_fields_set:
            _dict['issueInDescriptionType'] = None

        # set to None if issue_mentioned_in_offer (nullable) is None
        # and model_fields_set contains the field
        if self.issue_mentioned_in_offer is None and "issue_mentioned_in_offer" in self.model_fields_set:
            _dict['issueMentionedInOffer'] = None

        # set to None if issue_details (nullable) is None
        # and model_fields_set contains the field
        if self.issue_details is None and "issue_details" in self.model_fields_set:
            _dict['issueDetails'] = None

        # set to None if complainant_stake (nullable) is None
        # and model_fields_set contains the field
        if self.complainant_stake is None and "complainant_stake" in self.model_fields_set:
            _dict['complainantStake'] = None

        # set to None if inferred_stake (nullable) is None
        # and model_fields_set contains the field
        if self.inferred_stake is None and "inferred_stake" in self.model_fields_set:
            _dict['inferredStake'] = None

        # set to None if recommended_solution (nullable) is None
        # and model_fields_set contains the field
        if self.recommended_solution is None and "recommended_solution" in self.model_fields_set:
            _dict['recommendedSolution'] = None

        # set to None if recommended_partial_refund_amount (nullable) is None
        # and model_fields_set contains the field
        if self.recommended_partial_refund_amount is None and "recommended_partial_refund_amount" in self.model_fields_set:
            _dict['recommendedPartialRefundAmount'] = None

        # set to None if chosen_solution (nullable) is None
        # and model_fields_set contains the field
        if self.chosen_solution is None and "chosen_solution" in self.model_fields_set:
            _dict['chosenSolution'] = None

        # set to None if chosen_partial_refund_amount (nullable) is None
        # and model_fields_set contains the field
        if self.chosen_partial_refund_amount is None and "chosen_partial_refund_amount" in self.model_fields_set:
            _dict['chosenPartialRefundAmount'] = None

        # set to None if counter_solution (nullable) is None
        # and model_fields_set contains the field
        if self.counter_solution is None and "counter_solution" in self.model_fields_set:
            _dict['counterSolution'] = None

        # set to None if counter_partial_refund_amount (nullable) is None
        # and model_fields_set contains the field
        if self.counter_partial_refund_amount is None and "counter_partial_refund_amount" in self.model_fields_set:
            _dict['counterPartialRefundAmount'] = None

        # set to None if seller_notes (nullable) is None
        # and model_fields_set contains the field
        if self.seller_notes is None and "seller_notes" in self.model_fields_set:
            _dict['sellerNotes'] = None

        # set to None if seller_rejection_reason (nullable) is None
        # and model_fields_set contains the field
        if self.seller_rejection_reason is None and "seller_rejection_reason" in self.model_fields_set:
            _dict['sellerRejectionReason'] = None

        # set to None if complainant_approval (nullable) is None
        # and model_fields_set contains the field
        if self.complainant_approval is None and "complainant_approval" in self.model_fields_set:
            _dict['complainantApproval'] = None

        # set to None if seller_approval (nullable) is None
        # and model_fields_set contains the field
        if self.seller_approval is None and "seller_approval" in self.model_fields_set:
            _dict['sellerApproval'] = None

        # set to None if platform_solution (nullable) is None
        # and model_fields_set contains the field
        if self.platform_solution is None and "platform_solution" in self.model_fields_set:
            _dict['platformSolution'] = None

        # set to None if platform_partial_refund_amount (nullable) is None
        # and model_fields_set contains the field
        if self.platform_partial_refund_amount is None and "platform_partial_refund_amount" in self.model_fields_set:
            _dict['platformPartialRefundAmount'] = None

        # set to None if platform_approval (nullable) is None
        # and model_fields_set contains the field
        if self.platform_approval is None and "platform_approval" in self.model_fields_set:
            _dict['platformApproval'] = None

        # set to None if platform_actor_type (nullable) is None
        # and model_fields_set contains the field
        if self.platform_actor_type is None and "platform_actor_type" in self.model_fields_set:
            _dict['platformActorType'] = None

        # set to None if platform_reasoning (nullable) is None
        # and model_fields_set contains the field
        if self.platform_reasoning is None and "platform_reasoning" in self.model_fields_set:
            _dict['platformReasoning'] = None

        # set to None if arbitration_by (nullable) is None
        # and model_fields_set contains the field
        if self.arbitration_by is None and "arbitration_by" in self.model_fields_set:
            _dict['arbitrationBy'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updatedAt'] = None

        # set to None if status_expiration (nullable) is None
        # and model_fields_set contains the field
        if self.status_expiration is None and "status_expiration" in self.model_fields_set:
            _dict['statusExpiration'] = None

        # set to None if disbursed_by_buyer (nullable) is None
        # and model_fields_set contains the field
        if self.disbursed_by_buyer is None and "disbursed_by_buyer" in self.model_fields_set:
            _dict['disbursedByBuyer'] = None

        # set to None if max_refundable_for_buyer (nullable) is None
        # and model_fields_set contains the field
        if self.max_refundable_for_buyer is None and "max_refundable_for_buyer" in self.model_fields_set:
            _dict['maxRefundableForBuyer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DisputeDisputeRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ulid": obj.get("ulid"),
            "transaction": TransactionDisputeRead.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None,
            "status": obj.get("status") if obj.get("status") is not None else 'CREATED',
            "redirectUrl": obj.get("redirectUrl"),
            "itemCount": obj.get("itemCount"),
            "issueType": obj.get("issueType"),
            "issueInDescriptionType": obj.get("issueInDescriptionType"),
            "issueMentionedInOffer": obj.get("issueMentionedInOffer"),
            "issueDetails": obj.get("issueDetails"),
            "complainantTruthfulnessScore": obj.get("complainantTruthfulnessScore") if obj.get("complainantTruthfulnessScore") is not None else 100,
            "sellerTruthfulnessScore": obj.get("sellerTruthfulnessScore") if obj.get("sellerTruthfulnessScore") is not None else 100,
            "complainantStake": obj.get("complainantStake"),
            "inferredStake": obj.get("inferredStake"),
            "recommendedSolution": obj.get("recommendedSolution"),
            "recommendedPartialRefundAmount": obj.get("recommendedPartialRefundAmount"),
            "chosenSolution": obj.get("chosenSolution"),
            "chosenPartialRefundAmount": obj.get("chosenPartialRefundAmount"),
            "counterSolution": obj.get("counterSolution"),
            "counterPartialRefundAmount": obj.get("counterPartialRefundAmount"),
            "sellerNotes": obj.get("sellerNotes"),
            "sellerRejectionReason": obj.get("sellerRejectionReason"),
            "complainantApproval": obj.get("complainantApproval"),
            "sellerApproval": obj.get("sellerApproval"),
            "platformSolution": obj.get("platformSolution"),
            "platformPartialRefundAmount": obj.get("platformPartialRefundAmount"),
            "platformApproval": obj.get("platformApproval"),
            "platformActorType": obj.get("platformActorType"),
            "platformReasoning": obj.get("platformReasoning"),
            "arbitrationBy": obj.get("arbitrationBy"),
            "parcels": [ParcelDisputeRead.from_dict(_item) for _item in obj.get("parcels")] if obj.get("parcels") is not None else None,
            "views": [ViewDisputeRead.from_dict(_item) for _item in obj.get("views")] if obj.get("views") is not None else None,
            "metadata": [MetadataDisputeRead.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None,
            "events": [WorkflowEventDisputeRead.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "viewCount": obj.get("viewCount"),
            "statusExpiration": obj.get("statusExpiration"),
            "awaitedParty": obj.get("awaitedParty"),
            "iri": obj.get("iri"),
            "messageCount": obj.get("messageCount"),
            "closedInFavorOf": obj.get("closedInFavorOf"),
            "disbursedByBuyer": obj.get("disbursedByBuyer"),
            "maxRefundableForBuyer": obj.get("maxRefundableForBuyer")
        })
        return _obj


