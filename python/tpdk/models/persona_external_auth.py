# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.35
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class PersonaExternalAuth(BaseModel):
    """
    
    """
    captcha: Optional[StrictStr] = None
    target_url: Optional[StrictStr] = Field(None, alias="targetUrl", description="The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona.")
    plain_password: Optional[StrictStr] = Field(None, alias="plainPassword")
    email: Optional[StrictStr] = None
    mobile_phone_number: Optional[StrictStr] = Field(None, alias="mobilePhoneNumber")
    __properties = ["captcha", "targetUrl", "plainPassword", "email", "mobilePhoneNumber"]

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
    def from_json(cls, json_str: str) -> PersonaExternalAuth:
        """Create an instance of PersonaExternalAuth from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if captcha (nullable) is None
        # and __fields_set__ contains the field
        if self.captcha is None and "captcha" in self.__fields_set__:
            _dict['captcha'] = None

        # set to None if target_url (nullable) is None
        # and __fields_set__ contains the field
        if self.target_url is None and "target_url" in self.__fields_set__:
            _dict['targetUrl'] = None

        # set to None if plain_password (nullable) is None
        # and __fields_set__ contains the field
        if self.plain_password is None and "plain_password" in self.__fields_set__:
            _dict['plainPassword'] = None

        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if mobile_phone_number (nullable) is None
        # and __fields_set__ contains the field
        if self.mobile_phone_number is None and "mobile_phone_number" in self.__fields_set__:
            _dict['mobilePhoneNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PersonaExternalAuth:
        """Create an instance of PersonaExternalAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PersonaExternalAuth.parse_obj(obj)

        _obj = PersonaExternalAuth.parse_obj({
            "captcha": obj.get("captcha"),
            "target_url": obj.get("targetUrl"),
            "plain_password": obj.get("plainPassword"),
            "email": obj.get("email"),
            "mobile_phone_number": obj.get("mobilePhoneNumber")
        })
        return _obj

