# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.49
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from tpdk.models.evidence_read_media import EvidenceReadMedia

class OrganizationRead(BaseModel):
    """
    
    """
    name: Optional[StrictStr] = None
    website_url: Optional[StrictStr] = Field(None, alias="websiteUrl")
    custom_base_url: Optional[StrictStr] = Field(None, alias="customBaseUrl")
    icon: Optional[EvidenceReadMedia] = None
    logo: Optional[EvidenceReadMedia] = None
    primary_color: Optional[StrictStr] = Field(None, alias="primaryColor")
    secondary_color: Optional[StrictStr] = Field(None, alias="secondaryColor")
    accent_color: Optional[StrictStr] = Field(None, alias="accentColor")
    error_color: Optional[StrictStr] = Field(None, alias="errorColor")
    info_color: Optional[StrictStr] = Field(None, alias="infoColor")
    success_color: Optional[StrictStr] = Field(None, alias="successColor")
    warning_color: Optional[StrictStr] = Field(None, alias="warningColor")
    direct_notification_toggle: StrictBool = Field(..., alias="directNotificationToggle")
    persona_auth_portal_toggle: StrictBool = Field(..., alias="personaAuthPortalToggle")
    flat_rate_enabled: Optional[StrictBool] = Field(None, alias="flatRateEnabled")
    rate_commission_safe_checkout: Union[StrictFloat, StrictInt] = Field(..., alias="rateCommissionSafeCheckout")
    __properties = ["name", "websiteUrl", "customBaseUrl", "icon", "logo", "primaryColor", "secondaryColor", "accentColor", "errorColor", "infoColor", "successColor", "warningColor", "directNotificationToggle", "personaAuthPortalToggle", "flatRateEnabled", "rateCommissionSafeCheckout"]

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
    def from_json(cls, json_str: str) -> OrganizationRead:
        """Create an instance of OrganizationRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "flat_rate_enabled",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of icon
        if self.icon:
            _dict['icon'] = self.icon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # set to None if website_url (nullable) is None
        # and __fields_set__ contains the field
        if self.website_url is None and "website_url" in self.__fields_set__:
            _dict['websiteUrl'] = None

        # set to None if custom_base_url (nullable) is None
        # and __fields_set__ contains the field
        if self.custom_base_url is None and "custom_base_url" in self.__fields_set__:
            _dict['customBaseUrl'] = None

        # set to None if icon (nullable) is None
        # and __fields_set__ contains the field
        if self.icon is None and "icon" in self.__fields_set__:
            _dict['icon'] = None

        # set to None if logo (nullable) is None
        # and __fields_set__ contains the field
        if self.logo is None and "logo" in self.__fields_set__:
            _dict['logo'] = None

        # set to None if primary_color (nullable) is None
        # and __fields_set__ contains the field
        if self.primary_color is None and "primary_color" in self.__fields_set__:
            _dict['primaryColor'] = None

        # set to None if secondary_color (nullable) is None
        # and __fields_set__ contains the field
        if self.secondary_color is None and "secondary_color" in self.__fields_set__:
            _dict['secondaryColor'] = None

        # set to None if accent_color (nullable) is None
        # and __fields_set__ contains the field
        if self.accent_color is None and "accent_color" in self.__fields_set__:
            _dict['accentColor'] = None

        # set to None if error_color (nullable) is None
        # and __fields_set__ contains the field
        if self.error_color is None and "error_color" in self.__fields_set__:
            _dict['errorColor'] = None

        # set to None if info_color (nullable) is None
        # and __fields_set__ contains the field
        if self.info_color is None and "info_color" in self.__fields_set__:
            _dict['infoColor'] = None

        # set to None if success_color (nullable) is None
        # and __fields_set__ contains the field
        if self.success_color is None and "success_color" in self.__fields_set__:
            _dict['successColor'] = None

        # set to None if warning_color (nullable) is None
        # and __fields_set__ contains the field
        if self.warning_color is None and "warning_color" in self.__fields_set__:
            _dict['warningColor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationRead:
        """Create an instance of OrganizationRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrganizationRead.parse_obj(obj)

        _obj = OrganizationRead.parse_obj({
            "name": obj.get("name"),
            "website_url": obj.get("websiteUrl"),
            "custom_base_url": obj.get("customBaseUrl"),
            "icon": EvidenceReadMedia.from_dict(obj.get("icon")) if obj.get("icon") is not None else None,
            "logo": EvidenceReadMedia.from_dict(obj.get("logo")) if obj.get("logo") is not None else None,
            "primary_color": obj.get("primaryColor"),
            "secondary_color": obj.get("secondaryColor"),
            "accent_color": obj.get("accentColor"),
            "error_color": obj.get("errorColor"),
            "info_color": obj.get("infoColor"),
            "success_color": obj.get("successColor"),
            "warning_color": obj.get("warningColor"),
            "direct_notification_toggle": obj.get("directNotificationToggle") if obj.get("directNotificationToggle") is not None else True,
            "persona_auth_portal_toggle": obj.get("personaAuthPortalToggle"),
            "flat_rate_enabled": obj.get("flatRateEnabled"),
            "rate_commission_safe_checkout": obj.get("rateCommissionSafeCheckout")
        })
        return _obj

