# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.46
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, constr, validator

class DisputeUpdate(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.
    """
    item_count: Optional[conint(strict=True, gt=0)] = Field(None, alias="itemCount", description="The dispute may concern only PART of the package. Specify it there.")
    issue_type: Optional[StrictStr] = Field(None, alias="issueType")
    issue_in_description_type: Optional[StrictStr] = Field(None, alias="issueInDescriptionType", description="To be set only in conjunction of issueType = NOT_AS_DESCRIBED.")
    issue_mentioned_in_offer: Optional[StrictBool] = Field(None, alias="issueMentionedInOffer")
    issue_details: Optional[constr(strict=True, max_length=1000, min_length=30)] = Field(None, alias="issueDetails")
    complainant_stake: Optional[StrictStr] = Field(None, alias="complainantStake")
    chosen_solution: Optional[StrictStr] = Field(None, alias="chosenSolution")
    chosen_partial_refund_amount: Optional[conint(strict=True, gt=0)] = Field(None, alias="chosenPartialRefundAmount")
    counter_solution: Optional[StrictStr] = Field(None, alias="counterSolution")
    counter_partial_refund_amount: Optional[conint(strict=True, gt=0)] = Field(None, alias="counterPartialRefundAmount")
    complainant_approval: Optional[StrictBool] = Field(None, alias="complainantApproval")
    seller_approval: Optional[StrictBool] = Field(None, alias="sellerApproval")
    __properties = ["itemCount", "issueType", "issueInDescriptionType", "issueMentionedInOffer", "issueDetails", "complainantStake", "chosenSolution", "chosenPartialRefundAmount", "counterSolution", "counterPartialRefundAmount", "complainantApproval", "sellerApproval"]

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
    def from_json(cls, json_str: str) -> DisputeUpdate:
        """Create an instance of DisputeUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DisputeUpdate:
        """Create an instance of DisputeUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DisputeUpdate.parse_obj(obj)

        _obj = DisputeUpdate.parse_obj({
            "item_count": obj.get("itemCount"),
            "issue_type": obj.get("issueType"),
            "issue_in_description_type": obj.get("issueInDescriptionType"),
            "issue_mentioned_in_offer": obj.get("issueMentionedInOffer"),
            "issue_details": obj.get("issueDetails"),
            "complainant_stake": obj.get("complainantStake"),
            "chosen_solution": obj.get("chosenSolution"),
            "chosen_partial_refund_amount": obj.get("chosenPartialRefundAmount"),
            "counter_solution": obj.get("counterSolution"),
            "counter_partial_refund_amount": obj.get("counterPartialRefundAmount"),
            "complainant_approval": obj.get("complainantApproval"),
            "seller_approval": obj.get("sellerApproval")
        })
        return _obj

