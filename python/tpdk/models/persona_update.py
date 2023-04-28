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

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from tpdk.models.metadata_update import MetadataUpdate
from tpdk.models.persona_update_address import PersonaUpdateAddress

class PersonaUpdate(BaseModel):
    """
    
    """
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    gender: Optional[StrictStr] = 'RATHER_NOT_SAY'
    date_of_birth: Optional[date] = Field(None, alias="dateOfBirth")
    language: Optional[StrictStr] = Field(None, description="That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements.")
    address: Optional[PersonaUpdateAddress] = None
    external_purchase_count: Optional[StrictInt] = Field(None, alias="externalPurchaseCount", description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.")
    external_sell_count: Optional[StrictInt] = Field(None, alias="externalSellCount", description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.")
    metadata: conlist(MetadataUpdate) = Field(..., description="You can assign different meta to your Persona object for different purposes. eg. Ease searching.")
    __properties = ["firstName", "lastName", "gender", "dateOfBirth", "language", "address", "externalPurchaseCount", "externalSellCount", "metadata"]

    @validator('gender')
    def gender_validate_enum(cls, v):
        if v is None:
            return v
        if v not in ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY'):
            raise ValueError("must be one of enum values ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY')")
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
    def from_json(cls, json_str: str) -> PersonaUpdate:
        """Create an instance of PersonaUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # set to None if date_of_birth (nullable) is None
        # and __fields_set__ contains the field
        if self.date_of_birth is None and "date_of_birth" in self.__fields_set__:
            _dict['dateOfBirth'] = None

        # set to None if language (nullable) is None
        # and __fields_set__ contains the field
        if self.language is None and "language" in self.__fields_set__:
            _dict['language'] = None

        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict['address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonaUpdate:
        """Create an instance of PersonaUpdate from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PersonaUpdate.parse_obj(obj)

        _obj = PersonaUpdate.parse_obj({
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "gender": obj.get("gender") if obj.get("gender") is not None else 'RATHER_NOT_SAY',
            "date_of_birth": obj.get("dateOfBirth"),
            "language": obj.get("language"),
            "address": PersonaUpdateAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "external_purchase_count": obj.get("externalPurchaseCount"),
            "external_sell_count": obj.get("externalSellCount"),
            "metadata": [MetadataUpdate.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None
        })
        return _obj
