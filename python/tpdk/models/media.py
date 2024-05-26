# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.

    The version of the OpenAPI document: 2.0.202
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBytes, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Media(BaseModel):
    """
    
    """ # noqa: E501
    id: Optional[StrictInt] = None
    extension: StrictStr
    filename: StrictStr
    fingerprint: StrictStr
    public_url: StrictStr = Field(alias="publicUrl")
    file: Optional[Union[StrictBytes, StrictStr]] = None
    b64_encoded_tmp_file: Optional[StrictStr] = Field(default=None, alias="b64EncodedTmpFile")
    thumbnail: Optional[StrictStr] = Field(default=None, description="Associated 374x374 pixels small thumbnail")
    original: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    offers: Optional[List[StrictStr]] = None
    thumbnail_url: Optional[StrictStr] = Field(default=None, alias="thumbnailUrl")
    __properties: ClassVar[List[str]] = ["id", "extension", "filename", "fingerprint", "publicUrl", "file", "b64EncodedTmpFile", "thumbnail", "original", "owner", "offers", "thumbnailUrl"]

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
        """Create an instance of Media from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "thumbnail_url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if file (nullable) is None
        # and model_fields_set contains the field
        if self.file is None and "file" in self.model_fields_set:
            _dict['file'] = None

        # set to None if b64_encoded_tmp_file (nullable) is None
        # and model_fields_set contains the field
        if self.b64_encoded_tmp_file is None and "b64_encoded_tmp_file" in self.model_fields_set:
            _dict['b64EncodedTmpFile'] = None

        # set to None if thumbnail (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail is None and "thumbnail" in self.model_fields_set:
            _dict['thumbnail'] = None

        # set to None if original (nullable) is None
        # and model_fields_set contains the field
        if self.original is None and "original" in self.model_fields_set:
            _dict['original'] = None

        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and "owner" in self.model_fields_set:
            _dict['owner'] = None

        # set to None if thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail_url is None and "thumbnail_url" in self.model_fields_set:
            _dict['thumbnailUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Media from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "extension": obj.get("extension"),
            "filename": obj.get("filename"),
            "fingerprint": obj.get("fingerprint"),
            "publicUrl": obj.get("publicUrl"),
            "file": obj.get("file"),
            "b64EncodedTmpFile": obj.get("b64EncodedTmpFile"),
            "thumbnail": obj.get("thumbnail"),
            "original": obj.get("original"),
            "owner": obj.get("owner"),
            "offers": obj.get("offers"),
            "thumbnailUrl": obj.get("thumbnailUrl")
        })
        return _obj


