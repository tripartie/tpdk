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
from pydantic import BaseModel, Field, conint, constr

class EvaluationRead(BaseModel):
    """
      # noqa: E501
    """
    rating: conint(strict=True, le=10, ge=0) = Field(...)
    comment: Optional[constr(strict=True, max_length=500)] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    __properties = ["rating", "comment", "createdAt"]

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
    def from_json(cls, json_str: str) -> EvaluationRead:
        """Create an instance of EvaluationRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                          },
                          exclude_none=True)
        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EvaluationRead:
        """Create an instance of EvaluationRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EvaluationRead.parse_obj(obj)

        _obj = EvaluationRead.parse_obj({
            "rating": obj.get("rating"),
            "comment": obj.get("comment"),
            "created_at": obj.get("createdAt")
        })
        return _obj


