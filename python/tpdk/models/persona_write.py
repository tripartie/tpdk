# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.20
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conint, conlist, constr, validator
from tpdk.models.metadata_write import MetadataWrite
from tpdk.models.persona_write_address import PersonaWriteAddress

class PersonaWrite(BaseModel):
    """
    
    """
    first_name: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="firstName")
    last_name: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="lastName")
    gender: StrictStr = Field(...)
    date_of_birth: Optional[date] = Field(None, alias="dateOfBirth")
    language: Optional[StrictStr] = Field(None, description="That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements.")
    email: Optional[StrictStr] = None
    mobile_phone_number: Optional[StrictStr] = Field(None, alias="mobilePhoneNumber")
    address: Optional[PersonaWriteAddress] = None
    external_purchase_count: Optional[conint(strict=True, ge=0)] = Field(None, alias="externalPurchaseCount", description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.")
    external_sell_count: Optional[conint(strict=True, ge=0)] = Field(None, alias="externalSellCount", description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.")
    metadata: Optional[conlist(MetadataWrite, max_items=16)] = Field(None, description="You can assign different meta to your Persona object for different purposes. eg. Ease searching.")
    __properties = ["firstName", "lastName", "gender", "dateOfBirth", "language", "email", "mobilePhoneNumber", "address", "externalPurchaseCount", "externalSellCount", "metadata"]

    @validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY'):
            raise ValueError("must be one of enum values ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY')")
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
    def from_json(cls, json_str: str) -> PersonaWrite:
        """Create an instance of PersonaWrite from a JSON string"""
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

        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if mobile_phone_number (nullable) is None
        # and __fields_set__ contains the field
        if self.mobile_phone_number is None and "mobile_phone_number" in self.__fields_set__:
            _dict['mobilePhoneNumber'] = None

        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict['address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonaWrite:
        """Create an instance of PersonaWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PersonaWrite.parse_obj(obj)

        _obj = PersonaWrite.parse_obj({
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "gender": obj.get("gender") if obj.get("gender") is not None else 'RATHER_NOT_SAY',
            "date_of_birth": obj.get("dateOfBirth"),
            "language": obj.get("language"),
            "email": obj.get("email"),
            "mobile_phone_number": obj.get("mobilePhoneNumber"),
            "address": PersonaWriteAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "external_purchase_count": obj.get("externalPurchaseCount"),
            "external_sell_count": obj.get("externalSellCount"),
            "metadata": [MetadataWrite.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None
        })
        return _obj

