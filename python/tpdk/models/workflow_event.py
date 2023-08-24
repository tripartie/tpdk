# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.52
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class WorkflowEvent(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    label: StrictStr = Field(...)
    var_from: StrictStr = Field(..., alias="from")
    to: Optional[StrictStr] = None
    event: Optional[StrictStr] = None
    user: Optional[StrictStr] = None
    persona: Optional[StrictStr] = None
    dispute: Optional[StrictStr] = None
    occurred_at: Optional[datetime] = Field(None, alias="occurredAt")
    initiator: Optional[StrictStr] = None
    __properties = ["id", "label", "from", "to", "event", "user", "persona", "dispute", "occurredAt", "initiator"]

    @validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.expired', 'dispute.manual_arbitration_required', 'dispute.updated', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added', 'null'):
            raise ValueError("must be one of enum values ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.expired', 'dispute.manual_arbitration_required', 'dispute.updated', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added', 'null')")
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
    def from_json(cls, json_str: str) -> WorkflowEvent:
        """Create an instance of WorkflowEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "occurred_at",
                            "initiator",
                          },
                          exclude_none=True)
        # set to None if to (nullable) is None
        # and __fields_set__ contains the field
        if self.to is None and "to" in self.__fields_set__:
            _dict['to'] = None

        # set to None if event (nullable) is None
        # and __fields_set__ contains the field
        if self.event is None and "event" in self.__fields_set__:
            _dict['event'] = None

        # set to None if user (nullable) is None
        # and __fields_set__ contains the field
        if self.user is None and "user" in self.__fields_set__:
            _dict['user'] = None

        # set to None if persona (nullable) is None
        # and __fields_set__ contains the field
        if self.persona is None and "persona" in self.__fields_set__:
            _dict['persona'] = None

        # set to None if dispute (nullable) is None
        # and __fields_set__ contains the field
        if self.dispute is None and "dispute" in self.__fields_set__:
            _dict['dispute'] = None

        # set to None if initiator (nullable) is None
        # and __fields_set__ contains the field
        if self.initiator is None and "initiator" in self.__fields_set__:
            _dict['initiator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WorkflowEvent:
        """Create an instance of WorkflowEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WorkflowEvent.parse_obj(obj)

        _obj = WorkflowEvent.parse_obj({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "var_from": obj.get("from"),
            "to": obj.get("to"),
            "event": obj.get("event"),
            "user": obj.get("user"),
            "persona": obj.get("persona"),
            "dispute": obj.get("dispute"),
            "occurred_at": obj.get("occurredAt"),
            "initiator": obj.get("initiator")
        })
        return _obj

