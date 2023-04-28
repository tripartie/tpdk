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


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

class EvaluationWrite(BaseModel):
    """
    
    """
    rating: Optional[StrictInt] = None
    comment: Optional[StrictStr] = None
    __properties = ["rating", "comment"]

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
    def from_json(cls, json_str: str) -> EvaluationWrite:
        """Create an instance of EvaluationWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EvaluationWrite:
        """Create an instance of EvaluationWrite from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EvaluationWrite.parse_obj(obj)

        _obj = EvaluationWrite.parse_obj({
            "rating": obj.get("rating"),
            "comment": obj.get("comment")
        })
        return _obj

