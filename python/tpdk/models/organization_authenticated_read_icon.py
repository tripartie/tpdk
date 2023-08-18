# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.48
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
from tpdk.models.media_authenticated_read import MediaAuthenticatedRead
from typing import Any, List
from pydantic import StrictStr, Field

ORGANIZATIONAUTHENTICATEDREADICON_ANY_OF_SCHEMAS = ["MediaAuthenticatedRead"]

class OrganizationAuthenticatedReadIcon(BaseModel):
    """
    OrganizationAuthenticatedReadIcon
    """

    # data type: MediaAuthenticatedRead
    anyof_schema_1_validator: Optional[MediaAuthenticatedRead] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(ORGANIZATIONAUTHENTICATEDREADICON_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        if v is None:
            return v

        instance = OrganizationAuthenticatedReadIcon.construct()
        error_messages = []
        # validate data type: MediaAuthenticatedRead
        if not isinstance(v, MediaAuthenticatedRead):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MediaAuthenticatedRead`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in OrganizationAuthenticatedReadIcon with anyOf schemas: MediaAuthenticatedRead. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationAuthenticatedReadIcon:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> OrganizationAuthenticatedReadIcon:
        """Returns the object represented by the json string"""
        instance = OrganizationAuthenticatedReadIcon.construct()
        if json_str is None:
            return instance

        error_messages = []
        # anyof_schema_1_validator: Optional[MediaAuthenticatedRead] = None
        try:
            instance.actual_instance = MediaAuthenticatedRead.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into OrganizationAuthenticatedReadIcon with anyOf schemas: MediaAuthenticatedRead. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

