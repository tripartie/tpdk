# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.204
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tpdk.models.user_address_write import UserAddressWrite
from typing import Optional, Set
from typing_extensions import Self

class UserOrganizationWrite(BaseModel):
    """
    
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Annotated[str, Field(strict=True, max_length=64)]
    vat_number: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, alias="vatNumber")
    commercial_registry_number: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(default=None, alias="commercialRegistryNumber")
    website_url: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, alias="websiteUrl")
    billing_address: Optional[UserAddressWrite] = Field(default=None, alias="billingAddress")
    __properties: ClassVar[List[str]] = ["id", "name", "vatNumber", "commercialRegistryNumber", "websiteUrl", "billingAddress"]

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
        """Create an instance of UserOrganizationWrite from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
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

        # set to None if billing_address (nullable) is None
        # and model_fields_set contains the field
        if self.billing_address is None and "billing_address" in self.model_fields_set:
            _dict['billingAddress'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserOrganizationWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "vatNumber": obj.get("vatNumber"),
            "commercialRegistryNumber": obj.get("commercialRegistryNumber"),
            "websiteUrl": obj.get("websiteUrl"),
            "billingAddress": UserAddressWrite.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None
        })
        return _obj


