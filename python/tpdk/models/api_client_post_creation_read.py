# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.29
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr

class ApiClientPostCreationRead(BaseModel):
    """
    
    """
    identifier: Optional[StrictStr] = None
    secret: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    __properties = ["identifier", "secret", "name"]

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
    def from_json(cls, json_str: str) -> ApiClientPostCreationRead:
        """Create an instance of ApiClientPostCreationRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiClientPostCreationRead:
        """Create an instance of ApiClientPostCreationRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiClientPostCreationRead.parse_obj(obj)

        _obj = ApiClientPostCreationRead.parse_obj({
            "identifier": obj.get("identifier"),
            "secret": obj.get("secret"),
            "name": obj.get("name")
        })
        return _obj

