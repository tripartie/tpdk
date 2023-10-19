# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.91
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from tpdk.models.view import View

class User(BaseModel):
    """
      # noqa: E501
    """
    id: Optional[StrictStr] = None
    captcha: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    public_name: Optional[StrictStr] = Field(None, alias="publicName")
    role_in_company: Optional[StrictStr] = Field(None, alias="roleInCompany")
    birthday: Optional[datetime] = None
    email: Optional[StrictStr] = None
    invited_role: Optional[conlist(StrictStr)] = Field(None, alias="invitedRole")
    roles: conlist(StrictStr) = Field(...)
    password: Optional[StrictStr] = Field(None, description="The hashed password")
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
    keys: conlist(StrictStr) = Field(...)
    organization: Optional[StrictStr] = None
    username: Optional[StrictStr] = Field(None, description="A visual identifier that represents this user.")
    salt: Optional[StrictStr] = None
    user_identifier: Optional[StrictStr] = Field(None, alias="userIdentifier")
    __properties = ["id", "captcha", "firstName", "lastName", "publicName", "roleInCompany", "birthday", "email", "invitedRole", "roles", "password", "plainPassword", "intlPhoneNumber", "originCountry", "preferredLanguage", "lastSuccessfulLogIn", "emailVerificationCode", "emailVerificationInput", "phoneVerificationCode", "phoneVerificationInput", "avatar", "notifications", "medias", "views", "createdAt", "updatedAt", "consentMailNotification", "consentMailAds", "keys", "organization", "username", "salt", "userIdentifier"]

    @validator('invited_role')
    def invited_role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('ROLE_ADMIN', 'ROLE_CONSULTANT', 'ROLE_ACCOUNTING_MANAGER', 'ROLE_BILLING_MANAGER', 'ROLE_CUSTOMER_SERVICE'):
                raise ValueError("each list item must be one of ('ROLE_ADMIN', 'ROLE_CONSULTANT', 'ROLE_ACCOUNTING_MANAGER', 'ROLE_BILLING_MANAGER', 'ROLE_CUSTOMER_SERVICE')")
        return value

    @validator('roles')
    def roles_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in ('ROLE_ORGANIZATION_OWNER', 'ROLE_ADMIN', 'ROLE_CONSULTANT', 'ROLE_ACCOUNTING_MANAGER', 'ROLE_BILLING_MANAGER', 'ROLE_CUSTOMER_SERVICE', 'ROLE_PLATFORM_SUPPORT', 'ROLE_PLATFORM_ADMIN', 'ROLE_USER'):
                raise ValueError("each list item must be one of ('ROLE_ORGANIZATION_OWNER', 'ROLE_ADMIN', 'ROLE_CONSULTANT', 'ROLE_ACCOUNTING_MANAGER', 'ROLE_BILLING_MANAGER', 'ROLE_CUSTOMER_SERVICE', 'ROLE_PLATFORM_SUPPORT', 'ROLE_PLATFORM_ADMIN', 'ROLE_USER')")
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

        # set to None if invited_role (nullable) is None
        # and __fields_set__ contains the field
        if self.invited_role is None and "invited_role" in self.__fields_set__:
            _dict['invitedRole'] = None

        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

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
            "invited_role": obj.get("invitedRole"),
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
            "keys": obj.get("keys"),
            "organization": obj.get("organization"),
            "username": obj.get("username"),
            "salt": obj.get("salt"),
            "user_identifier": obj.get("userIdentifier")
        })
        return _obj


