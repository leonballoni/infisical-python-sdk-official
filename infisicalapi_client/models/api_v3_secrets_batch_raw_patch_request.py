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
from pydantic import ConfigDict, BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v3_secrets_batch_raw_patch_request_secrets_inner import ApiV3SecretsBatchRawPatchRequestSecretsInner
from typing_extensions import Annotated

class ApiV3SecretsBatchRawPatchRequest(BaseModel):
    """
    ApiV3SecretsBatchRawPatchRequest
    """
    project_slug: Optional[StrictStr] = Field(default=None, alias="projectSlug", description="The slug of the project to delete the secret in.")
    workspace_id: Optional[StrictStr] = Field(default=None, alias="workspaceId", description="The ID of the project where the secret is located.")
    environment: StrictStr = Field(default=..., description="The slug of the environment where the secret is located.")
    secret_path: Optional[StrictStr] = Field(default='/', alias="secretPath", description="The path of the secret to update")
    secrets: Annotated[List[ApiV3SecretsBatchRawPatchRequestSecretsInner], Field(min_length=1)] = Field(...)
    __properties = ["projectSlug", "workspaceId", "environment", "secretPath", "secrets"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV3SecretsBatchRawPatchRequest:
        """Create an instance of ApiV3SecretsBatchRawPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in secrets (list)
        _items = []
        if self.secrets:
            for _item in self.secrets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['secrets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV3SecretsBatchRawPatchRequest:
        """Create an instance of ApiV3SecretsBatchRawPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV3SecretsBatchRawPatchRequest.parse_obj(obj)

        _obj = ApiV3SecretsBatchRawPatchRequest.parse_obj({
            "project_slug": obj.get("projectSlug"),
            "workspace_id": obj.get("workspaceId"),
            "environment": obj.get("environment"),
            "secret_path": obj.get("secretPath") if obj.get("secretPath") is not None else '/',
            "secrets": [ApiV3SecretsBatchRawPatchRequestSecretsInner.from_dict(_item) for _item in obj.get("secrets")] if obj.get("secrets") is not None else None
        })
        return _obj


