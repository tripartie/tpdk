# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.178
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from tpdk.models.media_read import MediaRead
from tpdk.models.organization_read import OrganizationRead
from tpdk.models.persona_read import PersonaRead
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OfferRead(BaseModel):
    """
    
    """ # noqa: E501
    ulid: StrictStr
    public_url: Optional[StrictStr] = Field(default=None, description="If specified, there would be not need for you to fill-in details. Must be accessible over WAN.", alias="publicUrl")
    organization: Optional[OrganizationRead] = None
    seller: PersonaRead = Field(description="If the seller is actually YOUR organization, set it to NULL.")
    nature: StrictStr = Field(description="This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information.")
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unitPrice")
    currency_code: Optional[StrictStr] = Field(default='EUR', alias="currencyCode")
    item_count: Optional[StrictInt] = Field(default=1, alias="itemCount")
    condition: Optional[StrictStr] = 'USED'
    medias: List[MediaRead]
    __properties: ClassVar[List[str]] = ["ulid", "publicUrl", "organization", "seller", "nature", "title", "description", "unitPrice", "currencyCode", "itemCount", "condition", "medias"]

    @field_validator('nature')
    def nature_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('service', 'physical_item', 'dematerialized_item', 'rent_item'):
            raise ValueError("must be one of enum values ('service', 'physical_item', 'dematerialized_item', 'rent_item')")
        return value

    @field_validator('condition')
    def condition_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NEW', 'USED', 'DAMAGED', 'DETERIORATED', 'UNRECOVERABLE'):
            raise ValueError("must be one of enum values ('NEW', 'USED', 'DAMAGED', 'DETERIORATED', 'UNRECOVERABLE')")
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
        """Create an instance of OfferRead from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of seller
        if self.seller:
            _dict['seller'] = self.seller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in medias (list)
        _items = []
        if self.medias:
            for _item in self.medias:
                if _item:
                    _items.append(_item.to_dict())
            _dict['medias'] = _items
        # set to None if public_url (nullable) is None
        # and model_fields_set contains the field
        if self.public_url is None and "public_url" in self.model_fields_set:
            _dict['publicUrl'] = None

        # set to None if organization (nullable) is None
        # and model_fields_set contains the field
        if self.organization is None and "organization" in self.model_fields_set:
            _dict['organization'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if unit_price (nullable) is None
        # and model_fields_set contains the field
        if self.unit_price is None and "unit_price" in self.model_fields_set:
            _dict['unitPrice'] = None

        # set to None if currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.currency_code is None and "currency_code" in self.model_fields_set:
            _dict['currencyCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OfferRead from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ulid": obj.get("ulid"),
            "publicUrl": obj.get("publicUrl"),
            "organization": OrganizationRead.from_dict(obj.get("organization")) if obj.get("organization") is not None else None,
            "seller": PersonaRead.from_dict(obj.get("seller")) if obj.get("seller") is not None else None,
            "nature": obj.get("nature") if obj.get("nature") is not None else 'physical_item',
            "title": obj.get("title"),
            "description": obj.get("description"),
            "unitPrice": obj.get("unitPrice"),
            "currencyCode": obj.get("currencyCode") if obj.get("currencyCode") is not None else 'EUR',
            "itemCount": obj.get("itemCount") if obj.get("itemCount") is not None else 1,
            "condition": obj.get("condition") if obj.get("condition") is not None else 'USED',
            "medias": [MediaRead.from_dict(_item) for _item in obj.get("medias")] if obj.get("medias") is not None else None
        })
        return _obj


