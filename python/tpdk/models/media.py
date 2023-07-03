# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.20
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBytes, StrictInt, StrictStr

class Media(BaseModel):
    """
    
    """
    id: Optional[StrictInt] = None
    extension: StrictStr = Field(...)
    filename: StrictStr = Field(...)
    public_url: Optional[StrictStr] = Field(None, alias="publicUrl")
    file: Optional[Union[StrictBytes, StrictStr]] = None
    b64_encoded_tmp_file: Optional[StrictStr] = Field(None, alias="b64EncodedTmpFile")
    thumbnail: Optional[StrictStr] = Field(None, description="Associated 374x374 pixels small thumbnail")
    original: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    offer: Optional[StrictStr] = None
    thumbnail_url: Optional[StrictStr] = Field(None, alias="thumbnailUrl")
    __properties = ["id", "extension", "filename", "publicUrl", "file", "b64EncodedTmpFile", "thumbnail", "original", "owner", "offer", "thumbnailUrl"]

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
    def from_json(cls, json_str: str) -> Media:
        """Create an instance of Media from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "thumbnail_url",
                          },
                          exclude_none=True)
        # set to None if public_url (nullable) is None
        # and __fields_set__ contains the field
        if self.public_url is None and "public_url" in self.__fields_set__:
            _dict['publicUrl'] = None

        # set to None if file (nullable) is None
        # and __fields_set__ contains the field
        if self.file is None and "file" in self.__fields_set__:
            _dict['file'] = None

        # set to None if b64_encoded_tmp_file (nullable) is None
        # and __fields_set__ contains the field
        if self.b64_encoded_tmp_file is None and "b64_encoded_tmp_file" in self.__fields_set__:
            _dict['b64EncodedTmpFile'] = None

        # set to None if thumbnail (nullable) is None
        # and __fields_set__ contains the field
        if self.thumbnail is None and "thumbnail" in self.__fields_set__:
            _dict['thumbnail'] = None

        # set to None if original (nullable) is None
        # and __fields_set__ contains the field
        if self.original is None and "original" in self.__fields_set__:
            _dict['original'] = None

        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if offer (nullable) is None
        # and __fields_set__ contains the field
        if self.offer is None and "offer" in self.__fields_set__:
            _dict['offer'] = None

        # set to None if thumbnail_url (nullable) is None
        # and __fields_set__ contains the field
        if self.thumbnail_url is None and "thumbnail_url" in self.__fields_set__:
            _dict['thumbnailUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Media:
        """Create an instance of Media from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Media.parse_obj(obj)

        _obj = Media.parse_obj({
            "id": obj.get("id"),
            "extension": obj.get("extension"),
            "filename": obj.get("filename"),
            "public_url": obj.get("publicUrl"),
            "file": obj.get("file"),
            "b64_encoded_tmp_file": obj.get("b64EncodedTmpFile"),
            "thumbnail": obj.get("thumbnail"),
            "original": obj.get("original"),
            "owner": obj.get("owner"),
            "offer": obj.get("offer"),
            "thumbnail_url": obj.get("thumbnailUrl")
        })
        return _obj

