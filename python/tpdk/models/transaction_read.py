# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.52
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from tpdk.models.metadata_read import MetadataRead
from tpdk.models.offer_read import OfferRead
from tpdk.models.parcel_read import ParcelRead

class TransactionRead(BaseModel):
    """
    
    """
    ulid: StrictStr = Field(...)
    offer: OfferRead = Field(...)
    buyer: StrictStr = Field(...)
    fees: Optional[Union[StrictFloat, StrictInt]] = None
    metadata: Optional[conlist(MetadataRead)] = None
    parcels: Optional[conlist(ParcelRead)] = None
    __properties = ["ulid", "offer", "buyer", "fees", "metadata", "parcels"]

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
    def from_json(cls, json_str: str) -> TransactionRead:
        """Create an instance of TransactionRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of offer
        if self.offer:
            _dict['offer'] = self.offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parcels (list)
        _items = []
        if self.parcels:
            for _item in self.parcels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parcels'] = _items
        # set to None if fees (nullable) is None
        # and __fields_set__ contains the field
        if self.fees is None and "fees" in self.__fields_set__:
            _dict['fees'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionRead:
        """Create an instance of TransactionRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionRead.parse_obj(obj)

        _obj = TransactionRead.parse_obj({
            "ulid": obj.get("ulid"),
            "offer": OfferRead.from_dict(obj.get("offer")) if obj.get("offer") is not None else None,
            "buyer": obj.get("buyer"),
            "fees": obj.get("fees"),
            "metadata": [MetadataRead.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None,
            "parcels": [ParcelRead.from_dict(_item) for _item in obj.get("parcels")] if obj.get("parcels") is not None else None
        })
        return _obj

