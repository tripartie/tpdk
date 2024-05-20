# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.194
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WorkflowEventRead(BaseModel):
    """
    
    """ # noqa: E501
    label: StrictStr
    var_from: Optional[StrictStr] = Field(default=None, alias="from")
    to: Optional[StrictStr] = None
    event: Optional[StrictStr] = None
    occurred_at: Optional[datetime] = Field(default=None, alias="occurredAt")
    initiator: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["label", "from", "to", "event", "occurredAt", "initiator"]

    @field_validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.expired', 'dispute.manual_arbitration_required', 'dispute.updated', 'dispute.reminder', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added', 'null']):
            raise ValueError("must be one of enum values ('dispute.opened', 'dispute.submitted', 'dispute.created', 'dispute.abandoned', 'dispute.settlement', 'dispute.closed', 'dispute.expired', 'dispute.manual_arbitration_required', 'dispute.updated', 'dispute.reminder', 'offer.created', 'offer.expired', 'offer.updated', 'offer.crawl_failure', 'offer.transaction.authorized', 'offer.transaction.reconciled', 'offer.transaction.abandoned', 'offer.closed', 'offer.transaction.refund', 'persona.added', 'null')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WorkflowEventRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "occurred_at",
            "initiator",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if var_from (nullable) is None
        # and model_fields_set contains the field
        if self.var_from is None and "var_from" in self.model_fields_set:
            _dict['from'] = None

        # set to None if to (nullable) is None
        # and model_fields_set contains the field
        if self.to is None and "to" in self.model_fields_set:
            _dict['to'] = None

        # set to None if event (nullable) is None
        # and model_fields_set contains the field
        if self.event is None and "event" in self.model_fields_set:
            _dict['event'] = None

        # set to None if initiator (nullable) is None
        # and model_fields_set contains the field
        if self.initiator is None and "initiator" in self.model_fields_set:
            _dict['initiator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkflowEventRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": obj.get("label"),
            "from": obj.get("from"),
            "to": obj.get("to"),
            "event": obj.get("event"),
            "occurredAt": obj.get("occurredAt"),
            "initiator": obj.get("initiator")
        })
        return _obj


