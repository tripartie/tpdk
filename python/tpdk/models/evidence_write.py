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



from pydantic import BaseModel, Field, constr

class EvidenceWrite(BaseModel):
    """
      # noqa: E501
    """
    additional_information: constr(strict=True, max_length=500, min_length=10) = Field(..., alias="additionalInformation", description="Description of what the evidence actually is.")
    __properties = ["additionalInformation"]

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
    def from_json(cls, json_str: str) -> EvidenceWrite:
        """Create an instance of EvidenceWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EvidenceWrite:
        """Create an instance of EvidenceWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EvidenceWrite.parse_obj(obj)

        _obj = EvidenceWrite.parse_obj({
            "additional_information": obj.get("additionalInformation")
        })
        return _obj


