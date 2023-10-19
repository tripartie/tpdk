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

from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, conlist, validator
from tpdk.models.address import Address
from tpdk.models.metadata import Metadata
from tpdk.models.view import View

class Persona(BaseModel):
    """
      # noqa: E501
    """
    id: Optional[StrictInt] = None
    captcha: Optional[StrictStr] = None
    organization: Optional[StrictStr] = None
    target_url: Optional[StrictStr] = Field(None, alias="targetUrl", description="The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona.")
    auth_url: Optional[StrictStr] = Field(None, alias="authUrl", description="Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them.")
    expire_at: Optional[datetime] = Field(None, alias="expireAt", description="This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour.")
    password: Optional[StrictStr] = Field(None, description="The hashed password")
    plain_password: Optional[StrictStr] = Field(None, alias="plainPassword")
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    gender: Optional[StrictStr] = 'RATHER_NOT_SAY'
    date_of_birth: Optional[date] = Field(None, alias="dateOfBirth")
    language: Optional[StrictStr] = Field(None, description="That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements.")
    email: Optional[StrictStr] = None
    mobile_phone_number: Optional[StrictStr] = Field(None, alias="mobilePhoneNumber")
    address: Optional[Address] = None
    risk_level: Optional[StrictStr] = Field(None, alias="riskLevel", description="We sort Persona into three distinct risks' category. This is inferred from the riskScore.")
    risk_score: Optional[conint(strict=True, le=100, ge=0)] = Field(None, alias="riskScore", description="That score is regularly updated, each action taken can potentially update that value. A value close to zero mean zero risk and close to a hundred mean risky.")
    external_purchase_count: Optional[StrictInt] = Field(None, alias="externalPurchaseCount", description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.")
    external_sell_count: Optional[StrictInt] = Field(None, alias="externalSellCount", description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.")
    metadata: Optional[conlist(Metadata)] = Field(None, description="You can assign different meta to your Persona object for different purposes. eg. Ease searching.")
    offers: conlist(StrictStr) = Field(...)
    purchases: conlist(StrictStr) = Field(...)
    views: conlist(View) = Field(...)
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    offer_count: Optional[StrictInt] = Field(None, alias="offerCount", description="Issued Offers count owned by a given Persona")
    purchase_count: Optional[StrictInt] = Field(None, alias="purchaseCount")
    roles: Optional[conlist(StrictStr)] = None
    user_identifier: Optional[StrictStr] = Field(None, alias="userIdentifier", description="Either email or the mobile phone number")
    __properties = ["id", "captcha", "organization", "targetUrl", "authUrl", "expireAt", "password", "plainPassword", "firstName", "lastName", "gender", "dateOfBirth", "language", "email", "mobilePhoneNumber", "address", "riskLevel", "riskScore", "externalPurchaseCount", "externalSellCount", "metadata", "offers", "purchases", "views", "createdAt", "updatedAt", "offerCount", "purchaseCount", "roles", "userIdentifier"]

    @validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY'):
            raise ValueError("must be one of enum values ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY')")
        return value

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
    def from_json(cls, json_str: str) -> Persona:
        """Create an instance of Persona from a JSON string"""
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
                            "roles",
                            "user_identifier",
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
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item in self.views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['views'] = _items
        # set to None if captcha (nullable) is None
        # and __fields_set__ contains the field
        if self.captcha is None and "captcha" in self.__fields_set__:
            _dict['captcha'] = None

        # set to None if organization (nullable) is None
        # and __fields_set__ contains the field
        if self.organization is None and "organization" in self.__fields_set__:
            _dict['organization'] = None

        # set to None if target_url (nullable) is None
        # and __fields_set__ contains the field
        if self.target_url is None and "target_url" in self.__fields_set__:
            _dict['targetUrl'] = None

        # set to None if auth_url (nullable) is None
        # and __fields_set__ contains the field
        if self.auth_url is None and "auth_url" in self.__fields_set__:
            _dict['authUrl'] = None

        # set to None if expire_at (nullable) is None
        # and __fields_set__ contains the field
        if self.expire_at is None and "expire_at" in self.__fields_set__:
            _dict['expireAt'] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        # set to None if plain_password (nullable) is None
        # and __fields_set__ contains the field
        if self.plain_password is None and "plain_password" in self.__fields_set__:
            _dict['plainPassword'] = None

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
    def from_dict(cls, obj: dict) -> Persona:
        """Create an instance of Persona from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Persona.parse_obj(obj)

        _obj = Persona.parse_obj({
            "id": obj.get("id"),
            "captcha": obj.get("captcha"),
            "organization": obj.get("organization"),
            "target_url": obj.get("targetUrl"),
            "auth_url": obj.get("authUrl"),
            "expire_at": obj.get("expireAt"),
            "password": obj.get("password"),
            "plain_password": obj.get("plainPassword"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "gender": obj.get("gender") if obj.get("gender") is not None else 'RATHER_NOT_SAY',
            "date_of_birth": obj.get("dateOfBirth"),
            "language": obj.get("language"),
            "email": obj.get("email"),
            "mobile_phone_number": obj.get("mobilePhoneNumber"),
            "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "risk_level": obj.get("riskLevel"),
            "risk_score": obj.get("riskScore"),
            "external_purchase_count": obj.get("externalPurchaseCount"),
            "external_sell_count": obj.get("externalSellCount"),
            "metadata": [Metadata.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None,
            "offers": obj.get("offers"),
            "purchases": obj.get("purchases"),
            "views": [View.from_dict(_item) for _item in obj.get("views")] if obj.get("views") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "offer_count": obj.get("offerCount"),
            "purchase_count": obj.get("purchaseCount"),
            "roles": obj.get("roles"),
            "user_identifier": obj.get("userIdentifier")
        })
        return _obj


