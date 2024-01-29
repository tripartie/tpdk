# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.163
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiClientWrite(BaseModel):
    """
    
    """ # noqa: E501
    reference_name: Optional[Annotated[str, Field(strict=True, max_length=32)]] = Field(alias="referenceName")
    desired_scopes: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, alias="desiredScopes")
    __properties: ClassVar[List[str]] = ["referenceName", "desiredScopes"]

    @field_validator('desired_scopes')
    def desired_scopes_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('OFFER_READ', 'OFFER_WRITE', 'DISPUTE_READ', 'DISPUTE_WRITE', 'ORGANIZATION_READ', 'PERSONA_READ', 'PERSONA_WRITE', 'PERSONA_AUTH'):
                raise ValueError("each list item must be one of ('OFFER_READ', 'OFFER_WRITE', 'DISPUTE_READ', 'DISPUTE_WRITE', 'ORGANIZATION_READ', 'PERSONA_READ', 'PERSONA_WRITE', 'PERSONA_AUTH')")
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
        """Create an instance of ApiClientWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if reference_name (nullable) is None
        # and model_fields_set contains the field
        if self.reference_name is None and "reference_name" in self.model_fields_set:
            _dict['referenceName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApiClientWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "referenceName": obj.get("referenceName"),
            "desiredScopes": obj.get("desiredScopes")
        })
        return _obj


