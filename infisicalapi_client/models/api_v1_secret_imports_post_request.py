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
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr
from infisicalapi_client.models.api_v1_secret_imports_post_request_import import ApiV1SecretImportsPostRequestImport

class ApiV1SecretImportsPostRequest(BaseModel):
    """
    ApiV1SecretImportsPostRequest
    """
    workspace_id: StrictStr = Field(default=..., alias="workspaceId", description="The ID of the project you are working in.")
    environment: StrictStr = Field(default=..., description="The slug of the environment to import into.")
    path: Optional[StrictStr] = Field(default='/', description="The path to import into.")
    var_import: ApiV1SecretImportsPostRequestImport = Field(default=..., alias="import")
    is_replication: Optional[StrictBool] = Field(default=False, alias="isReplication", description="When true, secrets from the source will be automatically sent to the destination. If approval policies exist at the destination, the secrets will be sent as approval requests instead of being applied immediately.")
    __properties = ["workspaceId", "environment", "path", "import", "isReplication"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretImportsPostRequest:
        """Create an instance of ApiV1SecretImportsPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_import
        if self.var_import:
            _dict['import'] = self.var_import.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretImportsPostRequest:
        """Create an instance of ApiV1SecretImportsPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretImportsPostRequest.parse_obj(obj)

        _obj = ApiV1SecretImportsPostRequest.parse_obj({
            "workspace_id": obj.get("workspaceId"),
            "environment": obj.get("environment"),
            "path": obj.get("path") if obj.get("path") is not None else '/',
            "var_import": ApiV1SecretImportsPostRequestImport.from_dict(obj.get("import")) if obj.get("import") is not None else None,
            "is_replication": obj.get("isReplication") if obj.get("isReplication") is not None else False
        })
        return _obj


