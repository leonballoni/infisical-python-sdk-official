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
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Annotated

class ApiV1DynamicSecretsNameDeleteRequest(BaseModel):
    """
    ApiV1DynamicSecretsNameDeleteRequest
    """
    project_slug: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., alias="projectSlug", description="The slug of the project to delete dynamic secret in.")
    path: Optional[StrictStr] = Field(default='/', description="The path to delete the dynamic secret in.")
    environment_slug: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., alias="environmentSlug", description="The slug of the environment to delete the dynamic secret in.")
    is_forced: Optional[StrictBool] = Field(default=False, alias="isForced", description="A boolean flag to delete the the dynamic secret from infisical without trying to remove it from external provider. Used when the dynamic secret got modified externally.")
    __properties = ["projectSlug", "path", "environmentSlug", "isForced"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsNameDeleteRequest:
        """Create an instance of ApiV1DynamicSecretsNameDeleteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsNameDeleteRequest:
        """Create an instance of ApiV1DynamicSecretsNameDeleteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsNameDeleteRequest.parse_obj(obj)

        _obj = ApiV1DynamicSecretsNameDeleteRequest.parse_obj({
            "project_slug": obj.get("projectSlug"),
            "path": obj.get("path") if obj.get("path") is not None else '/',
            "environment_slug": obj.get("environmentSlug"),
            "is_forced": obj.get("isForced") if obj.get("isForced") is not None else False
        })
        return _obj


