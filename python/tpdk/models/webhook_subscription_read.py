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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator

class WebhookSubscriptionRead(BaseModel):
    """
    
    """
    event: StrictStr = ...
    callback_url: constr(strict=True, max_length=5000, min_length=4) = Field(..., alias="callbackUrl")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    __properties = ["event", "callbackUrl", "createdAt"]

    @validator('event')
    def event_validate_enum(cls, v):
        if v not in ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.manual_arbitration_required', 'dispute.updated', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added'):
            raise ValueError("must be one of enum values ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.manual_arbitration_required', 'dispute.updated', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added')")
        return v

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
    def from_json(cls, json_str: str) -> WebhookSubscriptionRead:
        """Create an instance of WebhookSubscriptionRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created_at",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebhookSubscriptionRead:
        """Create an instance of WebhookSubscriptionRead from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return WebhookSubscriptionRead.parse_obj(obj)

        _obj = WebhookSubscriptionRead.parse_obj({
            "event": obj.get("event"),
            "callback_url": obj.get("callbackUrl"),
            "created_at": obj.get("createdAt")
        })
        return _obj

