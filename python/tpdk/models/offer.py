# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.35
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from tpdk.models.metadata import Metadata
from tpdk.models.view import View

class Offer(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    ulid: StrictStr = Field(...)
    public_url: Optional[StrictStr] = Field(None, alias="publicUrl", description="If specified, there would be not need for you to fill-in details. Must be accessible over WAN.")
    enforce_persona_auth: StrictBool = Field(..., alias="enforcePersonaAuth", description="Mean that the generated url cannot be accessed without a generated token for a Persona. Disallow external registration.")
    override_rate_commission_safe_checkout: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="overrideRateCommissionSafeCheckout", description="Override YOUR platform fees for that particular Offer.")
    redirect_url: Optional[StrictStr] = Field(None, alias="redirectUrl", description="Fill-in that field IF you intend to redirect your customer instead of using a WebView.")
    url: Optional[StrictStr] = Field(...)
    organization: Optional[StrictStr] = None
    seller: StrictStr = Field(..., description="If the seller is actually YOUR organization, set it to NULL.")
    nature: StrictStr = Field(..., description="This WILL affect the assigned workflow. Choosing service will disable delivery for example. Refer to our technical hub for more information.")
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="unitPrice")
    currency_code: Optional[StrictStr] = Field('EUR', alias="currencyCode")
    item_count: Optional[StrictInt] = Field(1, alias="itemCount")
    condition: Optional[StrictStr] = 'USED'
    weight_in_gram: Optional[StrictInt] = Field(None, alias="weightInGram")
    shipping_allowed: StrictBool = Field(..., alias="shippingAllowed", description="That toggle allows the seller to propose shipping for its item. If set in conjunction of shippingCarrier, the label will be automatically generated. Also, it will restrict the carrier to the limited subset defined.")
    hand_delivery_allowed: StrictBool = Field(..., alias="handDeliveryAllowed", description="Enable both parties to finalize the transaction in person rather than using delivery. A QR Code must be scanned by the seller once the buyer claims the product.")
    shipping_carriers: Optional[conlist(StrictStr)] = Field(None, alias="shippingCarriers", description="If you wish to enable automated shipping label generation through a specific provider, specify it there.")
    ean_code: Optional[StrictStr] = Field(None, alias="eanCode")
    can_be_sold_separately: StrictBool = Field(..., alias="canBeSoldSeparately", description="Set this flag to false to forbid a potential buyer to acquire this item separately.          This is only useful in a BulkOffer context.")
    metadata: Optional[conlist(Metadata)] = None
    medias: conlist(StrictStr) = Field(...)
    views: conlist(View) = Field(...)
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    iri: Optional[StrictStr] = None
    __properties = ["id", "ulid", "publicUrl", "enforcePersonaAuth", "overrideRateCommissionSafeCheckout", "redirectUrl", "url", "organization", "seller", "nature", "title", "description", "unitPrice", "currencyCode", "itemCount", "condition", "weightInGram", "shippingAllowed", "handDeliveryAllowed", "shippingCarriers", "eanCode", "canBeSoldSeparately", "metadata", "medias", "views", "createdAt", "updatedAt", "iri"]

    @validator('nature')
    def nature_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('service', 'physical_item', 'dematerialized_item', 'rent_item'):
            raise ValueError("must be one of enum values ('service', 'physical_item', 'dematerialized_item', 'rent_item')")
        return value

    @validator('condition')
    def condition_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NEW', 'USED', 'DAMAGED', 'DETERIORATED', 'UNRECOVERABLE'):
            raise ValueError("must be one of enum values ('NEW', 'USED', 'DAMAGED', 'DETERIORATED', 'UNRECOVERABLE')")
        return value

    @validator('shipping_carriers')
    def shipping_carriers_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('SwissPost', 'Colissimo', 'MondialRelay'):
                raise ValueError("each list item must be one of ('SwissPost', 'Colissimo', 'MondialRelay')")
        return value

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
    def from_json(cls, json_str: str) -> Offer:
        """Create an instance of Offer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "url",
                            "created_at",
                            "updated_at",
                            "iri",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item in self.views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['views'] = _items
        # set to None if public_url (nullable) is None
        # and __fields_set__ contains the field
        if self.public_url is None and "public_url" in self.__fields_set__:
            _dict['publicUrl'] = None

        # set to None if override_rate_commission_safe_checkout (nullable) is None
        # and __fields_set__ contains the field
        if self.override_rate_commission_safe_checkout is None and "override_rate_commission_safe_checkout" in self.__fields_set__:
            _dict['overrideRateCommissionSafeCheckout'] = None

        # set to None if redirect_url (nullable) is None
        # and __fields_set__ contains the field
        if self.redirect_url is None and "redirect_url" in self.__fields_set__:
            _dict['redirectUrl'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if organization (nullable) is None
        # and __fields_set__ contains the field
        if self.organization is None and "organization" in self.__fields_set__:
            _dict['organization'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if unit_price (nullable) is None
        # and __fields_set__ contains the field
        if self.unit_price is None and "unit_price" in self.__fields_set__:
            _dict['unitPrice'] = None

        # set to None if currency_code (nullable) is None
        # and __fields_set__ contains the field
        if self.currency_code is None and "currency_code" in self.__fields_set__:
            _dict['currencyCode'] = None

        # set to None if weight_in_gram (nullable) is None
        # and __fields_set__ contains the field
        if self.weight_in_gram is None and "weight_in_gram" in self.__fields_set__:
            _dict['weightInGram'] = None

        # set to None if shipping_carriers (nullable) is None
        # and __fields_set__ contains the field
        if self.shipping_carriers is None and "shipping_carriers" in self.__fields_set__:
            _dict['shippingCarriers'] = None

        # set to None if ean_code (nullable) is None
        # and __fields_set__ contains the field
        if self.ean_code is None and "ean_code" in self.__fields_set__:
            _dict['eanCode'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Offer:
        """Create an instance of Offer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Offer.parse_obj(obj)

        _obj = Offer.parse_obj({
            "id": obj.get("id"),
            "ulid": obj.get("ulid"),
            "public_url": obj.get("publicUrl"),
            "enforce_persona_auth": obj.get("enforcePersonaAuth") if obj.get("enforcePersonaAuth") is not None else True,
            "override_rate_commission_safe_checkout": obj.get("overrideRateCommissionSafeCheckout"),
            "redirect_url": obj.get("redirectUrl"),
            "url": obj.get("url"),
            "organization": obj.get("organization"),
            "seller": obj.get("seller"),
            "nature": obj.get("nature") if obj.get("nature") is not None else 'physical_item',
            "title": obj.get("title"),
            "description": obj.get("description"),
            "unit_price": obj.get("unitPrice"),
            "currency_code": obj.get("currencyCode") if obj.get("currencyCode") is not None else 'EUR',
            "item_count": obj.get("itemCount") if obj.get("itemCount") is not None else 1,
            "condition": obj.get("condition") if obj.get("condition") is not None else 'USED',
            "weight_in_gram": obj.get("weightInGram"),
            "shipping_allowed": obj.get("shippingAllowed"),
            "hand_delivery_allowed": obj.get("handDeliveryAllowed") if obj.get("handDeliveryAllowed") is not None else True,
            "shipping_carriers": obj.get("shippingCarriers"),
            "ean_code": obj.get("eanCode"),
            "can_be_sold_separately": obj.get("canBeSoldSeparately") if obj.get("canBeSoldSeparately") is not None else True,
            "metadata": [Metadata.from_dict(_item) for _item in obj.get("metadata")] if obj.get("metadata") is not None else None,
            "medias": obj.get("medias"),
            "views": [View.from_dict(_item) for _item in obj.get("views")] if obj.get("views") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "iri": obj.get("iri")
        })
        return _obj

