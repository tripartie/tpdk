# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.52
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from tpdk.models.offer_collection_read import OfferCollectionRead
from tpdk.models.persona_collection_read import PersonaCollectionRead

class TransactionCollectionRead(BaseModel):
    """
    
    """
    ulid: StrictStr = Field(...)
    offer: OfferCollectionRead = Field(...)
    buyer: PersonaCollectionRead = Field(...)
    __properties = ["ulid", "offer", "buyer"]

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
    def from_json(cls, json_str: str) -> TransactionCollectionRead:
        """Create an instance of TransactionCollectionRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of offer
        if self.offer:
            _dict['offer'] = self.offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buyer
        if self.buyer:
            _dict['buyer'] = self.buyer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionCollectionRead:
        """Create an instance of TransactionCollectionRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionCollectionRead.parse_obj(obj)

        _obj = TransactionCollectionRead.parse_obj({
            "ulid": obj.get("ulid"),
            "offer": OfferCollectionRead.from_dict(obj.get("offer")) if obj.get("offer") is not None else None,
            "buyer": PersonaCollectionRead.from_dict(obj.get("buyer")) if obj.get("buyer") is not None else None
        })
        return _obj

