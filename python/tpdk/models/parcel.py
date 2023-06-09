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

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictInt, StrictStr, confloat, conint, constr, validator

class Parcel(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    carrier: StrictStr = Field(...)
    identifier: constr(strict=True, max_length=128, min_length=4) = Field(...)
    price: Optional[Union[confloat(ge=0, strict=True), conint(ge=0, strict=True)]] = None
    currency: Optional[StrictStr] = 'EUR'
    status: Optional[StrictStr] = None
    dispute: Optional[StrictStr] = None
    transaction: Optional[StrictStr] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    __properties = ["id", "carrier", "identifier", "price", "currency", "status", "dispute", "transaction", "createdAt", "updatedAt"]

    @validator('carrier')
    def carrier_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SwissPost', 'MondialRelay', 'Colissimo', 'Dhl', 'Chronopost', 'ColisPrive', 'Dpd', 'Ups', 'FedEx', 'RelaisColis'):
            raise ValueError("must be one of enum values ('SwissPost', 'MondialRelay', 'Colissimo', 'Dhl', 'Chronopost', 'ColisPrive', 'Dpd', 'Ups', 'FedEx', 'RelaisColis')")
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
    def from_json(cls, json_str: str) -> Parcel:
        """Create an instance of Parcel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "updated_at",
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

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if dispute (nullable) is None
        # and __fields_set__ contains the field
        if self.dispute is None and "dispute" in self.__fields_set__:
            _dict['dispute'] = None

        # set to None if transaction (nullable) is None
        # and __fields_set__ contains the field
        if self.transaction is None and "transaction" in self.__fields_set__:
            _dict['transaction'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Parcel:
        """Create an instance of Parcel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Parcel.parse_obj(obj)

        _obj = Parcel.parse_obj({
            "id": obj.get("id"),
            "carrier": obj.get("carrier"),
            "identifier": obj.get("identifier"),
            "price": obj.get("price"),
            "currency": obj.get("currency") if obj.get("currency") is not None else 'EUR',
            "status": obj.get("status"),
            "dispute": obj.get("dispute"),
            "transaction": obj.get("transaction"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

