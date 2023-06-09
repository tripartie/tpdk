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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class UserUpdate(BaseModel):
    """
    
    """
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    public_name: Optional[StrictStr] = Field(None, alias="publicName")
    role_in_company: Optional[StrictStr] = Field(None, alias="roleInCompany")
    birthday: datetime = Field(...)
    intl_phone_number: Optional[StrictStr] = Field(None, alias="intlPhoneNumber")
    consent_mail_notification: StrictBool = Field(..., alias="consentMailNotification")
    consent_mail_ads: StrictBool = Field(..., alias="consentMailAds")
    __properties = ["firstName", "lastName", "publicName", "roleInCompany", "birthday", "intlPhoneNumber", "consentMailNotification", "consentMailAds"]

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
    def from_json(cls, json_str: str) -> UserUpdate:
        """Create an instance of UserUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if public_name (nullable) is None
        # and __fields_set__ contains the field
        if self.public_name is None and "public_name" in self.__fields_set__:
            _dict['publicName'] = None

        # set to None if role_in_company (nullable) is None
        # and __fields_set__ contains the field
        if self.role_in_company is None and "role_in_company" in self.__fields_set__:
            _dict['roleInCompany'] = None

        # set to None if intl_phone_number (nullable) is None
        # and __fields_set__ contains the field
        if self.intl_phone_number is None and "intl_phone_number" in self.__fields_set__:
            _dict['intlPhoneNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserUpdate:
        """Create an instance of UserUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserUpdate.parse_obj(obj)

        _obj = UserUpdate.parse_obj({
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "public_name": obj.get("publicName"),
            "role_in_company": obj.get("roleInCompany"),
            "birthday": obj.get("birthday"),
            "intl_phone_number": obj.get("intlPhoneNumber"),
            "consent_mail_notification": obj.get("consentMailNotification"),
            "consent_mail_ads": obj.get("consentMailAds")
        })
        return _obj

