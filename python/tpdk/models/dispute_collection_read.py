# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0-b2
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, validator
from tpdk.models.transaction_collection_read import TransactionCollectionRead

class DisputeCollectionRead(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.
    """
    ulid: StrictStr = ...
    transaction: Optional[TransactionCollectionRead] = None
    status: StrictStr = ...
    item_count: Optional[conint(strict=True, gt=0)] = Field(None, alias="itemCount", description="The dispute may concern only PART of the package. Specify it there.")
    issue_type: StrictStr = Field(..., alias="issueType")
    issue_in_description_type: Optional[StrictStr] = Field(None, alias="issueInDescriptionType", description="To be set only in conjunction of issueType = NOT_AS_DESCRIBED.")
    complainant_stake: StrictStr = Field(..., alias="complainantStake")
    inferred_stake: Optional[StrictStr] = Field(None, alias="inferredStake")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    iri: Optional[StrictStr] = None
    message_count: Optional[StrictInt] = Field(None, alias="messageCount")
    __properties = ["ulid", "transaction", "status", "itemCount", "issueType", "issueInDescriptionType", "complainantStake", "inferredStake", "createdAt", "updatedAt", "iri", "messageCount"]

    @validator('status')
    def status_validate_enum(cls, v):
        if v not in ('CREATED', 'SUBMITTED', 'OPENED', 'ABANDONED', 'PENDING', 'OBJECTED', 'SHIPPED', 'IN_TRANSIT', 'RETURNED', 'DISMISSED', 'RESOLVED'):
            raise ValueError("must be one of enum values ('CREATED', 'SUBMITTED', 'OPENED', 'ABANDONED', 'PENDING', 'OBJECTED', 'SHIPPED', 'IN_TRANSIT', 'RETURNED', 'DISMISSED', 'RESOLVED')")
        return v

    @validator('issue_type')
    def issue_type_validate_enum(cls, v):
        if v not in ('NOT_AS_DESCRIBED', 'DOES_NOT_WORK', 'IS_INCOMPLETE', 'DELIVERY_ISSUE', 'ALLEGED_FRAUD'):
            raise ValueError("must be one of enum values ('NOT_AS_DESCRIBED', 'DOES_NOT_WORK', 'IS_INCOMPLETE', 'DELIVERY_ISSUE', 'ALLEGED_FRAUD')")
        return v

    @validator('issue_in_description_type')
    def issue_in_description_type_validate_enum(cls, v):
        if v is None:
            return v
        if v not in ('WRONG_COLOUR', 'DAMAGED_OR_USED', 'INCORRECT_FORMAT_OR_SIZE', 'DIFFERENT_MATERIAL', 'null'):
            raise ValueError("must be one of enum values ('WRONG_COLOUR', 'DAMAGED_OR_USED', 'INCORRECT_FORMAT_OR_SIZE', 'DIFFERENT_MATERIAL', 'null')")
        return v

    @validator('complainant_stake')
    def complainant_stake_validate_enum(cls, v):
        if v not in ('LOW', 'MEDIUM', 'HIGH'):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH')")
        return v

    @validator('inferred_stake')
    def inferred_stake_validate_enum(cls, v):
        if v is None:
            return v
        if v not in ('LOW', 'MEDIUM', 'HIGH', 'null'):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH', 'null')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DisputeCollectionRead:
        """Create an instance of DisputeCollectionRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                            "updated_at",
                            "iri",
                            "message_count",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # set to None if item_count (nullable) is None
        # and __fields_set__ contains the field
        if self.item_count is None and "item_count" in self.__fields_set__:
            _dict['itemCount'] = None

        # set to None if issue_in_description_type (nullable) is None
        # and __fields_set__ contains the field
        if self.issue_in_description_type is None and "issue_in_description_type" in self.__fields_set__:
            _dict['issueInDescriptionType'] = None

        # set to None if inferred_stake (nullable) is None
        # and __fields_set__ contains the field
        if self.inferred_stake is None and "inferred_stake" in self.__fields_set__:
            _dict['inferredStake'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DisputeCollectionRead:
        """Create an instance of DisputeCollectionRead from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DisputeCollectionRead.parse_obj(obj)

        _obj = DisputeCollectionRead.parse_obj({
            "ulid": obj.get("ulid"),
            "transaction": TransactionCollectionRead.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None,
            "status": obj.get("status") if obj.get("status") is not None else 'CREATED',
            "item_count": obj.get("itemCount"),
            "issue_type": obj.get("issueType"),
            "issue_in_description_type": obj.get("issueInDescriptionType"),
            "complainant_stake": obj.get("complainantStake"),
            "inferred_stake": obj.get("inferredStake"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "iri": obj.get("iri"),
            "message_count": obj.get("messageCount")
        })
        return _obj

