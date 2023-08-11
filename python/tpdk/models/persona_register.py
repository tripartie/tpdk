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

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator

class PersonaRegister(BaseModel):
    """
    
    """
    captcha: Optional[StrictStr] = None
    plain_password: Optional[constr(strict=True, max_length=64, min_length=6)] = Field(None, alias="plainPassword")
    first_name: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="firstName")
    last_name: constr(strict=True, max_length=64, min_length=1) = Field(..., alias="lastName")
    gender: StrictStr = Field(...)
    date_of_birth: Optional[date] = Field(None, alias="dateOfBirth")
    language: Optional[StrictStr] = Field(None, description="That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements.")
    email: Optional[StrictStr] = None
    mobile_phone_number: Optional[StrictStr] = Field(None, alias="mobilePhoneNumber")
    __properties = ["captcha", "plainPassword", "firstName", "lastName", "gender", "dateOfBirth", "language", "email", "mobilePhoneNumber"]

    @validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY'):
            raise ValueError("must be one of enum values ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY')")
        return value

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
    def from_json(cls, json_str: str) -> PersonaRegister:
        """Create an instance of PersonaRegister from a JSON string"""
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

        # set to None if plain_password (nullable) is None
        # and __fields_set__ contains the field
        if self.plain_password is None and "plain_password" in self.__fields_set__:
            _dict['plainPassword'] = None

        # set to None if date_of_birth (nullable) is None
        # and __fields_set__ contains the field
        if self.date_of_birth is None and "date_of_birth" in self.__fields_set__:
            _dict['dateOfBirth'] = None

        # set to None if language (nullable) is None
        # and __fields_set__ contains the field
        if self.language is None and "language" in self.__fields_set__:
            _dict['language'] = None

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
    def from_dict(cls, obj: dict) -> PersonaRegister:
        """Create an instance of PersonaRegister from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PersonaRegister.parse_obj(obj)

        _obj = PersonaRegister.parse_obj({
            "captcha": obj.get("captcha"),
            "plain_password": obj.get("plainPassword"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "gender": obj.get("gender") if obj.get("gender") is not None else 'RATHER_NOT_SAY',
            "date_of_birth": obj.get("dateOfBirth"),
            "language": obj.get("language"),
            "email": obj.get("email"),
            "mobile_phone_number": obj.get("mobilePhoneNumber")
        })
        return _obj

