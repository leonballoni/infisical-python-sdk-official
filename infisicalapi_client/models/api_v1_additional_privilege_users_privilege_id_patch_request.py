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
from typing import List, Optional
from pydantic import field_validator, StringConstraints, ConfigDict, BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Annotated

class ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest(BaseModel):
    """
    ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest
    """
    slug: Optional[Annotated[str, StringConstraints(strict=True, max_length=60)]] = Field(default=None, description="The slug of the privilege to create.")
    permissions: Optional[Annotated[List[StrictStr], Field()]] = Field(default=None, description="The permission object for the privilege. Refer https://casl.js.org/v6/en/guide/define-rules#the-shape-of-raw-rule to understand the shape")
    is_temporary: Optional[StrictBool] = Field(default=None, alias="isTemporary", description="Whether the privilege is temporary.")
    temporary_mode: Optional[StrictStr] = Field(default=None, alias="temporaryMode", description="Type of temporary access given. Types: relative")
    temporary_range: Optional[StrictStr] = Field(default=None, alias="temporaryRange", description="TTL for the temporay time. Eg: 1m, 1h, 1d")
    temporary_access_start_time: Optional[datetime] = Field(default=None, alias="temporaryAccessStartTime", description="ISO time for which temporary access should begin.")
    __properties = ["slug", "permissions", "isTemporary", "temporaryMode", "temporaryRange", "temporaryAccessStartTime"]

    @field_validator('temporary_mode')
    @classmethod
    def temporary_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('relative'):
            raise ValueError("must be one of enum values ('relative')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest:
        """Create an instance of ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest:
        """Create an instance of ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest.parse_obj(obj)

        _obj = ApiV1AdditionalPrivilegeUsersPrivilegeIdPatchRequest.parse_obj({
            "slug": obj.get("slug"),
            "permissions": obj.get("permissions"),
            "is_temporary": obj.get("isTemporary"),
            "temporary_mode": obj.get("temporaryMode"),
            "temporary_range": obj.get("temporaryRange"),
            "temporary_access_start_time": obj.get("temporaryAccessStartTime")
        })
        return _obj


