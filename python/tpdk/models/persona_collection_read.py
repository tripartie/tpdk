# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.13
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class PersonaCollectionRead(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    email: Optional[StrictStr] = None
    risk_level: Optional[StrictStr] = Field(None, alias="riskLevel", description="We sort Persona into three distinct risks' category. This is inferred from the riskScore.")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    offer_count: Optional[StrictInt] = Field(None, alias="offerCount", description="Issued Offers count owned by a given Persona")
    purchase_count: Optional[StrictInt] = Field(None, alias="purchaseCount")
    __properties = ["id", "firstName", "lastName", "email", "riskLevel", "createdAt", "updatedAt", "offerCount", "purchaseCount"]

    @validator('risk_level')
    def risk_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('WEAK', 'MEDIUM', 'HIGH', 'null'):
            raise ValueError("must be one of enum values ('WEAK', 'MEDIUM', 'HIGH', 'null')")
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
    def from_json(cls, json_str: str) -> PersonaCollectionRead:
        """Create an instance of PersonaCollectionRead from a JSON string"""
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
        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if risk_level (nullable) is None
        # and __fields_set__ contains the field
        if self.risk_level is None and "risk_level" in self.__fields_set__:
            _dict['riskLevel'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonaCollectionRead:
        """Create an instance of PersonaCollectionRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PersonaCollectionRead.parse_obj(obj)

        _obj = PersonaCollectionRead.parse_obj({
            "id": obj.get("id"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "email": obj.get("email"),
            "risk_level": obj.get("riskLevel"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "offer_count": obj.get("offerCount"),
            "purchase_count": obj.get("purchaseCount")
        })
        return _obj

