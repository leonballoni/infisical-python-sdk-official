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
from infisicalapi_client.models.api_v1_scim_groups_group_id_patch_request_operations_inner import ApiV1ScimGroupsGroupIdPatchRequestOperationsInner
from typing_extensions import Annotated

class ApiV1ScimGroupsGroupIdPatchRequest(BaseModel):
    """
    ApiV1ScimGroupsGroupIdPatchRequest
    """
    schemas: Annotated[List[StrictStr], Field()] = Field(...)
    operations: Annotated[List[ApiV1ScimGroupsGroupIdPatchRequestOperationsInner], Field()] = Field(default=..., alias="Operations")
    __properties = ["schemas", "Operations"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1ScimGroupsGroupIdPatchRequest:
        """Create an instance of ApiV1ScimGroupsGroupIdPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in operations (list)
        _items = []
        if self.operations:
            for _item in self.operations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Operations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1ScimGroupsGroupIdPatchRequest:
        """Create an instance of ApiV1ScimGroupsGroupIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1ScimGroupsGroupIdPatchRequest.parse_obj(obj)

        _obj = ApiV1ScimGroupsGroupIdPatchRequest.parse_obj({
            "schemas": obj.get("schemas"),
            "operations": [ApiV1ScimGroupsGroupIdPatchRequestOperationsInner.from_dict(_item) for _item in obj.get("Operations")] if obj.get("Operations") is not None else None
        })
        return _obj


