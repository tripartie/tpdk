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
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, constr

class ApiClient(BaseModel):
    """
    
    """
    identifier: constr(strict=True, max_length=32) = ...
    owner: Optional[StrictStr] = None
    created_at: datetime = Field(..., alias="createdAt")
    secret: Optional[StrictStr] = None
    monthly_quota: Optional[StrictInt] = Field(None, alias="monthlyQuota")
    name: Optional[StrictStr] = None
    redirect_uris: Optional[conlist(Dict[str, Any])] = Field(None, alias="redirectUris")
    grants: Optional[conlist(Dict[str, Any])] = None
    scopes: Optional[conlist(Dict[str, Any])] = None
    active: Optional[StrictBool] = None
    allow_plain_text_pkce: Optional[StrictBool] = Field(None, alias="allowPlainTextPkce")
    confidential: Optional[StrictBool] = None
    plain_text_pkce_allowed: Optional[StrictBool] = Field(None, alias="plainTextPkceAllowed")
    __properties = ["identifier", "owner", "createdAt", "secret", "monthlyQuota", "name", "redirectUris", "grants", "scopes", "active", "allowPlainTextPkce", "confidential", "plainTextPkceAllowed"]

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
    def from_json(cls, json_str: str) -> ApiClient:
        """Create an instance of ApiClient from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "confidential",
                            "plain_text_pkce_allowed",
                          },
                          exclude_none=True)
        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if secret (nullable) is None
        # and __fields_set__ contains the field
        if self.secret is None and "secret" in self.__fields_set__:
            _dict['secret'] = None

        # set to None if monthly_quota (nullable) is None
        # and __fields_set__ contains the field
        if self.monthly_quota is None and "monthly_quota" in self.__fields_set__:
            _dict['monthlyQuota'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiClient:
        """Create an instance of ApiClient from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiClient.parse_obj(obj)

        _obj = ApiClient.parse_obj({
            "identifier": obj.get("identifier"),
            "owner": obj.get("owner"),
            "created_at": obj.get("createdAt"),
            "secret": obj.get("secret"),
            "monthly_quota": obj.get("monthlyQuota"),
            "name": obj.get("name"),
            "redirect_uris": obj.get("redirectUris"),
            "grants": obj.get("grants"),
            "scopes": obj.get("scopes"),
            "active": obj.get("active"),
            "allow_plain_text_pkce": obj.get("allowPlainTextPkce"),
            "confidential": obj.get("confidential"),
            "plain_text_pkce_allowed": obj.get("plainTextPkceAllowed")
        })
        return _obj
