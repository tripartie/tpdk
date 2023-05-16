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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from tpdk.models.user_api import UserApi
from tpdk.models.view import View

class User(BaseModel):
    """
    
    """
    id: Optional[StrictStr] = None
    captcha: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    public_name: Optional[StrictStr] = Field(None, alias="publicName")
    role_in_company: Optional[StrictStr] = Field(None, alias="roleInCompany")
    birthday: datetime = Field(...)
    email: Optional[StrictStr] = None
    roles: conlist(StrictStr) = Field(...)
    password: StrictStr = Field(..., description="The hashed password")
    plain_password: Optional[StrictStr] = Field(None, alias="plainPassword")
    intl_phone_number: Optional[StrictStr] = Field(None, alias="intlPhoneNumber")
    origin_country: Optional[constr(strict=True, max_length=3)] = Field(None, alias="originCountry", description="The originating country")
    preferred_language: Optional[constr(strict=True, max_length=2)] = Field(None, alias="preferredLanguage")
    last_successful_log_in: Optional[datetime] = Field(None, alias="lastSuccessfulLogIn")
    email_verification_code: Optional[StrictStr] = Field(None, alias="emailVerificationCode")
    email_verification_input: Optional[StrictStr] = Field(None, alias="emailVerificationInput")
    phone_verification_code: Optional[StrictStr] = Field(None, alias="phoneVerificationCode")
    phone_verification_input: Optional[StrictStr] = Field(None, alias="phoneVerificationInput")
    avatar: Optional[StrictStr] = None
    notifications: Optional[conlist(StrictStr)] = None
    medias: Optional[conlist(StrictStr)] = None
    views: conlist(View) = Field(...)
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    consent_mail_notification: StrictBool = Field(..., alias="consentMailNotification")
    consent_mail_ads: StrictBool = Field(..., alias="consentMailAds")
    api: Optional[UserApi] = None
    organization: Optional[StrictStr] = None
    username: Optional[StrictStr] = Field(None, description="A visual identifier that represents this user.")
    salt: Optional[StrictStr] = None
    user_identifier: Optional[StrictStr] = Field(None, alias="userIdentifier")
    __properties = ["id", "captcha", "firstName", "lastName", "publicName", "roleInCompany", "birthday", "email", "roles", "password", "plainPassword", "intlPhoneNumber", "originCountry", "preferredLanguage", "lastSuccessfulLogIn", "emailVerificationCode", "emailVerificationInput", "phoneVerificationCode", "phoneVerificationInput", "avatar", "notifications", "medias", "views", "createdAt", "updatedAt", "consentMailNotification", "consentMailAds", "api", "organization", "username", "salt", "userIdentifier"]

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
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "notifications",
                            "medias",
                            "created_at",
                            "updated_at",
                            "username",
                            "salt",
                            "user_identifier",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item in self.views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['views'] = _items
        # override the default output from pydantic by calling `to_dict()` of api
        if self.api:
            _dict['api'] = self.api.to_dict()
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

        # set to None if plain_password (nullable) is None
        # and __fields_set__ contains the field
        if self.plain_password is None and "plain_password" in self.__fields_set__:
            _dict['plainPassword'] = None

        # set to None if intl_phone_number (nullable) is None
        # and __fields_set__ contains the field
        if self.intl_phone_number is None and "intl_phone_number" in self.__fields_set__:
            _dict['intlPhoneNumber'] = None

        # set to None if last_successful_log_in (nullable) is None
        # and __fields_set__ contains the field
        if self.last_successful_log_in is None and "last_successful_log_in" in self.__fields_set__:
            _dict['lastSuccessfulLogIn'] = None

        # set to None if email_verification_code (nullable) is None
        # and __fields_set__ contains the field
        if self.email_verification_code is None and "email_verification_code" in self.__fields_set__:
            _dict['emailVerificationCode'] = None

        # set to None if email_verification_input (nullable) is None
        # and __fields_set__ contains the field
        if self.email_verification_input is None and "email_verification_input" in self.__fields_set__:
            _dict['emailVerificationInput'] = None

        # set to None if phone_verification_code (nullable) is None
        # and __fields_set__ contains the field
        if self.phone_verification_code is None and "phone_verification_code" in self.__fields_set__:
            _dict['phoneVerificationCode'] = None

        # set to None if phone_verification_input (nullable) is None
        # and __fields_set__ contains the field
        if self.phone_verification_input is None and "phone_verification_input" in self.__fields_set__:
            _dict['phoneVerificationInput'] = None

        # set to None if avatar (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar is None and "avatar" in self.__fields_set__:
            _dict['avatar'] = None

        # set to None if api (nullable) is None
        # and __fields_set__ contains the field
        if self.api is None and "api" in self.__fields_set__:
            _dict['api'] = None

        # set to None if organization (nullable) is None
        # and __fields_set__ contains the field
        if self.organization is None and "organization" in self.__fields_set__:
            _dict['organization'] = None

        # set to None if salt (nullable) is None
        # and __fields_set__ contains the field
        if self.salt is None and "salt" in self.__fields_set__:
            _dict['salt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User.parse_obj(obj)

        _obj = User.parse_obj({
            "id": obj.get("id"),
            "captcha": obj.get("captcha"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "public_name": obj.get("publicName"),
            "role_in_company": obj.get("roleInCompany"),
            "birthday": obj.get("birthday"),
            "email": obj.get("email"),
            "roles": obj.get("roles"),
            "password": obj.get("password"),
            "plain_password": obj.get("plainPassword"),
            "intl_phone_number": obj.get("intlPhoneNumber"),
            "origin_country": obj.get("originCountry"),
            "preferred_language": obj.get("preferredLanguage"),
            "last_successful_log_in": obj.get("lastSuccessfulLogIn"),
            "email_verification_code": obj.get("emailVerificationCode"),
            "email_verification_input": obj.get("emailVerificationInput"),
            "phone_verification_code": obj.get("phoneVerificationCode"),
            "phone_verification_input": obj.get("phoneVerificationInput"),
            "avatar": obj.get("avatar"),
            "notifications": obj.get("notifications"),
            "medias": obj.get("medias"),
            "views": [View.from_dict(_item) for _item in obj.get("views")] if obj.get("views") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "consent_mail_notification": obj.get("consentMailNotification"),
            "consent_mail_ads": obj.get("consentMailAds"),
            "api": UserApi.from_dict(obj.get("api")) if obj.get("api") is not None else None,
            "organization": obj.get("organization"),
            "username": obj.get("username"),
            "salt": obj.get("salt"),
            "user_identifier": obj.get("userIdentifier")
        })
        return _obj

