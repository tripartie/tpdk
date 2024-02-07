# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.177
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from tpdk.models.address_update import AddressUpdate
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrganizationUpdate(BaseModel):
    """
    
    """ # noqa: E501
    name: Annotated[str, Field(strict=True, max_length=64)]
    vat_number: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(alias="vatNumber")
    commercial_registry_number: Annotated[str, Field(strict=True, max_length=32)] = Field(alias="commercialRegistryNumber")
    website_url: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, alias="websiteUrl")
    custom_base_url: Optional[StrictStr] = Field(default=None, alias="customBaseUrl")
    billing_address: Optional[AddressUpdate] = Field(default=None, alias="billingAddress")
    primary_color: Optional[StrictStr] = Field(default=None, alias="primaryColor")
    secondary_color: Optional[StrictStr] = Field(default=None, alias="secondaryColor")
    accent_color: Optional[StrictStr] = Field(default=None, alias="accentColor")
    error_color: Optional[StrictStr] = Field(default=None, alias="errorColor")
    info_color: Optional[StrictStr] = Field(default=None, alias="infoColor")
    success_color: Optional[StrictStr] = Field(default=None, alias="successColor")
    warning_color: Optional[StrictStr] = Field(default=None, alias="warningColor")
    direct_notification_toggle: Optional[StrictBool] = Field(default=True, alias="directNotificationToggle")
    anonymity_level: Optional[StrictStr] = Field(default='PARTIAL_FIRST_NAME', alias="anonymityLevel")
    internal_messaging_toggle: Optional[StrictBool] = Field(default=True, alias="internalMessagingToggle")
    persona_auth_portal_toggle: Optional[StrictBool] = Field(default=None, alias="personaAuthPortalToggle")
    automated_return_toggle: Optional[StrictBool] = Field(default=True, alias="automatedReturnToggle")
    counter_proposal_toggle: Optional[StrictBool] = Field(default=True, alias="counterProposalToggle")
    flat_rate_enabled: Optional[StrictBool] = Field(default=None, alias="flatRateEnabled")
    rate_commission_safe_checkout: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="rateCommissionSafeCheckout")
    __properties: ClassVar[List[str]] = ["name", "vatNumber", "commercialRegistryNumber", "websiteUrl", "customBaseUrl", "billingAddress", "primaryColor", "secondaryColor", "accentColor", "errorColor", "infoColor", "successColor", "warningColor", "directNotificationToggle", "anonymityLevel", "internalMessagingToggle", "personaAuthPortalToggle", "automatedReturnToggle", "counterProposalToggle", "flatRateEnabled", "rateCommissionSafeCheckout"]

    @field_validator('anonymity_level')
    def anonymity_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('COMPLETE', 'PARTIAL_FIRST_NAME', 'TRANSPARENT'):
            raise ValueError("must be one of enum values ('COMPLETE', 'PARTIAL_FIRST_NAME', 'TRANSPARENT')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrganizationUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "flat_rate_enabled",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        # set to None if vat_number (nullable) is None
        # and model_fields_set contains the field
        if self.vat_number is None and "vat_number" in self.model_fields_set:
            _dict['vatNumber'] = None

        # set to None if website_url (nullable) is None
        # and model_fields_set contains the field
        if self.website_url is None and "website_url" in self.model_fields_set:
            _dict['websiteUrl'] = None

        # set to None if custom_base_url (nullable) is None
        # and model_fields_set contains the field
        if self.custom_base_url is None and "custom_base_url" in self.model_fields_set:
            _dict['customBaseUrl'] = None

        # set to None if billing_address (nullable) is None
        # and model_fields_set contains the field
        if self.billing_address is None and "billing_address" in self.model_fields_set:
            _dict['billingAddress'] = None

        # set to None if primary_color (nullable) is None
        # and model_fields_set contains the field
        if self.primary_color is None and "primary_color" in self.model_fields_set:
            _dict['primaryColor'] = None

        # set to None if secondary_color (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_color is None and "secondary_color" in self.model_fields_set:
            _dict['secondaryColor'] = None

        # set to None if accent_color (nullable) is None
        # and model_fields_set contains the field
        if self.accent_color is None and "accent_color" in self.model_fields_set:
            _dict['accentColor'] = None

        # set to None if error_color (nullable) is None
        # and model_fields_set contains the field
        if self.error_color is None and "error_color" in self.model_fields_set:
            _dict['errorColor'] = None

        # set to None if info_color (nullable) is None
        # and model_fields_set contains the field
        if self.info_color is None and "info_color" in self.model_fields_set:
            _dict['infoColor'] = None

        # set to None if success_color (nullable) is None
        # and model_fields_set contains the field
        if self.success_color is None and "success_color" in self.model_fields_set:
            _dict['successColor'] = None

        # set to None if warning_color (nullable) is None
        # and model_fields_set contains the field
        if self.warning_color is None and "warning_color" in self.model_fields_set:
            _dict['warningColor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrganizationUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "vatNumber": obj.get("vatNumber"),
            "commercialRegistryNumber": obj.get("commercialRegistryNumber"),
            "websiteUrl": obj.get("websiteUrl"),
            "customBaseUrl": obj.get("customBaseUrl"),
            "billingAddress": AddressUpdate.from_dict(obj.get("billingAddress")) if obj.get("billingAddress") is not None else None,
            "primaryColor": obj.get("primaryColor"),
            "secondaryColor": obj.get("secondaryColor"),
            "accentColor": obj.get("accentColor"),
            "errorColor": obj.get("errorColor"),
            "infoColor": obj.get("infoColor"),
            "successColor": obj.get("successColor"),
            "warningColor": obj.get("warningColor"),
            "directNotificationToggle": obj.get("directNotificationToggle") if obj.get("directNotificationToggle") is not None else True,
            "anonymityLevel": obj.get("anonymityLevel") if obj.get("anonymityLevel") is not None else 'PARTIAL_FIRST_NAME',
            "internalMessagingToggle": obj.get("internalMessagingToggle") if obj.get("internalMessagingToggle") is not None else True,
            "personaAuthPortalToggle": obj.get("personaAuthPortalToggle"),
            "automatedReturnToggle": obj.get("automatedReturnToggle") if obj.get("automatedReturnToggle") is not None else True,
            "counterProposalToggle": obj.get("counterProposalToggle") if obj.get("counterProposalToggle") is not None else True,
            "flatRateEnabled": obj.get("flatRateEnabled"),
            "rateCommissionSafeCheckout": obj.get("rateCommissionSafeCheckout")
        })
        return _obj


