# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.92
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class WebhookHistoryCollectionRead(BaseModel):
    """
      # noqa: E501
    """
    id: Optional[StrictInt] = None
    object_id: Optional[StrictStr] = Field(None, alias="objectId")
    event: StrictStr = Field(...)
    response_code: Optional[StrictInt] = Field(None, alias="responseCode")
    occurred_at: datetime = Field(..., alias="occurredAt")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    attempted_at: Optional[datetime] = Field(None, alias="attemptedAt")
    retry_count: StrictInt = Field(..., alias="retryCount")
    in_progress: Optional[StrictBool] = Field(None, alias="inProgress")
    __properties = ["id", "objectId", "event", "responseCode", "occurredAt", "createdAt", "attemptedAt", "retryCount", "inProgress"]

    @validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.expired', 'dispute.manual_arbitration_required', 'dispute.updated', 'dispute.reminder', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added'):
            raise ValueError("must be one of enum values ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.expired', 'dispute.manual_arbitration_required', 'dispute.updated', 'dispute.reminder', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added')")
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
    def from_json(cls, json_str: str) -> WebhookHistoryCollectionRead:
        """Create an instance of WebhookHistoryCollectionRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "attempted_at",
                            "in_progress",
                          },
                          exclude_none=True)
        # set to None if object_id (nullable) is None
        # and __fields_set__ contains the field
        if self.object_id is None and "object_id" in self.__fields_set__:
            _dict['objectId'] = None

        # set to None if response_code (nullable) is None
        # and __fields_set__ contains the field
        if self.response_code is None and "response_code" in self.__fields_set__:
            _dict['responseCode'] = None

        # set to None if attempted_at (nullable) is None
        # and __fields_set__ contains the field
        if self.attempted_at is None and "attempted_at" in self.__fields_set__:
            _dict['attemptedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebhookHistoryCollectionRead:
        """Create an instance of WebhookHistoryCollectionRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebhookHistoryCollectionRead.parse_obj(obj)

        _obj = WebhookHistoryCollectionRead.parse_obj({
            "id": obj.get("id"),
            "object_id": obj.get("objectId"),
            "event": obj.get("event"),
            "response_code": obj.get("responseCode"),
            "occurred_at": obj.get("occurredAt"),
            "created_at": obj.get("createdAt"),
            "attempted_at": obj.get("attemptedAt"),
            "retry_count": obj.get("retryCount"),
            "in_progress": obj.get("inProgress")
        })
        return _obj


