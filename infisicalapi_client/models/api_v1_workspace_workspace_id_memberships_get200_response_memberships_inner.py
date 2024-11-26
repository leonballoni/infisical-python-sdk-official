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
from pydantic import ConfigDict, BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_workspace_workspace_id_memberships_get200_response_memberships_inner_user import ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInnerUser
from infisicalapi_client.models.api_v1_workspace_workspace_id_users_get200_response_users_inner_roles_inner import ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner
from typing_extensions import Annotated

class ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner(BaseModel):
    """
    ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner
    """
    id: StrictStr = Field(...)
    user_id: StrictStr = Field(default=..., alias="userId")
    project_id: StrictStr = Field(default=..., alias="projectId")
    user: ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInnerUser = Field(...)
    roles: Annotated[List[ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner], Field()] = Field(...)
    __properties = ["id", "userId", "projectId", "user", "roles"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner:
        """Create an instance of ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner:
        """Create an instance of ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner.parse_obj(obj)

        _obj = ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInner.parse_obj({
            "id": obj.get("id"),
            "user_id": obj.get("userId"),
            "project_id": obj.get("projectId"),
            "user": ApiV1WorkspaceWorkspaceIdMembershipsGet200ResponseMembershipsInnerUser.from_dict(obj.get("user")) if obj.get("user") is not None else None,
            "roles": [ApiV1WorkspaceWorkspaceIdUsersGet200ResponseUsersInnerRolesInner.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None
        })
        return _obj


