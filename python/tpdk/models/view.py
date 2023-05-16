# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0.b1
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class View(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    ip_address: StrictStr = Field(..., alias="ipAddress")
    offer: Optional[StrictStr] = None
    dispute: Optional[StrictStr] = None
    persona: Optional[StrictStr] = None
    user: Optional[StrictStr] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    __properties = ["id", "ipAddress", "offer", "dispute", "persona", "user", "createdAt"]

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
    def from_json(cls, json_str: str) -> View:
        """Create an instance of View from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                          },
                          exclude_none=True)
        # set to None if offer (nullable) is None
        # and __fields_set__ contains the field
        if self.offer is None and "offer" in self.__fields_set__:
            _dict['offer'] = None

        # set to None if dispute (nullable) is None
        # and __fields_set__ contains the field
        if self.dispute is None and "dispute" in self.__fields_set__:
            _dict['dispute'] = None

        # set to None if persona (nullable) is None
        # and __fields_set__ contains the field
        if self.persona is None and "persona" in self.__fields_set__:
            _dict['persona'] = None

        # set to None if user (nullable) is None
        # and __fields_set__ contains the field
        if self.user is None and "user" in self.__fields_set__:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> View:
        """Create an instance of View from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return View.parse_obj(obj)

        _obj = View.parse_obj({
            "id": obj.get("id"),
            "ip_address": obj.get("ipAddress"),
            "offer": obj.get("offer"),
            "dispute": obj.get("dispute"),
            "persona": obj.get("persona"),
            "user": obj.get("user"),
            "created_at": obj.get("createdAt")
        })
        return _obj

