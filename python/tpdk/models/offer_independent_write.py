# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.91
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from tpdk.models.metadata_independent_write import MetadataIndependentWrite
from tpdk.models.persona_independent_write import PersonaIndependentWrite

class OfferIndependentWrite(BaseModel):
    """
    An Offer object represent a public listening  # noqa: E501
    """
    public_url: Optional[StrictStr] = Field(None, alias="publicUrl", description="If specified, there would be not need for you to fill-in details. Must be accessible over WAN.")
    seller: PersonaIndependentWrite = Field(...)
    nature: StrictStr = Field(..., description="This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information.")
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="unitPrice")
    currency_code: Optional[StrictStr] = Field('EUR', alias="currencyCode")
    item_count: Optional[StrictInt] = Field(1, alias="itemCount")
    condition: Optional[StrictStr] = 'USED'
    weight_in_gram: Optional[StrictInt] = Field(None, alias="weightInGram")
    ean_code: Optional[StrictStr] = Field(None, alias="eanCode")
    metadata: Optional[conlist(MetadataIndependentWrite)] = None
    __properties = ["publicUrl", "seller", "nature", "title", "description", "unitPrice", "currencyCode", "itemCount", "condition", "weightInGram", "eanCode", "metadata"]

    @validator('nature')
    def nature_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('service', 'physical_item', 'dematerialized_item', 'rent_item'):
            raise ValueError("must be one of enum values ('service', 'physical_item', 'dematerialized_item', 'rent_item')")
        return value

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
    def from_json(cls, json_str: str) -> OfferIndependentWrite:
        """Create an instance of OfferIndependentWrite from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # set to None if public_url (nullable) is None
        # and __fields_set__ contains the field
        if self.public_url is None and "public_url" in self.__fields_set__:
            _dict['publicUrl'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if unit_price (nullable) is None
        # and __fields_set__ contains the field
        if self.unit_price is None and "unit_price" in self.__fields_set__:
            _dict['unitPrice'] = None

        # set to None if currency_code (nullable) is None
        # and __fields_set__ contains the field
        if self.currency_code is None and "currency_code" in self.__fields_set__:
            _dict['currencyCode'] = None

        # set to None if weight_in_gram (nullable) is None
        # and __fields_set__ contains the field
        if self.weight_in_gram is None and "weight_in_gram" in self.__fields_set__:
            _dict['weightInGram'] = None

        # set to None if ean_code (nullable) is None
        # and __fields_set__ contains the field
        if self.ean_code is None and "ean_code" in self.__fields_set__:
            _dict['eanCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferIndependentWrite:
        """Create an instance of OfferIndependentWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferIndependentWrite.parse_obj(obj)

        _obj = OfferIndependentWrite.parse_obj({
            "public_url": obj.get("publicUrl"),
            "seller": PersonaIndependentWrite.from_dict(obj.get("seller")) if obj.get("seller") is not None else None,
            "nature": obj.get("nature") if obj.get("nature") is not None else 'physical_item',
            "title": obj.get("title"),
            "description": obj.get("description"),
            "unit_price": obj.get("unitPrice"),
            "currency_code": obj.get("currencyCode") if obj.get("currencyCode") is not None else 'EUR',
            "item_count": obj.get("itemCount") if obj.get("itemCount") is not None else 1,
            "condition": obj.get("condition") if obj.get("condition") is not None else 'USED',
            "weight_in_gram": obj.get("weightInGram"),
            "ean_code": obj.get("eanCode"),
            "metadata": [MetadataIndependentWrite.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None
        })
        return _obj


