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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PersonaExternalAuth(BaseModel):
    """
    
    """ # noqa: E501
    captcha: Optional[StrictStr] = None
    target_url: Optional[StrictStr] = Field(default=None, description="The URL you wish that Persona to go to without additional MFA. The URL MUST concern that Persona.", alias="targetUrl")
    plain_password: Optional[StrictStr] = Field(default=None, alias="plainPassword")
    email: Optional[StrictStr] = None
    mobile_phone_number: Optional[StrictStr] = Field(default=None, alias="mobilePhoneNumber")
    __properties: ClassVar[List[str]] = ["captcha", "targetUrl", "plainPassword", "email", "mobilePhoneNumber"]

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
        """Create an instance of PersonaExternalAuth from a JSON string"""
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
        # set to None if captcha (nullable) is None
        # and model_fields_set contains the field
        if self.captcha is None and "captcha" in self.model_fields_set:
            _dict['captcha'] = None

        # set to None if target_url (nullable) is None
        # and model_fields_set contains the field
        if self.target_url is None and "target_url" in self.model_fields_set:
            _dict['targetUrl'] = None

        # set to None if plain_password (nullable) is None
        # and model_fields_set contains the field
        if self.plain_password is None and "plain_password" in self.model_fields_set:
            _dict['plainPassword'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if mobile_phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_phone_number is None and "mobile_phone_number" in self.model_fields_set:
            _dict['mobilePhoneNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PersonaExternalAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "captcha": obj.get("captcha"),
            "targetUrl": obj.get("targetUrl"),
            "plainPassword": obj.get("plainPassword"),
            "email": obj.get("email"),
            "mobilePhoneNumber": obj.get("mobilePhoneNumber")
        })
        return _obj


