# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.0-b1
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from tpdk.models.address_write import AddressWrite
from typing import Any, List
from pydantic import StrictStr, Field

PERSONAWRITEADDRESS_ANY_OF_SCHEMAS = ["AddressWrite"]

class PersonaWriteAddress(BaseModel):
    """
    Always the Shipping address. Thus enabling automated package returns.
    """

    # data type: AddressWrite
    anyof_schema_1_validator: Optional[AddressWrite] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(PERSONAWRITEADDRESS_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        if v is None:
            return v

        instance = cls()
        error_messages = []
        # validate data type: AddressWrite
        if type(v) is not AddressWrite:
            error_messages.append(f"Error! Input type `{type(v)}` is not `AddressWrite`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PersonaWriteAddress with anyOf schemas: AddressWrite. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> PersonaWriteAddress:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> PersonaWriteAddress:
        """Returns the object represented by the json string"""
        instance = cls()
        if json_str is None:
            return instance

        error_messages = []
        # anyof_schema_1_validator: Optional[AddressWrite] = None
        try:
            instance.actual_instance = AddressWrite.from_json(json_str)
            return instance
        except ValidationError as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PersonaWriteAddress with anyOf schemas: AddressWrite. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

