# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0.b1
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
from pydantic import BaseModel, Field, StrictStr

class AddressWrite(BaseModel):
    """
    
    """
    company_name: Optional[StrictStr] = Field(None, alias="companyName")
    country_code: Optional[StrictStr] = Field(None, alias="countryCode")
    zip_code: Optional[StrictStr] = Field(None, alias="zipCode")
    city_name: Optional[StrictStr] = Field(None, alias="cityName")
    first_line: Optional[StrictStr] = Field(None, alias="firstLine")
    second_line: Optional[StrictStr] = Field(None, alias="secondLine")
    building_name: Optional[StrictStr] = Field(None, alias="buildingName")
    building_floor: Optional[StrictStr] = Field(None, alias="buildingFloor")
    gate_or_portal_or_inbox_code: Optional[StrictStr] = Field(None, alias="gateOrPortalOrInboxCode")
    __properties = ["companyName", "countryCode", "zipCode", "cityName", "firstLine", "secondLine", "buildingName", "buildingFloor", "gateOrPortalOrInboxCode"]

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
    def from_json(cls, json_str: str) -> AddressWrite:
        """Create an instance of AddressWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if company_name (nullable) is None
        # and __fields_set__ contains the field
        if self.company_name is None and "company_name" in self.__fields_set__:
            _dict['companyName'] = None

        # set to None if country_code (nullable) is None
        # and __fields_set__ contains the field
        if self.country_code is None and "country_code" in self.__fields_set__:
            _dict['countryCode'] = None

        # set to None if second_line (nullable) is None
        # and __fields_set__ contains the field
        if self.second_line is None and "second_line" in self.__fields_set__:
            _dict['secondLine'] = None

        # set to None if building_name (nullable) is None
        # and __fields_set__ contains the field
        if self.building_name is None and "building_name" in self.__fields_set__:
            _dict['buildingName'] = None

        # set to None if building_floor (nullable) is None
        # and __fields_set__ contains the field
        if self.building_floor is None and "building_floor" in self.__fields_set__:
            _dict['buildingFloor'] = None

        # set to None if gate_or_portal_or_inbox_code (nullable) is None
        # and __fields_set__ contains the field
        if self.gate_or_portal_or_inbox_code is None and "gate_or_portal_or_inbox_code" in self.__fields_set__:
            _dict['gateOrPortalOrInboxCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddressWrite:
        """Create an instance of AddressWrite from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AddressWrite.parse_obj(obj)

        _obj = AddressWrite.parse_obj({
            "company_name": obj.get("companyName"),
            "country_code": obj.get("countryCode"),
            "zip_code": obj.get("zipCode"),
            "city_name": obj.get("cityName"),
            "first_line": obj.get("firstLine"),
            "second_line": obj.get("secondLine"),
            "building_name": obj.get("buildingName"),
            "building_floor": obj.get("buildingFloor"),
            "gate_or_portal_or_inbox_code": obj.get("gateOrPortalOrInboxCode")
        })
        return _obj
