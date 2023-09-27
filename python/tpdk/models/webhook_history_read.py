# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.75
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator

class WebhookHistoryRead(BaseModel):
    """
      # noqa: E501
    """
    id: Optional[StrictInt] = None
    object_id: Optional[StrictStr] = Field(None, alias="objectId")
    event: StrictStr = Field(...)
    url: StrictStr = Field(...)
    normalized_object: Optional[conlist(StrictStr)] = Field(None, alias="normalizedObject")
    response_code: Optional[StrictInt] = Field(None, alias="responseCode")
    response_body: Optional[StrictStr] = Field(None, alias="responseBody")
    occurred_at: datetime = Field(..., alias="occurredAt")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    attempted_at: Optional[datetime] = Field(None, alias="attemptedAt")
    retry_count: StrictInt = Field(..., alias="retryCount")
    in_progress: Optional[StrictBool] = Field(None, alias="inProgress")
    __properties = ["id", "objectId", "event", "url", "normalizedObject", "responseCode", "responseBody", "occurredAt", "createdAt", "attemptedAt", "retryCount", "inProgress"]

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
    def from_json(cls, json_str: str) -> WebhookHistoryRead:
        """Create an instance of WebhookHistoryRead from a JSON string"""
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

        # set to None if normalized_object (nullable) is None
        # and __fields_set__ contains the field
        if self.normalized_object is None and "normalized_object" in self.__fields_set__:
            _dict['normalizedObject'] = None

        # set to None if response_code (nullable) is None
        # and __fields_set__ contains the field
        if self.response_code is None and "response_code" in self.__fields_set__:
            _dict['responseCode'] = None

        # set to None if response_body (nullable) is None
        # and __fields_set__ contains the field
        if self.response_body is None and "response_body" in self.__fields_set__:
            _dict['responseBody'] = None

        # set to None if attempted_at (nullable) is None
        # and __fields_set__ contains the field
        if self.attempted_at is None and "attempted_at" in self.__fields_set__:
            _dict['attemptedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WebhookHistoryRead:
        """Create an instance of WebhookHistoryRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WebhookHistoryRead.parse_obj(obj)

        _obj = WebhookHistoryRead.parse_obj({
            "id": obj.get("id"),
            "object_id": obj.get("objectId"),
            "event": obj.get("event"),
            "url": obj.get("url"),
            "normalized_object": obj.get("normalizedObject"),
            "response_code": obj.get("responseCode"),
            "response_body": obj.get("responseBody"),
            "occurred_at": obj.get("occurredAt"),
            "created_at": obj.get("createdAt"),
            "attempted_at": obj.get("attemptedAt"),
            "retry_count": obj.get("retryCount"),
            "in_progress": obj.get("inProgress")
        })
        return _obj


