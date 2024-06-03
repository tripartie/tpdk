# coding: utf-8

"""
    Resolution Center

    Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution.

    The version of the OpenAPI document: 2.0.208
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class DisputeUpdate(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.
    """ # noqa: E501
    item_count: Optional[StrictInt] = Field(default=None, description="The dispute may concern only PART of the package. Specify it there.", alias="itemCount")
    issue_type: Optional[StrictStr] = Field(default=None, alias="issueType")
    issue_in_description_type: Optional[StrictStr] = Field(default=None, description="To be set only in conjunction of issueType = NOT_AS_DESCRIBED.", alias="issueInDescriptionType")
    issue_mentioned_in_offer: Optional[StrictBool] = Field(default=None, alias="issueMentionedInOffer")
    issue_details: Optional[Annotated[str, Field(min_length=30, strict=True, max_length=1000)]] = Field(default=None, alias="issueDetails")
    complainant_stake: Optional[StrictStr] = Field(default=None, alias="complainantStake")
    chosen_solution: Optional[StrictStr] = Field(default=None, alias="chosenSolution")
    chosen_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="chosenPartialRefundAmount")
    counter_solution: Optional[StrictStr] = Field(default=None, alias="counterSolution")
    counter_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="counterPartialRefundAmount")
    seller_notes: Optional[Annotated[str, Field(min_length=30, strict=True, max_length=1000)]] = Field(default=None, alias="sellerNotes")
    seller_rejection_reason: Optional[StrictStr] = Field(default=None, alias="sellerRejectionReason")
    complainant_approval: Optional[StrictBool] = Field(default=None, alias="complainantApproval")
    seller_approval: Optional[StrictBool] = Field(default=None, alias="sellerApproval")
    platform_solution: Optional[StrictStr] = Field(default=None, alias="platformSolution")
    platform_partial_refund_amount: Optional[StrictInt] = Field(default=None, alias="platformPartialRefundAmount")
    platform_approval: Optional[StrictBool] = Field(default=None, alias="platformApproval")
    platform_reasoning: Optional[Annotated[str, Field(min_length=30, strict=True, max_length=1000)]] = Field(default=None, description="Explicit additional information about the platform decision. Could be written by AI, Ruling or Customer Care.", alias="platformReasoning")
    __properties: ClassVar[List[str]] = ["itemCount", "issueType", "issueInDescriptionType", "issueMentionedInOffer", "issueDetails", "complainantStake", "chosenSolution", "chosenPartialRefundAmount", "counterSolution", "counterPartialRefundAmount", "sellerNotes", "sellerRejectionReason", "complainantApproval", "sellerApproval", "platformSolution", "platformPartialRefundAmount", "platformApproval", "platformReasoning"]

    @field_validator('issue_type')
    def issue_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NOT_AS_DESCRIBED', 'DOES_NOT_WORK', 'IS_INCOMPLETE', 'DELIVERY_ISSUE', 'ALLEGED_FRAUD', 'null']):
            raise ValueError("must be one of enum values ('NOT_AS_DESCRIBED', 'DOES_NOT_WORK', 'IS_INCOMPLETE', 'DELIVERY_ISSUE', 'ALLEGED_FRAUD', 'null')")
        return value

    @field_validator('issue_in_description_type')
    def issue_in_description_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['WRONG_COLOUR', 'DAMAGED_OR_USED', 'INCORRECT_FORMAT_OR_SIZE', 'DIFFERENT_MATERIAL', 'null']):
            raise ValueError("must be one of enum values ('WRONG_COLOUR', 'DAMAGED_OR_USED', 'INCORRECT_FORMAT_OR_SIZE', 'DIFFERENT_MATERIAL', 'null')")
        return value

    @field_validator('complainant_stake')
    def complainant_stake_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOW', 'MEDIUM', 'HIGH', 'null']):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH', 'null')")
        return value

    @field_validator('chosen_solution')
    def chosen_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null']):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @field_validator('counter_solution')
    def counter_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null']):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    @field_validator('seller_rejection_reason')
    def seller_rejection_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UNJUSTIFIED_REQUEST', 'ABUSIVE_REQUEST', 'FRAUD_ATTEMPT', 'OTHER', 'null']):
            raise ValueError("must be one of enum values ('UNJUSTIFIED_REQUEST', 'ABUSIVE_REQUEST', 'FRAUD_ATTEMPT', 'OTHER', 'null')")
        return value

    @field_validator('platform_solution')
    def platform_solution_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null']):
            raise ValueError("must be one of enum values ('PARTIAL_REFUND_WITH_PARTIAL_RETURN', 'PARTIAL_REFUND_WITHOUT_RETURN', 'COMPLETE_REFUND_WITH_RETURN', 'COMPLETE_REFUND_WITHOUT_RETURN', 'ABANDON_CLAIM', 'null')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DisputeUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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

        # set to None if platform_reasoning (nullable) is None
        # and model_fields_set contains the field
        if self.platform_reasoning is None and "platform_reasoning" in self.model_fields_set:
            _dict['platformReasoning'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DisputeUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemCount": obj.get("itemCount"),
            "issueType": obj.get("issueType"),
            "issueInDescriptionType": obj.get("issueInDescriptionType"),
            "issueMentionedInOffer": obj.get("issueMentionedInOffer"),
            "issueDetails": obj.get("issueDetails"),
            "complainantStake": obj.get("complainantStake"),
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
            "platformReasoning": obj.get("platformReasoning")
        })
        return _obj


