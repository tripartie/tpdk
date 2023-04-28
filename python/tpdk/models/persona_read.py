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

from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, conlist, validator
from tpdk.models.metadata_read import MetadataRead
from tpdk.models.persona_read_address import PersonaReadAddress

class PersonaRead(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    gender: Optional[StrictStr] = 'RATHER_NOT_SAY'
    date_of_birth: Optional[date] = Field(None, alias="dateOfBirth")
    language: Optional[StrictStr] = Field(None, description="That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements.")
    email: Optional[StrictStr] = None
    mobile_phone_number: Optional[StrictStr] = Field(None, alias="mobilePhoneNumber")
    address: Optional[PersonaReadAddress] = None
    risk_level: Optional[StrictStr] = Field(None, alias="riskLevel", description="We sort Persona into three distinct risks' category. This is inferred from the riskScore.")
    risk_score: Optional[conint(strict=True, le=100, ge=0)] = Field(None, alias="riskScore", description="That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky.")
    external_purchase_count: Optional[StrictInt] = Field(None, alias="externalPurchaseCount", description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.")
    external_sell_count: Optional[StrictInt] = Field(None, alias="externalSellCount", description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.")
    metadata: conlist(MetadataRead) = Field(..., description="You can assign different meta to your Persona object for different purposes. eg. Ease searching.")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    offer_count: Optional[StrictInt] = Field(None, alias="offerCount", description="Issued Offers count owned by a given Persona")
    purchase_count: Optional[StrictInt] = Field(None, alias="purchaseCount")
    __properties = ["id", "firstName", "lastName", "gender", "dateOfBirth", "language", "email", "mobilePhoneNumber", "address", "riskLevel", "riskScore", "externalPurchaseCount", "externalSellCount", "metadata", "createdAt", "updatedAt", "offerCount", "purchaseCount"]

    @validator('gender')
    def gender_validate_enum(cls, v):
        if v is None:
            return v
        if v not in ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY'):
            raise ValueError("must be one of enum values ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY')")
        return v

    @validator('risk_level')
    def risk_level_validate_enum(cls, v):
        if v is None:
            return v
        if v not in ('WEAK', 'MEDIUM', 'HIGH', 'null'):
            raise ValueError("must be one of enum values ('WEAK', 'MEDIUM', 'HIGH', 'null')")
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
    def from_json(cls, json_str: str) -> PersonaRead:
        """Create an instance of PersonaRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "updated_at",
                            "offer_count",
                            "purchase_count",
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

        # set to None if risk_level (nullable) is None
        # and __fields_set__ contains the field
        if self.risk_level is None and "risk_level" in self.__fields_set__:
            _dict['riskLevel'] = None

        # set to None if risk_score (nullable) is None
        # and __fields_set__ contains the field
        if self.risk_score is None and "risk_score" in self.__fields_set__:
            _dict['riskScore'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonaRead:
        """Create an instance of PersonaRead from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PersonaRead.parse_obj(obj)

        _obj = PersonaRead.parse_obj({
            "id": obj.get("id"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "gender": obj.get("gender") if obj.get("gender") is not None else 'RATHER_NOT_SAY',
            "date_of_birth": obj.get("dateOfBirth"),
            "language": obj.get("language"),
            "email": obj.get("email"),
            "mobile_phone_number": obj.get("mobilePhoneNumber"),
            "address": PersonaReadAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "risk_level": obj.get("riskLevel"),
            "risk_score": obj.get("riskScore"),
            "external_purchase_count": obj.get("externalPurchaseCount"),
            "external_sell_count": obj.get("externalSellCount"),
            "metadata": [MetadataRead.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "offer_count": obj.get("offerCount"),
            "purchase_count": obj.get("purchaseCount")
        })
        return _obj
