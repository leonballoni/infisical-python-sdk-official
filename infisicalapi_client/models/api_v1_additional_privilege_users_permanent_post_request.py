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


from typing import List, Optional
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictStr
from typing_extensions import Annotated

class ApiV1AdditionalPrivilegeUsersPermanentPostRequest(BaseModel):
    """
    ApiV1AdditionalPrivilegeUsersPermanentPostRequest
    """
    project_membership_id: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., alias="projectMembershipId", description="Project membership id of user")
    slug: Optional[Annotated[str, StringConstraints(strict=True, max_length=60, min_length=1)]] = Field(default=None, description="The slug of the privilege to create.")
    permissions: Annotated[List[StrictStr], Field()] = Field(default=..., description="The permission object for the privilege. Refer https://casl.js.org/v6/en/guide/define-rules#the-shape-of-raw-rule to understand the shape")
    __properties = ["projectMembershipId", "slug", "permissions"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1AdditionalPrivilegeUsersPermanentPostRequest:
        """Create an instance of ApiV1AdditionalPrivilegeUsersPermanentPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AdditionalPrivilegeUsersPermanentPostRequest:
        """Create an instance of ApiV1AdditionalPrivilegeUsersPermanentPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AdditionalPrivilegeUsersPermanentPostRequest.parse_obj(obj)

        _obj = ApiV1AdditionalPrivilegeUsersPermanentPostRequest.parse_obj({
            "project_membership_id": obj.get("projectMembershipId"),
            "slug": obj.get("slug"),
            "permissions": obj.get("permissions")
        })
        return _obj


