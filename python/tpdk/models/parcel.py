# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.153
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Parcel(BaseModel):
    """
    
    """ # noqa: E501
    id: Optional[StrictInt] = None
    carrier: StrictStr
    identifier: Annotated[str, Field(min_length=4, strict=True, max_length=128)]
    price: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = None
    refundable: Optional[StrictBool] = None
    currency: Optional[StrictStr] = 'EUR'
    status: Optional[StrictStr] = None
    dispute: Optional[StrictStr] = None
    transaction: Optional[StrictStr] = None
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "carrier", "identifier", "price", "refundable", "currency", "status", "dispute", "transaction", "createdAt", "updatedAt"]

    @field_validator('carrier')
    def carrier_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SwissPost', 'MondialRelay', 'Colissimo', 'Dhl', 'Chronopost', 'ColisPrive', 'Dpd', 'Ups', 'FedEx', 'RelaisColis'):
            raise ValueError("must be one of enum values ('SwissPost', 'MondialRelay', 'Colissimo', 'Dhl', 'Chronopost', 'ColisPrive', 'Dpd', 'Ups', 'FedEx', 'RelaisColis')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CREATED', 'SHIPPED', 'IN_TRANSIT', 'DELIVERED', 'ERROR', 'ACCEPTED', 'REFUSED', 'null'):
            raise ValueError("must be one of enum values ('CREATED', 'SHIPPED', 'IN_TRANSIT', 'DELIVERED', 'ERROR', 'ACCEPTED', 'REFUSED', 'null')")
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
        """Create an instance of Parcel from a JSON string"""
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
                "updated_at",
            },
            exclude_none=True,
        )
        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if dispute (nullable) is None
        # and model_fields_set contains the field
        if self.dispute is None and "dispute" in self.model_fields_set:
            _dict['dispute'] = None

        # set to None if transaction (nullable) is None
        # and model_fields_set contains the field
        if self.transaction is None and "transaction" in self.model_fields_set:
            _dict['transaction'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Parcel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "carrier": obj.get("carrier"),
            "identifier": obj.get("identifier"),
            "price": obj.get("price"),
            "refundable": obj.get("refundable"),
            "currency": obj.get("currency") if obj.get("currency") is not None else 'EUR',
            "status": obj.get("status"),
            "dispute": obj.get("dispute"),
            "transaction": obj.get("transaction"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


