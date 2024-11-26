# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class ApiV1FoldersGet200ResponseFoldersInner(BaseModel):
    """
    ApiV1FoldersGet200ResponseFoldersInner
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    version: Optional[Union[StrictFloat, StrictInt]] = 1
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    env_id: StrictStr = Field(default=..., alias="envId")
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    is_reserved: Optional[StrictBool] = Field(default=False, alias="isReserved")
    __properties = ["id", "name", "version", "createdAt", "updatedAt", "envId", "parentId", "isReserved"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1FoldersGet200ResponseFoldersInner:
        """Create an instance of ApiV1FoldersGet200ResponseFoldersInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if version (nullable) is None
        # and __fields_set__ contains the field
        if self.version is None and "version" in self.__fields_set__:
            _dict['version'] = None

        # set to None if parent_id (nullable) is None
        # and __fields_set__ contains the field
        if self.parent_id is None and "parent_id" in self.__fields_set__:
            _dict['parentId'] = None

        # set to None if is_reserved (nullable) is None
        # and __fields_set__ contains the field
        if self.is_reserved is None and "is_reserved" in self.__fields_set__:
            _dict['isReserved'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1FoldersGet200ResponseFoldersInner:
        """Create an instance of ApiV1FoldersGet200ResponseFoldersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1FoldersGet200ResponseFoldersInner.parse_obj(obj)

        _obj = ApiV1FoldersGet200ResponseFoldersInner.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "version": obj.get("version") if obj.get("version") is not None else 1,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "env_id": obj.get("envId"),
            "parent_id": obj.get("parentId"),
            "is_reserved": obj.get("isReserved") if obj.get("isReserved") is not None else False
        })
        return _obj


