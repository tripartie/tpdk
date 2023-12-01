# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.139
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from tpdk.models.media_read import MediaRead
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EvidenceRead(BaseModel):
    """
    
    """ # noqa: E501
    id: Optional[StrictInt] = None
    status: StrictStr
    media: Optional[MediaRead] = None
    additional_information: Optional[StrictStr] = Field(default=None, description="Description of what the evidence actually is.", alias="additionalInformation")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    publisher: Optional[StrictStr] = Field(default=None, description="Shortcut to whomever sent the evidence")
    __properties: ClassVar[List[str]] = ["id", "status", "media", "additionalInformation", "createdAt", "updatedAt", "publisher"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SUBMITTED', 'CORRELATED', 'UNRELATED', 'PENDING', 'TEMPERED', 'REJECTED'):
            raise ValueError("must be one of enum values ('SUBMITTED', 'CORRELATED', 'UNRELATED', 'PENDING', 'TEMPERED', 'REJECTED')")
        return value

    @field_validator('publisher')
    def publisher_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BUYER', 'PLATFORM', 'SELLER'):
            raise ValueError("must be one of enum values ('BUYER', 'PLATFORM', 'SELLER')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EvidenceRead from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "created_at",
                "updated_at",
                "publisher",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of media
        if self.media:
            _dict['media'] = self.media.to_dict()
        # set to None if media (nullable) is None
        # and model_fields_set contains the field
        if self.media is None and "media" in self.model_fields_set:
            _dict['media'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EvidenceRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status") if obj.get("status") is not None else 'SUBMITTED',
            "media": MediaRead.from_dict(obj.get("media")) if obj.get("media") is not None else None,
            "additionalInformation": obj.get("additionalInformation"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "publisher": obj.get("publisher")
        })
        return _obj


