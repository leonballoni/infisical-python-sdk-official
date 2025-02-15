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


from typing import Optional
from pydantic import StringConstraints, ConfigDict, BaseModel, Field
from typing_extensions import Annotated

class ApiV1GroupsCurrentSlugPatchRequest(BaseModel):
    """
    ApiV1GroupsCurrentSlugPatchRequest
    """
    name: Optional[Annotated[str, StringConstraints(strict=True, min_length=1)]] = Field(default=None, description="The new name of the group to update to.")
    slug: Optional[Annotated[str, StringConstraints(strict=True, max_length=36, min_length=5)]] = Field(default=None, description="The new slug of the group to update to.")
    role: Optional[Annotated[str, StringConstraints(strict=True, min_length=1)]] = Field(default=None, description="The new role of the group to update to.")
    __properties = ["name", "slug", "role"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1GroupsCurrentSlugPatchRequest:
        """Create an instance of ApiV1GroupsCurrentSlugPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1GroupsCurrentSlugPatchRequest:
        """Create an instance of ApiV1GroupsCurrentSlugPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1GroupsCurrentSlugPatchRequest.parse_obj(obj)

        _obj = ApiV1GroupsCurrentSlugPatchRequest.parse_obj({
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "role": obj.get("role")
        })
        return _obj


