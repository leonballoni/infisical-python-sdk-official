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


from typing import List
from pydantic import ConfigDict, BaseModel, Field
from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_post_request_members_inner import ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner
from typing_extensions import Annotated

class ApiV1WorkspaceWorkspaceIdMembershipsPostRequest(BaseModel):
    """
    ApiV1WorkspaceWorkspaceIdMembershipsPostRequest
    """
    members: Annotated[List[ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner], Field(min_length=1)] = Field(...)
    __properties = ["members"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceWorkspaceIdMembershipsPostRequest:
        """Create an instance of ApiV1WorkspaceWorkspaceIdMembershipsPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item in self.members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['members'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceWorkspaceIdMembershipsPostRequest:
        """Create an instance of ApiV1WorkspaceWorkspaceIdMembershipsPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceWorkspaceIdMembershipsPostRequest.parse_obj(obj)

        _obj = ApiV1WorkspaceWorkspaceIdMembershipsPostRequest.parse_obj({
            "members": [ApiV1WorkspaceWorkspaceIdMembershipsPostRequestMembersInner.from_dict(_item) for _item in obj.get("members")] if obj.get("members") is not None else None
        })
        return _obj


