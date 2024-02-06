# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.172
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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class View(BaseModel):
    """
    
    """ # noqa: E501
    id: Optional[StrictInt] = None
    ip_address: StrictStr = Field(alias="ipAddress")
    offer: Optional[StrictStr] = None
    dispute: Optional[StrictStr] = None
    persona: Optional[StrictStr] = None
    user: Optional[StrictStr] = None
    hit_count: StrictInt = Field(alias="hitCount")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    named_source: Optional[StrictStr] = Field(default=None, alias="namedSource")
    __properties: ClassVar[List[str]] = ["id", "ipAddress", "offer", "dispute", "persona", "user", "hitCount", "createdAt", "namedSource"]

    @field_validator('named_source')
    def named_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BUYER', 'PLATFORM', 'SELLER', 'OTHER'):
            raise ValueError("must be one of enum values ('BUYER', 'PLATFORM', 'SELLER', 'OTHER')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
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
        """Create an instance of View from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "created_at",
                "named_source",
            },
            exclude_none=True,
        )
        # set to None if offer (nullable) is None
        # and model_fields_set contains the field
        if self.offer is None and "offer" in self.model_fields_set:
            _dict['offer'] = None

        # set to None if dispute (nullable) is None
        # and model_fields_set contains the field
        if self.dispute is None and "dispute" in self.model_fields_set:
            _dict['dispute'] = None

        # set to None if persona (nullable) is None
        # and model_fields_set contains the field
        if self.persona is None and "persona" in self.model_fields_set:
            _dict['persona'] = None

        # set to None if user (nullable) is None
        # and model_fields_set contains the field
        if self.user is None and "user" in self.model_fields_set:
            _dict['user'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of View from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "ipAddress": obj.get("ipAddress"),
            "offer": obj.get("offer"),
            "dispute": obj.get("dispute"),
            "persona": obj.get("persona"),
            "user": obj.get("user"),
            "hitCount": obj.get("hitCount") if obj.get("hitCount") is not None else 1,
            "createdAt": obj.get("createdAt"),
            "namedSource": obj.get("namedSource")
        })
        return _obj


