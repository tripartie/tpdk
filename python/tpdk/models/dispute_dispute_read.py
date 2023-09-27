# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.75
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist, validator
from tpdk.models.metadata_dispute_read import MetadataDisputeRead
from tpdk.models.parcel_dispute_read import ParcelDisputeRead
from tpdk.models.transaction_dispute_read import TransactionDisputeRead
from tpdk.models.workflow_event_dispute_read import WorkflowEventDisputeRead

class DisputeDisputeRead(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.  # noqa: E501
    """
    ulid: StrictStr = Field(...)
    transaction: Optional[TransactionDisputeRead] = None
    status: StrictStr = Field(...)
    redirect_url: Optional[StrictStr] = Field(None, alias="redirectUrl", description="Fill-in that field IF you intend to redirect your customer instead of using a WebView.")
    item_count: Optional[StrictInt] = Field(None, alias="itemCount", description="The dispute may concern only PART of the package. Specify it there.")
    issue_type: Optional[StrictStr] = Field(None, alias="issueType")
    issue_in_description_type: Optional[StrictStr] = Field(None, alias="issueInDescriptionType", description="To be set only in conjunction of issueType = NOT_AS_DESCRIBED.")
    issue_mentioned_in_offer: Optional[StrictBool] = Field(None, alias="issueMentionedInOffer")
    issue_details: Optional[StrictStr] = Field(None, alias="issueDetails")
    complainant_truthfulness_score: StrictInt = Field(..., alias="complainantTruthfulnessScore")
    seller_truthfulness_score: StrictInt = Field(..., alias="sellerTruthfulnessScore")
    complainant_stake: Optional[StrictStr] = Field(None, alias="complainantStake")
    inferred_stake: Optional[StrictStr] = Field(None, alias="inferredStake")
    recommended_solution: Optional[StrictStr] = Field(None, alias="recommendedSolution")
    recommended_partial_refund_amount: Optional[StrictInt] = Field(None, alias="recommendedPartialRefundAmount")
    chosen_solution: Optional[StrictStr] = Field(None, alias="chosenSolution")
    chosen_partial_refund_amount: Optional[StrictInt] = Field(None, alias="chosenPartialRefundAmount")
    counter_solution: Optional[StrictStr] = Field(None, alias="counterSolution")
    counter_partial_refund_amount: Optional[StrictInt] = Field(None, alias="counterPartialRefundAmount")
    complainant_approval: Optional[StrictBool] = Field(None, alias="complainantApproval")
    seller_approval: Optional[StrictBool] = Field(None, alias="sellerApproval")
    platform_solution: Optional[StrictStr] = Field(None, alias="platformSolution")
    platform_partial_refund_amount: Optional[conint(strict=True, gt=0)] = Field(None, alias="platformPartialRefundAmount")
    platform_approval: Optional[StrictBool] = Field(None, alias="platformApproval")
    arbitration_by: Optional[StrictStr] = Field(None, alias="arbitrationBy")
    parcels: conlist(ParcelDisputeRead) = Field(...)
    metadata: conlist(MetadataDisputeRead) = Field(...)
    events: Optional[conlist(WorkflowEventDisputeRead)] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    status_expiration: Optional[datetime] = Field(None, alias="statusExpiration", description="Yield if eligible the date-time at which the dispute state expire.")
    awaited_party: Optional[StrictStr] = Field(None, alias="awaitedParty", description="Determine who is awaited (actor) for the next transition")
    iri: Optional[StrictStr] = None
    message_count: Optional[StrictInt] = Field(None, alias="messageCount")
    __properties = ["ulid", "transaction", "status", "redirectUrl", "itemCount", "issueType", "issueInDescriptionType", "issueMentionedInOffer", "issueDetails", "complainantTruthfulnessScore", "sellerTruthfulnessScore", "complainantStake", "inferredStake", "recommendedSolution", "recommendedPartialRefundAmount", "chosenSolution", "chosenPartialRefundAmount", "counterSolution", "counterPartialRefundAmount", "complainantApproval", "sellerApproval", "platformSolution", "platformPartialRefundAmount", "platformApproval", "arbitrationBy", "parcels", "metadata", "events", "createdAt", "updatedAt", "statusExpiration", "awaitedParty", "iri", "messageCount"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CREATED', 'SUBMITTED', 'OPENED', 'ABANDONED', 'OBJECTED', 'PENDING_SHIPMENT', 'SHIPPED', 'IN_TRANSIT', 'RETURNED', 'DISMISSED', 'RESOLVED', 'PENDING'):
            raise ValueError("must be one of enum values ('CREATED', 'SUBMITTED', 'OPENED', 'ABANDONED', 'OBJECTED', 'PENDING_SHIPMENT', 'SHIPPED', 'IN_TRANSIT', 'RETURNED', 'DISMISSED', 'RESOLVED', 'PENDING')")
        return value

    @validator('issue_type')
    def issue_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NOT_AS_DESCRIBED', 'DOES_NOT_WORK', 'IS_INCOMPLETE', 'DELIVERY_ISSUE', 'ALLEGED_FRAUD', 'null'):
            raise ValueError("must be one of enum values ('NOT_AS_DESCRIBED', 'DOES_NOT_WORK', 'IS_INCOMPLETE', 'DELIVERY_ISSUE', 'ALLEGED_FRAUD', 'null')")
        return value

    @validator('issue_in_description_type')
    def issue_in_description_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('WRONG_COLOUR', 'DAMAGED_OR_USED', 'INCORRECT_FORMAT_OR_SIZE', 'DIFFERENT_MATERIAL', 'null'):
            raise ValueError("must be one of enum values ('WRONG_COLOUR', 'DAMAGED_OR_USED', 'INCORRECT_FORMAT_OR_SIZE', 'DIFFERENT_MATERIAL', 'null')")
        return value

    @validator('complainant_stake')
    def complainant_stake_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('LOW', 'MEDIUM', 'HIGH', 'null'):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH', 'null')")
        return value

    @validator('inferred_stake')
    def inferred_stake_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('LOW', 'MEDIUM', 'HIGH', 'null'):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH', 'null')")
        return value

    @validator('recommended_solution')
    def recommended_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @validator('chosen_solution')
    def chosen_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @validator('counter_solution')
    def counter_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @validator('platform_solution')
    def platform_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @validator('awaited_party')
    def awaited_party_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BUYER', 'PLATFORM', 'SELLER'):
            raise ValueError("must be one of enum values ('BUYER', 'PLATFORM', 'SELLER')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DisputeDisputeRead:
        """Create an instance of DisputeDisputeRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "events",
                            "created_at",
                            "updated_at",
                            "status_expiration",
                            "awaited_party",
                            "iri",
                            "message_count",
                          },
                          exclude_none=True)
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
        # and __fields_set__ contains the field
        if self.redirect_url is None and "redirect_url" in self.__fields_set__:
            _dict['redirectUrl'] = None

        # set to None if item_count (nullable) is None
        # and __fields_set__ contains the field
        if self.item_count is None and "item_count" in self.__fields_set__:
            _dict['itemCount'] = None

        # set to None if issue_type (nullable) is None
        # and __fields_set__ contains the field
        if self.issue_type is None and "issue_type" in self.__fields_set__:
            _dict['issueType'] = None

        # set to None if issue_in_description_type (nullable) is None
        # and __fields_set__ contains the field
        if self.issue_in_description_type is None and "issue_in_description_type" in self.__fields_set__:
            _dict['issueInDescriptionType'] = None

        # set to None if issue_mentioned_in_offer (nullable) is None
        # and __fields_set__ contains the field
        if self.issue_mentioned_in_offer is None and "issue_mentioned_in_offer" in self.__fields_set__:
            _dict['issueMentionedInOffer'] = None

        # set to None if issue_details (nullable) is None
        # and __fields_set__ contains the field
        if self.issue_details is None and "issue_details" in self.__fields_set__:
            _dict['issueDetails'] = None

        # set to None if complainant_stake (nullable) is None
        # and __fields_set__ contains the field
        if self.complainant_stake is None and "complainant_stake" in self.__fields_set__:
            _dict['complainantStake'] = None

        # set to None if inferred_stake (nullable) is None
        # and __fields_set__ contains the field
        if self.inferred_stake is None and "inferred_stake" in self.__fields_set__:
            _dict['inferredStake'] = None

        # set to None if recommended_solution (nullable) is None
        # and __fields_set__ contains the field
        if self.recommended_solution is None and "recommended_solution" in self.__fields_set__:
            _dict['recommendedSolution'] = None

        # set to None if recommended_partial_refund_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.recommended_partial_refund_amount is None and "recommended_partial_refund_amount" in self.__fields_set__:
            _dict['recommendedPartialRefundAmount'] = None

        # set to None if chosen_solution (nullable) is None
        # and __fields_set__ contains the field
        if self.chosen_solution is None and "chosen_solution" in self.__fields_set__:
            _dict['chosenSolution'] = None

        # set to None if chosen_partial_refund_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.chosen_partial_refund_amount is None and "chosen_partial_refund_amount" in self.__fields_set__:
            _dict['chosenPartialRefundAmount'] = None

        # set to None if counter_solution (nullable) is None
        # and __fields_set__ contains the field
        if self.counter_solution is None and "counter_solution" in self.__fields_set__:
            _dict['counterSolution'] = None

        # set to None if counter_partial_refund_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.counter_partial_refund_amount is None and "counter_partial_refund_amount" in self.__fields_set__:
            _dict['counterPartialRefundAmount'] = None

        # set to None if complainant_approval (nullable) is None
        # and __fields_set__ contains the field
        if self.complainant_approval is None and "complainant_approval" in self.__fields_set__:
            _dict['complainantApproval'] = None

        # set to None if seller_approval (nullable) is None
        # and __fields_set__ contains the field
        if self.seller_approval is None and "seller_approval" in self.__fields_set__:
            _dict['sellerApproval'] = None

        # set to None if platform_solution (nullable) is None
        # and __fields_set__ contains the field
        if self.platform_solution is None and "platform_solution" in self.__fields_set__:
            _dict['platformSolution'] = None

        # set to None if platform_partial_refund_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.platform_partial_refund_amount is None and "platform_partial_refund_amount" in self.__fields_set__:
            _dict['platformPartialRefundAmount'] = None

        # set to None if platform_approval (nullable) is None
        # and __fields_set__ contains the field
        if self.platform_approval is None and "platform_approval" in self.__fields_set__:
            _dict['platformApproval'] = None

        # set to None if arbitration_by (nullable) is None
        # and __fields_set__ contains the field
        if self.arbitration_by is None and "arbitration_by" in self.__fields_set__:
            _dict['arbitrationBy'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        # set to None if status_expiration (nullable) is None
        # and __fields_set__ contains the field
        if self.status_expiration is None and "status_expiration" in self.__fields_set__:
            _dict['statusExpiration'] = None

        # set to None if awaited_party (nullable) is None
        # and __fields_set__ contains the field
        if self.awaited_party is None and "awaited_party" in self.__fields_set__:
            _dict['awaitedParty'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DisputeDisputeRead:
        """Create an instance of DisputeDisputeRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DisputeDisputeRead.parse_obj(obj)

        _obj = DisputeDisputeRead.parse_obj({
            "ulid": obj.get("ulid"),
            "transaction": TransactionDisputeRead.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None,
            "status": obj.get("status") if obj.get("status") is not None else 'CREATED',
            "redirect_url": obj.get("redirectUrl"),
            "item_count": obj.get("itemCount"),
            "issue_type": obj.get("issueType"),
            "issue_in_description_type": obj.get("issueInDescriptionType"),
            "issue_mentioned_in_offer": obj.get("issueMentionedInOffer"),
            "issue_details": obj.get("issueDetails"),
            "complainant_truthfulness_score": obj.get("complainantTruthfulnessScore") if obj.get("complainantTruthfulnessScore") is not None else 100,
            "seller_truthfulness_score": obj.get("sellerTruthfulnessScore") if obj.get("sellerTruthfulnessScore") is not None else 100,
            "complainant_stake": obj.get("complainantStake"),
            "inferred_stake": obj.get("inferredStake"),
            "recommended_solution": obj.get("recommendedSolution"),
            "recommended_partial_refund_amount": obj.get("recommendedPartialRefundAmount"),
            "chosen_solution": obj.get("chosenSolution"),
            "chosen_partial_refund_amount": obj.get("chosenPartialRefundAmount"),
            "counter_solution": obj.get("counterSolution"),
            "counter_partial_refund_amount": obj.get("counterPartialRefundAmount"),
            "complainant_approval": obj.get("complainantApproval"),
            "seller_approval": obj.get("sellerApproval"),
            "platform_solution": obj.get("platformSolution"),
            "platform_partial_refund_amount": obj.get("platformPartialRefundAmount"),
            "platform_approval": obj.get("platformApproval"),
            "arbitration_by": obj.get("arbitrationBy"),
            "parcels": [ParcelDisputeRead.from_dict(_item) for _item in obj.get("parcels")] if obj.get("parcels") is not None else None,
            "metadata": [MetadataDisputeRead.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None,
            "events": [WorkflowEventDisputeRead.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "status_expiration": obj.get("statusExpiration"),
            "awaited_party": obj.get("awaitedParty"),
            "iri": obj.get("iri"),
            "message_count": obj.get("messageCount")
        })
        return _obj


