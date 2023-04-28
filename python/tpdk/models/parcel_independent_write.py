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
from pydantic import BaseModel, StrictStr, confloat, constr, validator

class ParcelIndependentWrite(BaseModel):
    """
    
    """
    carrier: StrictStr = ...
    identifier: constr(strict=True, max_length=128, min_length=4) = ...
    price: Optional[confloat(ge=0, strict=True)] = None
    currency: Optional[StrictStr] = 'EUR'
    __properties = ["carrier", "identifier", "price", "currency"]

    @validator('carrier')
    def carrier_validate_enum(cls, v):
        if v not in ('SwissPost', 'MondialRelay', 'Colissimo', 'Dhl', 'Chronopost', 'ColisPrive', 'Dpd', 'Ups', 'FedEx', 'RelaisColis'):
            raise ValueError("must be one of enum values ('SwissPost', 'MondialRelay', 'Colissimo', 'Dhl', 'Chronopost', 'ColisPrive', 'Dpd', 'Ups', 'FedEx', 'RelaisColis')")
        return v

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
    def from_json(cls, json_str: str) -> ParcelIndependentWrite:
        """Create an instance of ParcelIndependentWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if price (nullable) is None
        # and __fields_set__ contains the field
        if self.price is None and "price" in self.__fields_set__:
            _dict['price'] = None

        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParcelIndependentWrite:
        """Create an instance of ParcelIndependentWrite from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ParcelIndependentWrite.parse_obj(obj)

        _obj = ParcelIndependentWrite.parse_obj({
            "carrier": obj.get("carrier"),
            "identifier": obj.get("identifier"),
            "price": obj.get("price"),
            "currency": obj.get("currency") if obj.get("currency") is not None else 'EUR'
        })
        return _obj

