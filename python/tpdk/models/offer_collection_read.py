# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.92
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator
from tpdk.models.persona_collection_read import PersonaCollectionRead

class OfferCollectionRead(BaseModel):
    """
    An Offer object represent a public listening  # noqa: E501
    """
    ulid: StrictStr = Field(...)
    public_url: Optional[StrictStr] = Field(None, alias="publicUrl", description="If specified, there would be not need for you to fill-in details. Must be accessible over WAN.")
    seller: PersonaCollectionRead = Field(...)
    title: Optional[StrictStr] = None
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="unitPrice")
    currency_code: Optional[StrictStr] = Field('EUR', alias="currencyCode")
    item_count: Optional[StrictInt] = Field(1, alias="itemCount")
    condition: Optional[StrictStr] = 'USED'
    __properties = ["ulid", "publicUrl", "seller", "title", "unitPrice", "currencyCode", "itemCount", "condition"]

    @validator('condition')
    def condition_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NEW', 'USED', 'DAMAGED', 'DETERIORATED', 'UNRECOVERABLE'):
            raise ValueError("must be one of enum values ('NEW', 'USED', 'DAMAGED', 'DETERIORATED', 'UNRECOVERABLE')")
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
    def from_json(cls, json_str: str) -> OfferCollectionRead:
        """Create an instance of OfferCollectionRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of seller
        if self.seller:
            _dict['seller'] = self.seller.to_dict()
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

        if not isinstance(obj, dict):
            return OfferCollectionRead.parse_obj(obj)

        _obj = OfferCollectionRead.parse_obj({
            "ulid": obj.get("ulid"),
            "public_url": obj.get("publicUrl"),
            "seller": PersonaCollectionRead.from_dict(obj.get("seller")) if obj.get("seller") is not None else None,
            "title": obj.get("title"),
            "unit_price": obj.get("unitPrice"),
            "currency_code": obj.get("currencyCode") if obj.get("currencyCode") is not None else 'EUR',
            "item_count": obj.get("itemCount") if obj.get("itemCount") is not None else 1,
            "condition": obj.get("condition") if obj.get("condition") is not None else 'USED'
        })
        return _obj


