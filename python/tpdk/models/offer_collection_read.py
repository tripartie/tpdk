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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class OfferCollectionRead(BaseModel):
    """
    An Offer object represent a public listening
    """
    ulid: StrictStr = ...
    public_url: Optional[StrictStr] = Field(None, alias="publicUrl", description="If specified, there would be not need for you to fill-in details. Must be accessible over WAN.")
    title: Optional[StrictStr] = None
    unit_price: Optional[StrictFloat] = Field(None, alias="unitPrice")
    currency_code: Optional[StrictStr] = Field('EUR', alias="currencyCode")
    item_count: StrictInt = Field(..., alias="itemCount")
    condition: StrictStr = ...
    __properties = ["ulid", "publicUrl", "title", "unitPrice", "currencyCode", "itemCount", "condition"]

    @validator('condition')
    def condition_validate_enum(cls, v):
        if v not in ('NEW', 'USED', 'DAMAGED', 'DETERIORATED', 'UNRECOVERABLE'):
            raise ValueError("must be one of enum values ('NEW', 'USED', 'DAMAGED', 'DETERIORATED', 'UNRECOVERABLE')")
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
    def from_json(cls, json_str: str) -> OfferCollectionRead:
        """Create an instance of OfferCollectionRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if public_url (nullable) is None
        # and __fields_set__ contains the field
        if self.public_url is None and "public_url" in self.__fields_set__:
            _dict['publicUrl'] = None

        # set to None if unit_price (nullable) is None
        # and __fields_set__ contains the field
        if self.unit_price is None and "unit_price" in self.__fields_set__:
            _dict['unitPrice'] = None

        # set to None if currency_code (nullable) is None
        # and __fields_set__ contains the field
        if self.currency_code is None and "currency_code" in self.__fields_set__:
            _dict['currencyCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferCollectionRead:
        """Create an instance of OfferCollectionRead from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OfferCollectionRead.parse_obj(obj)

        _obj = OfferCollectionRead.parse_obj({
            "ulid": obj.get("ulid"),
            "public_url": obj.get("publicUrl"),
            "title": obj.get("title"),
            "unit_price": obj.get("unitPrice"),
            "currency_code": obj.get("currencyCode") if obj.get("currencyCode") is not None else 'EUR',
            "item_count": obj.get("itemCount") if obj.get("itemCount") is not None else 1,
            "condition": obj.get("condition") if obj.get("condition") is not None else 'USED'
        })
        return _obj
