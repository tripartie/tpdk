# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.29
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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from tpdk.models.organization_authenticated_read_icon import OrganizationAuthenticatedReadIcon
from tpdk.models.user_authenticated_read_organization import UserAuthenticatedReadOrganization

class UserAuthenticatedRead(BaseModel):
    """
    
    """
    id: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    public_name: Optional[StrictStr] = Field(None, alias="publicName")
    role_in_company: Optional[StrictStr] = Field(None, alias="roleInCompany")
    birthday: datetime = Field(...)
    email: Optional[StrictStr] = None
    roles: conlist(StrictStr) = Field(...)
    intl_phone_number: Optional[StrictStr] = Field(None, alias="intlPhoneNumber")
    origin_country: Optional[constr(strict=True, max_length=3)] = Field(None, alias="originCountry", description="The originating country")
    preferred_language: Optional[constr(strict=True, max_length=2)] = Field(None, alias="preferredLanguage")
    last_successful_log_in: Optional[datetime] = Field(None, alias="lastSuccessfulLogIn")
    avatar: Optional[OrganizationAuthenticatedReadIcon] = None
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    consent_mail_notification: StrictBool = Field(..., alias="consentMailNotification")
    consent_mail_ads: StrictBool = Field(..., alias="consentMailAds")
    organization: Optional[UserAuthenticatedReadOrganization] = None
    __properties = ["id", "firstName", "lastName", "publicName", "roleInCompany", "birthday", "email", "roles", "intlPhoneNumber", "originCountry", "preferredLanguage", "lastSuccessfulLogIn", "avatar", "createdAt", "updatedAt", "consentMailNotification", "consentMailAds", "organization"]

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
    def from_json(cls, json_str: str) -> UserAuthenticatedRead:
        """Create an instance of UserAuthenticatedRead from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of avatar
        if self.avatar:
            _dict['avatar'] = self.avatar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
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

        # set to None if last_successful_log_in (nullable) is None
        # and __fields_set__ contains the field
        if self.last_successful_log_in is None and "last_successful_log_in" in self.__fields_set__:
            _dict['lastSuccessfulLogIn'] = None

        # set to None if avatar (nullable) is None
        # and __fields_set__ contains the field
        if self.avatar is None and "avatar" in self.__fields_set__:
            _dict['avatar'] = None

        # set to None if organization (nullable) is None
        # and __fields_set__ contains the field
        if self.organization is None and "organization" in self.__fields_set__:
            _dict['organization'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserAuthenticatedRead:
        """Create an instance of UserAuthenticatedRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserAuthenticatedRead.parse_obj(obj)

        _obj = UserAuthenticatedRead.parse_obj({
            "id": obj.get("id"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "public_name": obj.get("publicName"),
            "role_in_company": obj.get("roleInCompany"),
            "birthday": obj.get("birthday"),
            "email": obj.get("email"),
            "roles": obj.get("roles"),
            "intl_phone_number": obj.get("intlPhoneNumber"),
            "origin_country": obj.get("originCountry"),
            "preferred_language": obj.get("preferredLanguage"),
            "last_successful_log_in": obj.get("lastSuccessfulLogIn"),
            "avatar": OrganizationAuthenticatedReadIcon.from_dict(obj.get("avatar")) if obj.get("avatar") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "consent_mail_notification": obj.get("consentMailNotification"),
            "consent_mail_ads": obj.get("consentMailAds"),
            "organization": UserAuthenticatedReadOrganization.from_dict(obj.get("organization")) if obj.get("organization") is not None else None
        })
        return _obj

