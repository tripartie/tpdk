# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.86
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator

class ApiClientWrite(BaseModel):
    """
      # noqa: E501
    """
    reference_name: Optional[constr(strict=True, max_length=32)] = Field(..., alias="referenceName")
    desired_scopes: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="desiredScopes")
    __properties = ["referenceName", "desiredScopes"]

    @validator('desired_scopes')
    def desired_scopes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('OFFER_READ', 'OFFER_WRITE', 'DISPUTE_READ', 'DISPUTE_WRITE', 'ORGANIZATION_READ', 'PERSONA_READ', 'PERSONA_WRITE', 'PERSONA_AUTH'):
                raise ValueError("each list item must be one of ('OFFER_READ', 'OFFER_WRITE', 'DISPUTE_READ', 'DISPUTE_WRITE', 'ORGANIZATION_READ', 'PERSONA_READ', 'PERSONA_WRITE', 'PERSONA_AUTH')")
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
    def from_json(cls, json_str: str) -> ApiClientWrite:
        """Create an instance of ApiClientWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if reference_name (nullable) is None
        # and __fields_set__ contains the field
        if self.reference_name is None and "reference_name" in self.__fields_set__:
            _dict['referenceName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiClientWrite:
        """Create an instance of ApiClientWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiClientWrite.parse_obj(obj)

        _obj = ApiClientWrite.parse_obj({
            "reference_name": obj.get("referenceName"),
            "desired_scopes": obj.get("desiredScopes")
        })
        return _obj


