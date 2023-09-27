# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.74
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from tpdk.models.metadata_independent_write import MetadataIndependentWrite
from tpdk.models.transaction_independent_write import TransactionIndependentWrite

class DisputeIndependentWrite(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.  # noqa: E501
    """
    transaction: TransactionIndependentWrite = Field(...)
    redirect_url: Optional[StrictStr] = Field(None, alias="redirectUrl", description="Fill-in that field IF you intend to redirect your customer instead of using a WebView.")
    metadata: Optional[conlist(MetadataIndependentWrite, max_items=16)] = None
    __properties = ["transaction", "redirectUrl", "metadata"]

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
    def from_json(cls, json_str: str) -> DisputeIndependentWrite:
        """Create an instance of DisputeIndependentWrite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # set to None if redirect_url (nullable) is None
        # and __fields_set__ contains the field
        if self.redirect_url is None and "redirect_url" in self.__fields_set__:
            _dict['redirectUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DisputeIndependentWrite:
        """Create an instance of DisputeIndependentWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DisputeIndependentWrite.parse_obj(obj)

        _obj = DisputeIndependentWrite.parse_obj({
            "transaction": TransactionIndependentWrite.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None,
            "redirect_url": obj.get("redirectUrl"),
            "metadata": [MetadataIndependentWrite.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None
        })
        return _obj


