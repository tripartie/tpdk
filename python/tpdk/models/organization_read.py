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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class OrganizationRead(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    domain_verified: StrictBool = Field(..., alias="domainVerified")
    __properties = ["id", "name", "domainVerified"]

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
    def from_json(cls, json_str: str) -> OrganizationRead:
        """Create an instance of OrganizationRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationRead:
        """Create an instance of OrganizationRead from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrganizationRead.parse_obj(obj)

        _obj = OrganizationRead.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "domain_verified": obj.get("domainVerified")
        })
        return _obj

