# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.199
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from tpdk.models.user_media_read import UserMediaRead
from typing import Optional, Set
from typing_extensions import Self

class UserOrganizationRead(BaseModel):
    """
    
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Annotated[str, Field(strict=True, max_length=64)]
    domain_verified: Optional[StrictBool] = Field(default=None, alias="domainVerified")
    icon: Optional[UserMediaRead] = None
    logo: Optional[UserMediaRead] = None
    safe_checkout_toggle: Optional[StrictBool] = Field(default=None, alias="safeCheckoutToggle")
    resolution_center_toggle: Optional[StrictBool] = Field(default=True, alias="resolutionCenterToggle")
    internal_messaging_toggle: Optional[StrictBool] = Field(default=True, alias="internalMessagingToggle")
    persona_auth_portal_toggle: Optional[StrictBool] = Field(default=None, alias="personaAuthPortalToggle")
    automated_return_toggle: Optional[StrictBool] = Field(default=True, alias="automatedReturnToggle")
    counter_proposal_toggle: Optional[StrictBool] = Field(default=True, alias="counterProposalToggle")
    flat_rate_enabled: Optional[StrictBool] = Field(default=None, alias="flatRateEnabled")
    rate_commission_safe_checkout: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="rateCommissionSafeCheckout")
    __properties: ClassVar[List[str]] = ["id", "name", "domainVerified", "icon", "logo", "safeCheckoutToggle", "resolutionCenterToggle", "internalMessagingToggle", "personaAuthPortalToggle", "automatedReturnToggle", "counterProposalToggle", "flatRateEnabled", "rateCommissionSafeCheckout"]

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
        """Create an instance of UserOrganizationRead from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "flat_rate_enabled",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of icon
        if self.icon:
            _dict['icon'] = self.icon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if logo (nullable) is None
        # and model_fields_set contains the field
        if self.logo is None and "logo" in self.model_fields_set:
            _dict['logo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserOrganizationRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "domainVerified": obj.get("domainVerified"),
            "icon": UserMediaRead.from_dict(obj["icon"]) if obj.get("icon") is not None else None,
            "logo": UserMediaRead.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "safeCheckoutToggle": obj.get("safeCheckoutToggle"),
            "resolutionCenterToggle": obj.get("resolutionCenterToggle") if obj.get("resolutionCenterToggle") is not None else True,
            "internalMessagingToggle": obj.get("internalMessagingToggle") if obj.get("internalMessagingToggle") is not None else True,
            "personaAuthPortalToggle": obj.get("personaAuthPortalToggle"),
            "automatedReturnToggle": obj.get("automatedReturnToggle") if obj.get("automatedReturnToggle") is not None else True,
            "counterProposalToggle": obj.get("counterProposalToggle") if obj.get("counterProposalToggle") is not None else True,
            "flatRateEnabled": obj.get("flatRateEnabled"),
            "rateCommissionSafeCheckout": obj.get("rateCommissionSafeCheckout")
        })
        return _obj


