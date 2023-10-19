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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from tpdk.models.address_write import AddressWrite

class OrganizationWrite(BaseModel):
    """
      # noqa: E501
    """
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    vat_number: Optional[StrictStr] = Field(None, alias="vatNumber")
    commercial_registry_number: Optional[StrictStr] = Field(None, alias="commercialRegistryNumber")
    website_url: Optional[StrictStr] = Field(None, alias="websiteUrl")
    billing_address: Optional[AddressWrite] = Field(None, alias="billingAddress")
    __properties = ["id", "name", "vatNumber", "commercialRegistryNumber", "websiteUrl", "billingAddress"]

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
    def from_json(cls, json_str: str) -> OrganizationWrite:
        """Create an instance of OrganizationWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
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

        # set to None if billing_address (nullable) is None
        # and __fields_set__ contains the field
        if self.billing_address is None and "billing_address" in self.__fields_set__:
            _dict['billingAddress'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationWrite:
        """Create an instance of OrganizationWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrganizationWrite.parse_obj(obj)

        _obj = OrganizationWrite.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "vat_number": obj.get("vatNumber"),
            "commercial_registry_number": obj.get("commercialRegistryNumber"),
            "website_url": obj.get("websiteUrl"),
            "billing_address": AddressWrite.from_dict(obj.get("billingAddress")) if obj.get("billingAddress") is not None else None
        })
        return _obj


