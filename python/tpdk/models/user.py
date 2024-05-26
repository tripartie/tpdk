# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.202
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tpdk.models.view import View
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    
    """ # noqa: E501
    id: Optional[StrictInt] = None
    captcha: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    public_name: Optional[StrictStr] = Field(default=None, alias="publicName")
    role_in_company: Optional[StrictStr] = Field(default=None, alias="roleInCompany")
    birthday: Optional[datetime] = None
    email: Optional[StrictStr] = None
    invited_role: Optional[List[StrictStr]] = Field(default=None, alias="invitedRole")
    roles: List[StrictStr]
    password: Optional[StrictStr] = Field(default=None, description="The hashed password")
    plain_password: Optional[StrictStr] = Field(default=None, alias="plainPassword")
    new_password: Optional[StrictStr] = Field(default=None, alias="newPassword")
    totp_secret: Optional[StrictStr] = Field(default=None, alias="totpSecret")
    totp_uri: Optional[StrictStr] = Field(default=None, alias="totpUri")
    totp_enabled: Optional[StrictBool] = Field(default=None, alias="totpEnabled")
    totp_challenge: Optional[StrictStr] = Field(default=None, alias="totpChallenge")
    intl_phone_number: Optional[StrictStr] = Field(default=None, alias="intlPhoneNumber")
    origin_country: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, description="The originating country", alias="originCountry")
    preferred_language: Optional[Annotated[str, Field(strict=True, max_length=2)]] = Field(default=None, alias="preferredLanguage")
    last_successful_log_in: Optional[datetime] = Field(default=None, alias="lastSuccessfulLogIn")
    email_verification_code: Optional[StrictStr] = Field(default=None, alias="emailVerificationCode")
    email_verification_input: Optional[StrictStr] = Field(default=None, alias="emailVerificationInput")
    phone_verification_code: Optional[StrictStr] = Field(default=None, alias="phoneVerificationCode")
    phone_verification_input: Optional[StrictStr] = Field(default=None, alias="phoneVerificationInput")
    avatar: Optional[StrictStr] = None
    notifications: Optional[List[StrictStr]] = None
    medias: Optional[List[StrictStr]] = None
    views: List[View]
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    consent_mail_notification: StrictBool = Field(alias="consentMailNotification")
    consent_mail_ads: StrictBool = Field(alias="consentMailAds")
    lockdown: StrictBool
    keys: List[StrictStr]
    organization: Optional[StrictStr] = None
    impersonated_organization: Optional[StrictStr] = Field(default=None, alias="impersonatedOrganization")
    iri: Optional[StrictStr] = None
    username: Optional[StrictStr] = Field(default=None, description="A visual identifier that represents this user.")
    salt: Optional[StrictStr] = None
    user_identifier: Optional[StrictStr] = Field(default=None, alias="userIdentifier")
    impersonating_organization: Optional[StrictBool] = Field(default=None, alias="impersonatingOrganization")
    var_2fa: Optional[StrictBool] = Field(default=None, alias="2fa")
    __properties: ClassVar[List[str]] = ["id", "captcha", "firstName", "lastName", "publicName", "roleInCompany", "birthday", "email", "invitedRole", "roles", "password", "plainPassword", "newPassword", "totpSecret", "totpUri", "totpEnabled", "totpChallenge", "intlPhoneNumber", "originCountry", "preferredLanguage", "lastSuccessfulLogIn", "emailVerificationCode", "emailVerificationInput", "phoneVerificationCode", "phoneVerificationInput", "avatar", "notifications", "medias", "views", "createdAt", "updatedAt", "consentMailNotification", "consentMailAds", "lockdown", "keys", "organization", "impersonatedOrganization", "iri", "username", "salt", "userIdentifier", "impersonatingOrganization", "2fa"]

    @field_validator('invited_role')
    def invited_role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ROLE_ADMIN', 'ROLE_CONSULTANT', 'ROLE_ACCOUNTING_MANAGER', 'ROLE_BILLING_MANAGER', 'ROLE_CUSTOMER_SERVICE', 'ROLE_CUSTOMER_SERVICE', 'ROLE_PLATFORM_ADMIN', 'ROLE_PLATFORM_SUPPORT', 'ROLE_ORGANIZATION_OWNER']):
                raise ValueError("each list item must be one of ('ROLE_ADMIN', 'ROLE_CONSULTANT', 'ROLE_ACCOUNTING_MANAGER', 'ROLE_BILLING_MANAGER', 'ROLE_CUSTOMER_SERVICE', 'ROLE_CUSTOMER_SERVICE', 'ROLE_PLATFORM_ADMIN', 'ROLE_PLATFORM_SUPPORT', 'ROLE_ORGANIZATION_OWNER')")
        return value

    @field_validator('roles')
    def roles_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['ROLE_ORGANIZATION_OWNER', 'ROLE_ADMIN', 'ROLE_CONSULTANT', 'ROLE_ACCOUNTING_MANAGER', 'ROLE_BILLING_MANAGER', 'ROLE_CUSTOMER_SERVICE', 'ROLE_PLATFORM_SUPPORT', 'ROLE_PLATFORM_ADMIN', 'ROLE_USER']):
                raise ValueError("each list item must be one of ('ROLE_ORGANIZATION_OWNER', 'ROLE_ADMIN', 'ROLE_CONSULTANT', 'ROLE_ACCOUNTING_MANAGER', 'ROLE_BILLING_MANAGER', 'ROLE_CUSTOMER_SERVICE', 'ROLE_PLATFORM_SUPPORT', 'ROLE_PLATFORM_ADMIN', 'ROLE_USER')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_at",
            "updated_at",
            "iri",
            "username",
            "salt",
            "user_identifier",
            "impersonating_organization",
            "var_2fa",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item in self.views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['views'] = _items
        # set to None if captcha (nullable) is None
        # and model_fields_set contains the field
        if self.captcha is None and "captcha" in self.model_fields_set:
            _dict['captcha'] = None

        # set to None if public_name (nullable) is None
        # and model_fields_set contains the field
        if self.public_name is None and "public_name" in self.model_fields_set:
            _dict['publicName'] = None

        # set to None if role_in_company (nullable) is None
        # and model_fields_set contains the field
        if self.role_in_company is None and "role_in_company" in self.model_fields_set:
            _dict['roleInCompany'] = None

        # set to None if birthday (nullable) is None
        # and model_fields_set contains the field
        if self.birthday is None and "birthday" in self.model_fields_set:
            _dict['birthday'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if plain_password (nullable) is None
        # and model_fields_set contains the field
        if self.plain_password is None and "plain_password" in self.model_fields_set:
            _dict['plainPassword'] = None

        # set to None if new_password (nullable) is None
        # and model_fields_set contains the field
        if self.new_password is None and "new_password" in self.model_fields_set:
            _dict['newPassword'] = None

        # set to None if totp_secret (nullable) is None
        # and model_fields_set contains the field
        if self.totp_secret is None and "totp_secret" in self.model_fields_set:
            _dict['totpSecret'] = None

        # set to None if totp_uri (nullable) is None
        # and model_fields_set contains the field
        if self.totp_uri is None and "totp_uri" in self.model_fields_set:
            _dict['totpUri'] = None

        # set to None if totp_challenge (nullable) is None
        # and model_fields_set contains the field
        if self.totp_challenge is None and "totp_challenge" in self.model_fields_set:
            _dict['totpChallenge'] = None

        # set to None if intl_phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.intl_phone_number is None and "intl_phone_number" in self.model_fields_set:
            _dict['intlPhoneNumber'] = None

        # set to None if origin_country (nullable) is None
        # and model_fields_set contains the field
        if self.origin_country is None and "origin_country" in self.model_fields_set:
            _dict['originCountry'] = None

        # set to None if preferred_language (nullable) is None
        # and model_fields_set contains the field
        if self.preferred_language is None and "preferred_language" in self.model_fields_set:
            _dict['preferredLanguage'] = None

        # set to None if last_successful_log_in (nullable) is None
        # and model_fields_set contains the field
        if self.last_successful_log_in is None and "last_successful_log_in" in self.model_fields_set:
            _dict['lastSuccessfulLogIn'] = None

        # set to None if email_verification_code (nullable) is None
        # and model_fields_set contains the field
        if self.email_verification_code is None and "email_verification_code" in self.model_fields_set:
            _dict['emailVerificationCode'] = None

        # set to None if email_verification_input (nullable) is None
        # and model_fields_set contains the field
        if self.email_verification_input is None and "email_verification_input" in self.model_fields_set:
            _dict['emailVerificationInput'] = None

        # set to None if phone_verification_code (nullable) is None
        # and model_fields_set contains the field
        if self.phone_verification_code is None and "phone_verification_code" in self.model_fields_set:
            _dict['phoneVerificationCode'] = None

        # set to None if phone_verification_input (nullable) is None
        # and model_fields_set contains the field
        if self.phone_verification_input is None and "phone_verification_input" in self.model_fields_set:
            _dict['phoneVerificationInput'] = None

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if organization (nullable) is None
        # and model_fields_set contains the field
        if self.organization is None and "organization" in self.model_fields_set:
            _dict['organization'] = None

        # set to None if impersonated_organization (nullable) is None
        # and model_fields_set contains the field
        if self.impersonated_organization is None and "impersonated_organization" in self.model_fields_set:
            _dict['impersonatedOrganization'] = None

        # set to None if salt (nullable) is None
        # and model_fields_set contains the field
        if self.salt is None and "salt" in self.model_fields_set:
            _dict['salt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "captcha": obj.get("captcha"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "publicName": obj.get("publicName"),
            "roleInCompany": obj.get("roleInCompany"),
            "birthday": obj.get("birthday"),
            "email": obj.get("email"),
            "invitedRole": obj.get("invitedRole"),
            "roles": obj.get("roles"),
            "password": obj.get("password"),
            "plainPassword": obj.get("plainPassword"),
            "newPassword": obj.get("newPassword"),
            "totpSecret": obj.get("totpSecret"),
            "totpUri": obj.get("totpUri"),
            "totpEnabled": obj.get("totpEnabled"),
            "totpChallenge": obj.get("totpChallenge"),
            "intlPhoneNumber": obj.get("intlPhoneNumber"),
            "originCountry": obj.get("originCountry"),
            "preferredLanguage": obj.get("preferredLanguage"),
            "lastSuccessfulLogIn": obj.get("lastSuccessfulLogIn"),
            "emailVerificationCode": obj.get("emailVerificationCode"),
            "emailVerificationInput": obj.get("emailVerificationInput"),
            "phoneVerificationCode": obj.get("phoneVerificationCode"),
            "phoneVerificationInput": obj.get("phoneVerificationInput"),
            "avatar": obj.get("avatar"),
            "notifications": obj.get("notifications"),
            "medias": obj.get("medias"),
            "views": [View.from_dict(_item) for _item in obj["views"]] if obj.get("views") is not None else None,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "consentMailNotification": obj.get("consentMailNotification"),
            "consentMailAds": obj.get("consentMailAds"),
            "lockdown": obj.get("lockdown"),
            "keys": obj.get("keys"),
            "organization": obj.get("organization"),
            "impersonatedOrganization": obj.get("impersonatedOrganization"),
            "iri": obj.get("iri"),
            "username": obj.get("username"),
            "salt": obj.get("salt"),
            "userIdentifier": obj.get("userIdentifier"),
            "impersonatingOrganization": obj.get("impersonatingOrganization"),
            "2fa": obj.get("2fa")
        })
        return _obj


