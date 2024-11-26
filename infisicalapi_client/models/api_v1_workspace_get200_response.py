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
from infisicalapi_client.models.api_v1_workspace_get200_response_workspaces_inner import ApiV1WorkspaceGet200ResponseWorkspacesInner
from typing_extensions import Annotated

class ApiV1WorkspaceGet200Response(BaseModel):
    """
    ApiV1WorkspaceGet200Response
    """
    workspaces: Annotated[List[ApiV1WorkspaceGet200ResponseWorkspacesInner], Field()] = Field(...)
    __properties = ["workspaces"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceGet200Response:
        """Create an instance of ApiV1WorkspaceGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in workspaces (list)
        _items = []
        if self.workspaces:
            for _item in self.workspaces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['workspaces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceGet200Response:
        """Create an instance of ApiV1WorkspaceGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceGet200Response.parse_obj(obj)

        _obj = ApiV1WorkspaceGet200Response.parse_obj({
            "workspaces": [ApiV1WorkspaceGet200ResponseWorkspacesInner.from_dict(_item) for _item in obj.get("workspaces")] if obj.get("workspaces") is not None else None
        })
        return _obj


