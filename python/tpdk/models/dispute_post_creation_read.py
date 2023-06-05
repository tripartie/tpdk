# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.7
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class DisputePostCreationRead(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.
    """
    ulid: StrictStr = Field(...)
    url: Optional[StrictStr] = None
    __properties = ["ulid", "url"]

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
    def from_json(cls, json_str: str) -> DisputePostCreationRead:
        """Create an instance of DisputePostCreationRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DisputePostCreationRead:
        """Create an instance of DisputePostCreationRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DisputePostCreationRead.parse_obj(obj)

        _obj = DisputePostCreationRead.parse_obj({
            "ulid": obj.get("ulid"),
            "url": obj.get("url")
        })
        return _obj

