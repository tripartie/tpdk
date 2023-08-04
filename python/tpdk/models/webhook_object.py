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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from tpdk.models.dispute_read import DisputeRead
from tpdk.models.offer_read import OfferRead
from tpdk.models.persona_read import PersonaRead
from typing import Any, List
from pydantic import StrictStr, Field

WEBHOOKOBJECT_ANY_OF_SCHEMAS = ["DisputeRead", "OfferRead", "PersonaRead"]

class WebhookObject(BaseModel):
    """
    WebhookObject
    """

    # data type: DisputeRead
    anyof_schema_1_validator: Optional[DisputeRead] = None
    # data type: PersonaRead
    anyof_schema_2_validator: Optional[PersonaRead] = None
    # data type: OfferRead
    anyof_schema_3_validator: Optional[OfferRead] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(WEBHOOKOBJECT_ANY_OF_SCHEMAS, const=True)

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
        instance = WebhookObject.construct()
        error_messages = []
        # validate data type: DisputeRead
        if not isinstance(v, DisputeRead):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DisputeRead`")
        else:
            return v

        # validate data type: PersonaRead
        if not isinstance(v, PersonaRead):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PersonaRead`")
        else:
            return v

        # validate data type: OfferRead
        if not isinstance(v, OfferRead):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferRead`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in WebhookObject with anyOf schemas: DisputeRead, OfferRead, PersonaRead. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> WebhookObject:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> WebhookObject:
        """Returns the object represented by the json string"""
        instance = WebhookObject.construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[DisputeRead] = None
        try:
            instance.actual_instance = DisputeRead.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[PersonaRead] = None
        try:
            instance.actual_instance = PersonaRead.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[OfferRead] = None
        try:
            instance.actual_instance = OfferRead.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into WebhookObject with anyOf schemas: DisputeRead, OfferRead, PersonaRead. Details: " + ", ".join(error_messages))
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

