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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PersonaAuthReturn(BaseModel):
    """
    
    """ # noqa: E501
    auth_url: Optional[StrictStr] = Field(default=None, description="Url that is able to bypass MFA for a single user. Please note that this should not be shared between the complainant and the seller or anyone external to them.", alias="authUrl")
    expire_at: Optional[datetime] = Field(default=None, description="This authenticated-URL cannot be renewed, you will have to re-create one each time. Typically valid for a single hour.", alias="expireAt")
    __properties: ClassVar[List[str]] = ["authUrl", "expireAt"]

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
        """Create an instance of PersonaAuthReturn from a JSON string"""
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
        # set to None if auth_url (nullable) is None
        # and model_fields_set contains the field
        if self.auth_url is None and "auth_url" in self.model_fields_set:
            _dict['authUrl'] = None

        # set to None if expire_at (nullable) is None
        # and model_fields_set contains the field
        if self.expire_at is None and "expire_at" in self.model_fields_set:
            _dict['expireAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PersonaAuthReturn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authUrl": obj.get("authUrl"),
            "expireAt": obj.get("expireAt")
        })
        return _obj


