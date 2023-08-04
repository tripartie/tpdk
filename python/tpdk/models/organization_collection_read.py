# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.28
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
from tpdk.models.organization_collection_read_icon import OrganizationCollectionReadIcon

class OrganizationCollectionRead(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    vat_number: Optional[StrictStr] = Field(None, alias="vatNumber")
    commercial_registry_number: Optional[StrictStr] = Field(None, alias="commercialRegistryNumber")
    website_url: Optional[StrictStr] = Field(None, alias="websiteUrl")
    icon: Optional[OrganizationCollectionReadIcon] = None
    logo: Optional[OrganizationCollectionReadIcon] = None
    direct_notification_toggle: StrictBool = Field(..., alias="directNotificationToggle")
    safe_checkout_toggle: StrictBool = Field(..., alias="safeCheckoutToggle")
    resolution_center_toggle: StrictBool = Field(..., alias="resolutionCenterToggle")
    internal_messaging_toggle: StrictBool = Field(..., alias="internalMessagingToggle")
    persona_auth_portal_toggle: StrictBool = Field(..., alias="personaAuthPortalToggle")
    automated_return_toggle: StrictBool = Field(..., alias="automatedReturnToggle")
    flat_rate_enabled: Optional[StrictBool] = Field(None, alias="flatRateEnabled")
    rate_commission_safe_checkout: Union[StrictFloat, StrictInt] = Field(..., alias="rateCommissionSafeCheckout")
    __properties = ["id", "name", "vatNumber", "commercialRegistryNumber", "websiteUrl", "icon", "logo", "directNotificationToggle", "safeCheckoutToggle", "resolutionCenterToggle", "internalMessagingToggle", "personaAuthPortalToggle", "automatedReturnToggle", "flatRateEnabled", "rateCommissionSafeCheckout"]

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
    def from_json(cls, json_str: str) -> OrganizationCollectionRead:
        """Create an instance of OrganizationCollectionRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "flat_rate_enabled",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of icon
        if self.icon:
            _dict['icon'] = self.icon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # set to None if vat_number (nullable) is None
        # and __fields_set__ contains the field
        if self.vat_number is None and "vat_number" in self.__fields_set__:
            _dict['vatNumber'] = None

        # set to None if website_url (nullable) is None
        # and __fields_set__ contains the field
        if self.website_url is None and "website_url" in self.__fields_set__:
            _dict['websiteUrl'] = None

        # set to None if icon (nullable) is None
        # and __fields_set__ contains the field
        if self.icon is None and "icon" in self.__fields_set__:
            _dict['icon'] = None

        # set to None if logo (nullable) is None
        # and __fields_set__ contains the field
        if self.logo is None and "logo" in self.__fields_set__:
            _dict['logo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationCollectionRead:
        """Create an instance of OrganizationCollectionRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrganizationCollectionRead.parse_obj(obj)

        _obj = OrganizationCollectionRead.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "vat_number": obj.get("vatNumber"),
            "commercial_registry_number": obj.get("commercialRegistryNumber"),
            "website_url": obj.get("websiteUrl"),
            "icon": OrganizationCollectionReadIcon.from_dict(obj.get("icon")) if obj.get("icon") is not None else None,
            "logo": OrganizationCollectionReadIcon.from_dict(obj.get("logo")) if obj.get("logo") is not None else None,
            "direct_notification_toggle": obj.get("directNotificationToggle") if obj.get("directNotificationToggle") is not None else True,
            "safe_checkout_toggle": obj.get("safeCheckoutToggle"),
            "resolution_center_toggle": obj.get("resolutionCenterToggle") if obj.get("resolutionCenterToggle") is not None else True,
            "internal_messaging_toggle": obj.get("internalMessagingToggle") if obj.get("internalMessagingToggle") is not None else True,
            "persona_auth_portal_toggle": obj.get("personaAuthPortalToggle"),
            "automated_return_toggle": obj.get("automatedReturnToggle") if obj.get("automatedReturnToggle") is not None else True,
            "flat_rate_enabled": obj.get("flatRateEnabled"),
            "rate_commission_safe_checkout": obj.get("rateCommissionSafeCheckout")
        })
        return _obj

