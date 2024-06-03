# coding: utf-8

"""
    Resolution Center

    Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution.

    The version of the OpenAPI document: 2.0.208
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DisputePostCreationRead(BaseModel):
    """
    Access directly our resolution center without having used the safe-checkout feature.
    """ # noqa: E501
    ulid: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    buyer_id: Optional[StrictInt] = Field(default=None, alias="buyerId")
    seller_id: Optional[StrictInt] = Field(default=None, alias="sellerId")
    offer_ulid: Optional[StrictStr] = Field(default=None, alias="offerUlid")
    __properties: ClassVar[List[str]] = ["ulid", "url", "buyerId", "sellerId", "offerUlid"]

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
        """Create an instance of DisputePostCreationRead from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "buyer_id",
            "seller_id",
            "offer_ulid",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if buyer_id (nullable) is None
        # and model_fields_set contains the field
        if self.buyer_id is None and "buyer_id" in self.model_fields_set:
            _dict['buyerId'] = None

        # set to None if seller_id (nullable) is None
        # and model_fields_set contains the field
        if self.seller_id is None and "seller_id" in self.model_fields_set:
            _dict['sellerId'] = None

        # set to None if offer_ulid (nullable) is None
        # and model_fields_set contains the field
        if self.offer_ulid is None and "offer_ulid" in self.model_fields_set:
            _dict['offerUlid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DisputePostCreationRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ulid": obj.get("ulid"),
            "url": obj.get("url"),
            "buyerId": obj.get("buyerId"),
            "sellerId": obj.get("sellerId"),
            "offerUlid": obj.get("offerUlid")
        })
        return _obj


