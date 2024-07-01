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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tpdk.models.dispute_address_independent_write import DisputeAddressIndependentWrite
from tpdk.models.dispute_metadata_independent_write import DisputeMetadataIndependentWrite
from typing import Optional, Set
from typing_extensions import Self

class DisputePersonaIndependentWrite(BaseModel):
    """
    
    """ # noqa: E501
    first_name: Annotated[str, Field(min_length=1, strict=True, max_length=64)] = Field(alias="firstName")
    last_name: Annotated[str, Field(min_length=1, strict=True, max_length=64)] = Field(alias="lastName")
    gender: StrictStr
    date_of_birth: Optional[date] = Field(default=None, alias="dateOfBirth")
    language: Optional[StrictStr] = Field(default=None, description="That data is used for rendering the frontend application with given language. If not set, will be inferred. Custom codes can be issued for specific requirements.")
    email: Optional[StrictStr] = None
    mobile_phone_number: Optional[StrictStr] = Field(default=None, alias="mobilePhoneNumber")
    address: Optional[DisputeAddressIndependentWrite] = None
    external_purchase_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.", alias="externalPurchaseCount")
    external_sell_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Knowing the statistics on your user is used to better know its profile when you do not use the Safe-Checkout feature. Although it is not required, we recommend that you keep us informed.", alias="externalSellCount")
    metadata: Optional[Annotated[List[DisputeMetadataIndependentWrite], Field(max_length=16)]] = Field(default=None, description="You can assign different meta to your Persona object for different purposes. eg. Ease searching.")
    __properties: ClassVar[List[str]] = ["firstName", "lastName", "gender", "dateOfBirth", "language", "email", "mobilePhoneNumber", "address", "externalPurchaseCount", "externalSellCount", "metadata"]

    @field_validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY']):
            raise ValueError("must be one of enum values ('MALE', 'FEMALE', 'OTHER', 'RATHER_NOT_SAY')")
        return value

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
        """Create an instance of DisputePersonaIndependentWrite from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in metadata (list)
        _items = []
        if self.metadata:
            for _item in self.metadata:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata'] = _items
        # set to None if date_of_birth (nullable) is None
        # and model_fields_set contains the field
        if self.date_of_birth is None and "date_of_birth" in self.model_fields_set:
            _dict['dateOfBirth'] = None

        # set to None if language (nullable) is None
        # and model_fields_set contains the field
        if self.language is None and "language" in self.model_fields_set:
            _dict['language'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if mobile_phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_phone_number is None and "mobile_phone_number" in self.model_fields_set:
            _dict['mobilePhoneNumber'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DisputePersonaIndependentWrite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "gender": obj.get("gender") if obj.get("gender") is not None else 'RATHER_NOT_SAY',
            "dateOfBirth": obj.get("dateOfBirth"),
            "language": obj.get("language"),
            "email": obj.get("email"),
            "mobilePhoneNumber": obj.get("mobilePhoneNumber"),
            "address": DisputeAddressIndependentWrite.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "externalPurchaseCount": obj.get("externalPurchaseCount"),
            "externalSellCount": obj.get("externalSellCount"),
            "metadata": [DisputeMetadataIndependentWrite.from_dict(_item) for _item in obj["metadata"]] if obj.get("metadata") is not None else None
        })
        return _obj

