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
from typing import List
from pydantic import ConfigDict, BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_workspace_workspace_id_users_get200_response_users_inner_roles_inner import ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner
from infisicalapi_client.models.api_v2_workspace_project_slug_groups_get200_response_group_memberships_inner_group import ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInnerGroup
from typing_extensions import Annotated

class ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner(BaseModel):
    """
    ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner
    """
    id: StrictStr = Field(...)
    group_id: StrictStr = Field(default=..., alias="groupId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    roles: Annotated[List[ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner], Field()] = Field(...)
    group: ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInnerGroup = Field(...)
    __properties = ["id", "groupId", "createdAt", "updatedAt", "roles", "group"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner:
        """Create an instance of ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner:
        """Create an instance of ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner.parse_obj(obj)

        _obj = ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInner.parse_obj({
            "id": obj.get("id"),
            "group_id": obj.get("groupId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "roles": [ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None,
            "group": ApiV2WorkspaceProjectSlugGroupsGet200ResponseGroupMembershipsInnerGroup.from_dict(obj.get("group")) if obj.get("group") is not None else None
        })
        return _obj


