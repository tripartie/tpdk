# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.48
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

class Metadata(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    persona: Optional[StrictStr] = None
    dispute: Optional[StrictStr] = None
    offer: Optional[StrictStr] = None
    transaction: Optional[StrictStr] = None
    key: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    __properties = ["id", "persona", "dispute", "offer", "transaction", "key", "value"]

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
    def from_json(cls, json_str: str) -> Metadata:
        """Create an instance of Metadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        # set to None if persona (nullable) is None
        # and __fields_set__ contains the field
        if self.persona is None and "persona" in self.__fields_set__:
            _dict['persona'] = None

        # set to None if dispute (nullable) is None
        # and __fields_set__ contains the field
        if self.dispute is None and "dispute" in self.__fields_set__:
            _dict['dispute'] = None

        # set to None if offer (nullable) is None
        # and __fields_set__ contains the field
        if self.offer is None and "offer" in self.__fields_set__:
            _dict['offer'] = None

        # set to None if transaction (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction is None and "transaction" in self.__fields_set__:
            _dict['transaction'] = None

        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Metadata:
        """Create an instance of Metadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Metadata.parse_obj(obj)

        _obj = Metadata.parse_obj({
            "id": obj.get("id"),
            "persona": obj.get("persona"),
            "dispute": obj.get("dispute"),
            "offer": obj.get("offer"),
            "transaction": obj.get("transaction"),
            "key": obj.get("key"),
            "value": obj.get("value")
        })
        return _obj

