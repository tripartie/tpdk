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
from tpdk.models.media_user_read import MediaUserRead
from tpdk.models.organization_user_read import OrganizationUserRead
from typing import Optional, Set
from typing_extensions import Self

class UserUserRead(BaseModel):
    """
    
    """ # noqa: E501
    id: Optional[StrictInt] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    public_name: Optional[StrictStr] = Field(default=None, alias="publicName")
    role_in_company: Optional[StrictStr] = Field(default=None, alias="roleInCompany")
    birthday: Optional[datetime] = None
    email: Annotated[str, Field(strict=True, max_length=180)]
    roles: Optional[List[StrictStr]] = None
    totp_enabled: Optional[StrictBool] = Field(default=None, alias="totpEnabled")
    intl_phone_number: Optional[StrictStr] = Field(default=None, alias="intlPhoneNumber")
    origin_country: Optional[StrictStr] = Field(default=None, description="The originating country", alias="originCountry")
    preferred_language: Optional[StrictStr] = Field(default=None, alias="preferredLanguage")
    last_successful_log_in: Optional[datetime] = Field(default=None, alias="lastSuccessfulLogIn")
    avatar: Optional[MediaUserRead] = None
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    consent_mail_notification: Optional[StrictBool] = Field(default=None, alias="consentMailNotification")
    consent_mail_ads: Optional[StrictBool] = Field(default=None, alias="consentMailAds")
    lockdown: Optional[StrictBool] = None
    organization: Optional[OrganizationUserRead] = None
    iri: Optional[StrictStr] = None
    impersonating_organization: Optional[StrictBool] = Field(default=None, alias="impersonatingOrganization")
    var_2fa: Optional[StrictBool] = Field(default=None, alias="2fa")
    __properties: ClassVar[List[str]] = ["id", "firstName", "lastName", "publicName", "roleInCompany", "birthday", "email", "roles", "totpEnabled", "intlPhoneNumber", "originCountry", "preferredLanguage", "lastSuccessfulLogIn", "avatar", "createdAt", "updatedAt", "consentMailNotification", "consentMailAds", "lockdown", "organization", "iri", "impersonatingOrganization", "2fa"]

    @field_validator('roles')
    def roles_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
        """Create an instance of UserUserRead from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_at",
            "updated_at",
            "iri",
            "impersonating_organization",
            "var_2fa",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of avatar
        if self.avatar:
            _dict['avatar'] = self.avatar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
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

        # set to None if avatar (nullable) is None
        # and model_fields_set contains the field
        if self.avatar is None and "avatar" in self.model_fields_set:
            _dict['avatar'] = None

        # set to None if organization (nullable) is None
        # and model_fields_set contains the field
        if self.organization is None and "organization" in self.model_fields_set:
            _dict['organization'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserUserRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "publicName": obj.get("publicName"),
            "roleInCompany": obj.get("roleInCompany"),
            "birthday": obj.get("birthday"),
            "email": obj.get("email"),
            "roles": obj.get("roles"),
            "totpEnabled": obj.get("totpEnabled"),
            "intlPhoneNumber": obj.get("intlPhoneNumber"),
            "originCountry": obj.get("originCountry"),
            "preferredLanguage": obj.get("preferredLanguage"),
            "lastSuccessfulLogIn": obj.get("lastSuccessfulLogIn"),
            "avatar": MediaUserRead.from_dict(obj["avatar"]) if obj.get("avatar") is not None else None,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "consentMailNotification": obj.get("consentMailNotification"),
            "consentMailAds": obj.get("consentMailAds"),
            "lockdown": obj.get("lockdown"),
            "organization": OrganizationUserRead.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "iri": obj.get("iri"),
            "impersonatingOrganization": obj.get("impersonatingOrganization"),
            "2fa": obj.get("2fa")
        })
        return _obj


