# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0-b1
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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class Evidence(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    dispute: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    status: StrictStr = ...
    media: Optional[StrictStr] = None
    additional_information: Optional[StrictStr] = Field(None, alias="additionalInformation", description="Description of what the evidence actually is.")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    __properties = ["id", "dispute", "owner", "status", "media", "additionalInformation", "createdAt", "updatedAt"]

    @validator('status')
    def status_validate_enum(cls, v):
        if v not in ('SUBMITTED', 'CORRELATED', 'UNRELATED', 'PENDING', 'TEMPERED', 'REJECTED'):
            raise ValueError("must be one of enum values ('SUBMITTED', 'CORRELATED', 'UNRELATED', 'PENDING', 'TEMPERED', 'REJECTED')")
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
    def from_json(cls, json_str: str) -> Evidence:
        """Create an instance of Evidence from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "updated_at",
                          },
                          exclude_none=True)
        # set to None if dispute (nullable) is None
        # and __fields_set__ contains the field
        if self.dispute is None and "dispute" in self.__fields_set__:
            _dict['dispute'] = None

        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if media (nullable) is None
        # and __fields_set__ contains the field
        if self.media is None and "media" in self.__fields_set__:
            _dict['media'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Evidence:
        """Create an instance of Evidence from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Evidence.parse_obj(obj)

        _obj = Evidence.parse_obj({
            "id": obj.get("id"),
            "dispute": obj.get("dispute"),
            "owner": obj.get("owner"),
            "status": obj.get("status") if obj.get("status") is not None else 'SUBMITTED',
            "media": obj.get("media"),
            "additional_information": obj.get("additionalInformation"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

