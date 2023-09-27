# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.75
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr
from tpdk.models.organization_write import OrganizationWrite

class UserWrite(BaseModel):
    """
      # noqa: E501
    """
    captcha: Optional[StrictStr] = Field(...)
    first_name: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="firstName")
    last_name: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="lastName")
    public_name: Optional[constr(strict=True, max_length=32, min_length=2)] = Field(..., alias="publicName")
    role_in_company: Optional[constr(strict=True, max_length=32, min_length=2)] = Field(..., alias="roleInCompany")
    birthday: Optional[datetime] = None
    email: constr(strict=True, max_length=180) = Field(...)
    plain_password: Optional[constr(strict=True, max_length=64, min_length=6)] = Field(..., alias="plainPassword")
    intl_phone_number: Optional[StrictStr] = Field(None, alias="intlPhoneNumber")
    origin_country: Optional[StrictStr] = Field(..., alias="originCountry", description="The originating country")
    preferred_language: Optional[StrictStr] = Field(..., alias="preferredLanguage")
    consent_mail_notification: Optional[StrictBool] = Field(None, alias="consentMailNotification")
    consent_mail_ads: Optional[StrictBool] = Field(None, alias="consentMailAds")
    organization: Optional[OrganizationWrite] = None
    __properties = ["captcha", "firstName", "lastName", "publicName", "roleInCompany", "birthday", "email", "plainPassword", "intlPhoneNumber", "originCountry", "preferredLanguage", "consentMailNotification", "consentMailAds", "organization"]

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
    def from_json(cls, json_str: str) -> UserWrite:
        """Create an instance of UserWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # set to None if captcha (nullable) is None
        # and __fields_set__ contains the field
        if self.captcha is None and "captcha" in self.__fields_set__:
            _dict['captcha'] = None

        # set to None if public_name (nullable) is None
        # and __fields_set__ contains the field
        if self.public_name is None and "public_name" in self.__fields_set__:
            _dict['publicName'] = None

        # set to None if role_in_company (nullable) is None
        # and __fields_set__ contains the field
        if self.role_in_company is None and "role_in_company" in self.__fields_set__:
            _dict['roleInCompany'] = None

        # set to None if birthday (nullable) is None
        # and __fields_set__ contains the field
        if self.birthday is None and "birthday" in self.__fields_set__:
            _dict['birthday'] = None

        # set to None if plain_password (nullable) is None
        # and __fields_set__ contains the field
        if self.plain_password is None and "plain_password" in self.__fields_set__:
            _dict['plainPassword'] = None

        # set to None if intl_phone_number (nullable) is None
        # and __fields_set__ contains the field
        if self.intl_phone_number is None and "intl_phone_number" in self.__fields_set__:
            _dict['intlPhoneNumber'] = None

        # set to None if origin_country (nullable) is None
        # and __fields_set__ contains the field
        if self.origin_country is None and "origin_country" in self.__fields_set__:
            _dict['originCountry'] = None

        # set to None if preferred_language (nullable) is None
        # and __fields_set__ contains the field
        if self.preferred_language is None and "preferred_language" in self.__fields_set__:
            _dict['preferredLanguage'] = None

        # set to None if organization (nullable) is None
        # and __fields_set__ contains the field
        if self.organization is None and "organization" in self.__fields_set__:
            _dict['organization'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserWrite:
        """Create an instance of UserWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserWrite.parse_obj(obj)

        _obj = UserWrite.parse_obj({
            "captcha": obj.get("captcha"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "public_name": obj.get("publicName"),
            "role_in_company": obj.get("roleInCompany"),
            "birthday": obj.get("birthday"),
            "email": obj.get("email"),
            "plain_password": obj.get("plainPassword"),
            "intl_phone_number": obj.get("intlPhoneNumber"),
            "origin_country": obj.get("originCountry"),
            "preferred_language": obj.get("preferredLanguage"),
            "consent_mail_notification": obj.get("consentMailNotification"),
            "consent_mail_ads": obj.get("consentMailAds"),
            "organization": OrganizationWrite.from_dict(obj.get("organization")) if obj.get("organization") is not None else None
        })
        return _obj


