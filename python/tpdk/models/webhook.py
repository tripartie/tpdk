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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from tpdk.models.webhook_object import WebhookObject

class Webhook(BaseModel):
    """
    Webhook
    """
    id: Optional[StrictInt] = None
    event: Optional[StrictStr] = None
    object_id: Optional[StrictStr] = Field(None, alias="objectId")
    iri: Optional[StrictStr] = None
    occurred_at: Optional[datetime] = Field(None, alias="occurredAt")
    object: Optional[WebhookObject] = None
    __properties = ["id", "event", "objectId", "iri", "occurredAt", "object"]

    @validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.expired', 'dispute.manual_arbitration_required', 'dispute.updated', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added'):
            raise ValueError("must be one of enum values ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.expired', 'dispute.manual_arbitration_required', 'dispute.updated', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added')")
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
    def from_json(cls, json_str: str) -> Webhook:
        """Create an instance of Webhook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Webhook:
        """Create an instance of Webhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Webhook.parse_obj(obj)

        _obj = Webhook.parse_obj({
            "id": obj.get("id"),
            "event": obj.get("event"),
            "object_id": obj.get("objectId"),
            "iri": obj.get("iri"),
            "occurred_at": obj.get("occurredAt"),
            "object": WebhookObject.from_dict(obj.get("object")) if obj.get("object") is not None else None
        })
        return _obj

