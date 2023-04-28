# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0-b2
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictStr, validator
from tpdk.models.organization_update_billing_address import OrganizationUpdateBillingAddress

class OrganizationUpdate(BaseModel):
    """
    
    """
    name: Optional[StrictStr] = None
    vat_number: Optional[StrictStr] = Field(None, alias="vatNumber")
    commercial_registry_number: Optional[StrictStr] = Field(None, alias="commercialRegistryNumber")
    website_url: Optional[StrictStr] = Field(None, alias="websiteUrl")
    custom_base_url: Optional[StrictStr] = Field(None, alias="customBaseUrl")
    billing_address: Optional[OrganizationUpdateBillingAddress] = Field(None, alias="billingAddress")
    primary_color: Optional[StrictStr] = Field(None, alias="primaryColor")
    secondary_color: Optional[StrictStr] = Field(None, alias="secondaryColor")
    accent_color: Optional[StrictStr] = Field(None, alias="accentColor")
    error_color: Optional[StrictStr] = Field(None, alias="errorColor")
    info_color: Optional[StrictStr] = Field(None, alias="infoColor")
    success_color: Optional[StrictStr] = Field(None, alias="successColor")
    warning_color: Optional[StrictStr] = Field(None, alias="warningColor")
    end_user_notification_toggle: StrictBool = Field(..., alias="endUserNotificationToggle")
    anonymity_level: StrictStr = Field(..., alias="anonymityLevel")
    flat_rate_enabled: Optional[StrictBool] = Field(None, alias="flatRateEnabled")
    rate_commission_safe_checkout: StrictFloat = Field(..., alias="rateCommissionSafeCheckout")
    __properties = ["name", "vatNumber", "commercialRegistryNumber", "websiteUrl", "customBaseUrl", "billingAddress", "primaryColor", "secondaryColor", "accentColor", "errorColor", "infoColor", "successColor", "warningColor", "endUserNotificationToggle", "anonymityLevel", "flatRateEnabled", "rateCommissionSafeCheckout"]

    @validator('anonymity_level')
    def anonymity_level_validate_enum(cls, v):
        if v not in ('COMPLETE', 'PARTIAL_FIRST_NAME', 'TRANSPARENT'):
            raise ValueError("must be one of enum values ('COMPLETE', 'PARTIAL_FIRST_NAME', 'TRANSPARENT')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OrganizationUpdate:
        """Create an instance of OrganizationUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "flat_rate_enabled",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        # set to None if vat_number (nullable) is None
        # and __fields_set__ contains the field
        if self.vat_number is None and "vat_number" in self.__fields_set__:
            _dict['vatNumber'] = None

        # set to None if website_url (nullable) is None
        # and __fields_set__ contains the field
        if self.website_url is None and "website_url" in self.__fields_set__:
            _dict['websiteUrl'] = None

        # set to None if custom_base_url (nullable) is None
        # and __fields_set__ contains the field
        if self.custom_base_url is None and "custom_base_url" in self.__fields_set__:
            _dict['customBaseUrl'] = None

        # set to None if billing_address (nullable) is None
        # and __fields_set__ contains the field
        if self.billing_address is None and "billing_address" in self.__fields_set__:
            _dict['billingAddress'] = None

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
    def from_dict(cls, obj: dict) -> OrganizationUpdate:
        """Create an instance of OrganizationUpdate from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrganizationUpdate.parse_obj(obj)

        _obj = OrganizationUpdate.parse_obj({
            "name": obj.get("name"),
            "vat_number": obj.get("vatNumber"),
            "commercial_registry_number": obj.get("commercialRegistryNumber"),
            "website_url": obj.get("websiteUrl"),
            "custom_base_url": obj.get("customBaseUrl"),
            "billing_address": OrganizationUpdateBillingAddress.from_dict(obj.get("billingAddress")) if obj.get("billingAddress") is not None else None,
            "primary_color": obj.get("primaryColor"),
            "secondary_color": obj.get("secondaryColor"),
            "accent_color": obj.get("accentColor"),
            "error_color": obj.get("errorColor"),
            "info_color": obj.get("infoColor"),
            "success_color": obj.get("successColor"),
            "warning_color": obj.get("warningColor"),
            "end_user_notification_toggle": obj.get("endUserNotificationToggle"),
            "anonymity_level": obj.get("anonymityLevel") if obj.get("anonymityLevel") is not None else 'PARTIAL_FIRST_NAME',
            "flat_rate_enabled": obj.get("flatRateEnabled"),
            "rate_commission_safe_checkout": obj.get("rateCommissionSafeCheckout")
        })
        return _obj

