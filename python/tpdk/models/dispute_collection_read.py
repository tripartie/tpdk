# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.167
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from tpdk.models.transaction_collection_read import TransactionCollectionRead
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DisputeCollectionRead(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.
    """ # noqa: E501
    ulid: StrictStr
    transaction: Optional[TransactionCollectionRead] = None
    status: StrictStr
    item_count: Optional[StrictInt] = Field(default=None, description="The dispute may concern only PART of the package. Specify it there.", alias="itemCount")
    issue_type: Optional[StrictStr] = Field(default=None, alias="issueType")
    issue_in_description_type: Optional[StrictStr] = Field(default=None, description="To be set only in conjunction of issueType = NOT_AS_DESCRIBED.", alias="issueInDescriptionType")
    issue_mentioned_in_offer: Optional[StrictBool] = Field(default=None, alias="issueMentionedInOffer")
    complainant_stake: Optional[StrictStr] = Field(default=None, alias="complainantStake")
    inferred_stake: Optional[StrictStr] = Field(default=None, alias="inferredStake")
    chosen_solution: Optional[StrictStr] = Field(default=None, alias="chosenSolution")
    chosen_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="chosenPartialRefundAmount")
    platform_solution: Optional[StrictStr] = Field(default=None, alias="platformSolution")
    platform_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="platformPartialRefundAmount")
    platform_approval: Optional[StrictBool] = Field(default=None, alias="platformApproval")
    platform_actor_type: Optional[StrictStr] = Field(default=None, alias="platformActorType")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    status_expiration: Optional[datetime] = Field(default=None, description="Yield if eligible the date-time at which the dispute state expire.", alias="statusExpiration")
    awaited_party: Optional[StrictStr] = Field(default=None, description="Determine who is awaited (actor) for the next transition", alias="awaitedParty")
    iri: Optional[StrictStr] = None
    message_count: Optional[StrictInt] = Field(default=None, alias="messageCount")
    closed_in_favor_of: Optional[StrictStr] = Field(default=None, description="Determine who won the case, if not specified, then it is ongoing.", alias="closedInFavorOf")
    __properties: ClassVar[List[str]] = ["ulid", "transaction", "status", "itemCount", "issueType", "issueInDescriptionType", "issueMentionedInOffer", "complainantStake", "inferredStake", "chosenSolution", "chosenPartialRefundAmount", "platformSolution", "platformPartialRefundAmount", "platformApproval", "platformActorType", "createdAt", "updatedAt", "statusExpiration", "awaitedParty", "iri", "messageCount", "closedInFavorOf"]

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

    @field_validator('chosen_solution')
    def chosen_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null'):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
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
        """Create an instance of DisputeCollectionRead from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "updated_at",
                "status_expiration",
                "awaited_party",
                "iri",
                "message_count",
                "closed_in_favor_of",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
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

        # set to None if complainant_stake (nullable) is None
        # and model_fields_set contains the field
        if self.complainant_stake is None and "complainant_stake" in self.model_fields_set:
            _dict['complainantStake'] = None

        # set to None if inferred_stake (nullable) is None
        # and model_fields_set contains the field
        if self.inferred_stake is None and "inferred_stake" in self.model_fields_set:
            _dict['inferredStake'] = None

        # set to None if chosen_solution (nullable) is None
        # and model_fields_set contains the field
        if self.chosen_solution is None and "chosen_solution" in self.model_fields_set:
            _dict['chosenSolution'] = None

        # set to None if chosen_partial_refund_amount (nullable) is None
        # and model_fields_set contains the field
        if self.chosen_partial_refund_amount is None and "chosen_partial_refund_amount" in self.model_fields_set:
            _dict['chosenPartialRefundAmount'] = None

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

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updatedAt'] = None

        # set to None if status_expiration (nullable) is None
        # and model_fields_set contains the field
        if self.status_expiration is None and "status_expiration" in self.model_fields_set:
            _dict['statusExpiration'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DisputeCollectionRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ulid": obj.get("ulid"),
            "transaction": TransactionCollectionRead.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None,
            "status": obj.get("status") if obj.get("status") is not None else 'CREATED',
            "itemCount": obj.get("itemCount"),
            "issueType": obj.get("issueType"),
            "issueInDescriptionType": obj.get("issueInDescriptionType"),
            "issueMentionedInOffer": obj.get("issueMentionedInOffer"),
            "complainantStake": obj.get("complainantStake"),
            "inferredStake": obj.get("inferredStake"),
            "chosenSolution": obj.get("chosenSolution"),
            "chosenPartialRefundAmount": obj.get("chosenPartialRefundAmount"),
            "platformSolution": obj.get("platformSolution"),
            "platformPartialRefundAmount": obj.get("platformPartialRefundAmount"),
            "platformApproval": obj.get("platformApproval"),
            "platformActorType": obj.get("platformActorType"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "statusExpiration": obj.get("statusExpiration"),
            "awaitedParty": obj.get("awaitedParty"),
            "iri": obj.get("iri"),
            "messageCount": obj.get("messageCount"),
            "closedInFavorOf": obj.get("closedInFavorOf")
        })
        return _obj


