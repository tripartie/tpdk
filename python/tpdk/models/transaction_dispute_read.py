# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.199
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from tpdk.models.metadata_dispute_read import MetadataDisputeRead
from tpdk.models.offer_dispute_read import OfferDisputeRead
from tpdk.models.parcel_dispute_read import ParcelDisputeRead
from tpdk.models.persona_dispute_read import PersonaDisputeRead
from typing import Optional, Set
from typing_extensions import Self

class TransactionDisputeRead(BaseModel):
    """
    
    """ # noqa: E501
    ulid: StrictStr
    offer: OfferDisputeRead
    buyer: PersonaDisputeRead
    fees: Optional[Union[StrictFloat, StrictInt]] = None
    refundable_fees: Optional[StrictBool] = Field(default=None, alias="refundableFees")
    metadata: Optional[List[MetadataDisputeRead]] = None
    parcels: Optional[List[ParcelDisputeRead]] = None
    __properties: ClassVar[List[str]] = ["ulid", "offer", "buyer", "fees", "refundableFees", "metadata", "parcels"]

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
        """Create an instance of TransactionDisputeRead from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of offer
        if self.offer:
            _dict['offer'] = self.offer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of buyer
        if self.buyer:
            _dict['buyer'] = self.buyer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parcels (list)
        _items = []
        if self.parcels:
            for _item in self.parcels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parcels'] = _items
        # set to None if fees (nullable) is None
        # and model_fields_set contains the field
        if self.fees is None and "fees" in self.model_fields_set:
            _dict['fees'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionDisputeRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ulid": obj.get("ulid"),
            "offer": OfferDisputeRead.from_dict(obj["offer"]) if obj.get("offer") is not None else None,
            "buyer": PersonaDisputeRead.from_dict(obj["buyer"]) if obj.get("buyer") is not None else None,
            "fees": obj.get("fees"),
            "refundableFees": obj.get("refundableFees"),
            "metadata": [MetadataDisputeRead.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None,
            "parcels": [ParcelDisputeRead.from_dict(_item) for _item in obj["parcels"]] if obj.get("parcels") is not None else None
        })
        return _obj


