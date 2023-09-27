# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.74
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class PersonaPostAuthRead(BaseModel):
    """
      # noqa: E501
    """
    auth_url: Optional[StrictStr] = Field(None, alias="authUrl", description="Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them.")
    expire_at: Optional[datetime] = Field(None, alias="expireAt", description="This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour.")
    __properties = ["authUrl", "expireAt"]

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
    def from_json(cls, json_str: str) -> PersonaPostAuthRead:
        """Create an instance of PersonaPostAuthRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if auth_url (nullable) is None
        # and __fields_set__ contains the field
        if self.auth_url is None and "auth_url" in self.__fields_set__:
            _dict['authUrl'] = None

        # set to None if expire_at (nullable) is None
        # and __fields_set__ contains the field
        if self.expire_at is None and "expire_at" in self.__fields_set__:
            _dict['expireAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonaPostAuthRead:
        """Create an instance of PersonaPostAuthRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PersonaPostAuthRead.parse_obj(obj)

        _obj = PersonaPostAuthRead.parse_obj({
            "auth_url": obj.get("authUrl"),
            "expire_at": obj.get("expireAt")
        })
        return _obj


