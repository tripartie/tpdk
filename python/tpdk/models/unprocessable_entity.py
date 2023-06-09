# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.22
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist
from tpdk.models.unprocessable_entity_violations_inner import UnprocessableEntityViolationsInner

class UnprocessableEntity(BaseModel):
    """
    UnprocessableEntity
    """
    type: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    detail: Optional[StrictStr] = None
    violations: Optional[conlist(UnprocessableEntityViolationsInner)] = None
    __properties = ["type", "title", "detail", "violations"]

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
    def from_json(cls, json_str: str) -> UnprocessableEntity:
        """Create an instance of UnprocessableEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in violations (list)
        _items = []
        if self.violations:
            for _item in self.violations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['violations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UnprocessableEntity:
        """Create an instance of UnprocessableEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UnprocessableEntity.parse_obj(obj)

        _obj = UnprocessableEntity.parse_obj({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "detail": obj.get("detail"),
            "violations": [UnprocessableEntityViolationsInner.from_dict(_item) for _item in obj.get("violations")] if obj.get("violations") is not None else None
        })
        return _obj

