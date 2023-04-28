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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from tpdk.models.evidence_read_media import EvidenceReadMedia

class EvidenceRead(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    status: StrictStr = ...
    media: Optional[EvidenceReadMedia] = None
    additional_information: Optional[StrictStr] = Field(None, alias="additionalInformation", description="Description of what the evidence actually is.")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    __properties = ["id", "status", "media", "additionalInformation", "createdAt", "updatedAt"]

    @validator('status')
    def status_validate_enum(cls, v):
        if v not in ('SUBMITTED', 'CORRELATED', 'UNRELATED', 'PENDING', 'TEMPERED', 'REJECTED'):
            raise ValueError("must be one of enum values ('SUBMITTED', 'CORRELATED', 'UNRELATED', 'PENDING', 'TEMPERED', 'REJECTED')")
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
    def from_json(cls, json_str: str) -> EvidenceRead:
        """Create an instance of EvidenceRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "updated_at",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of media
        if self.media:
            _dict['media'] = self.media.to_dict()
        # set to None if media (nullable) is None
        # and __fields_set__ contains the field
        if self.media is None and "media" in self.__fields_set__:
            _dict['media'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EvidenceRead:
        """Create an instance of EvidenceRead from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EvidenceRead.parse_obj(obj)

        _obj = EvidenceRead.parse_obj({
            "id": obj.get("id"),
            "status": obj.get("status") if obj.get("status") is not None else 'SUBMITTED',
            "media": EvidenceReadMedia.from_dict(obj.get("media")) if obj.get("media") is not None else None,
            "additional_information": obj.get("additionalInformation"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

