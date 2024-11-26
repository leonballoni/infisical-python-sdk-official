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
from pydantic import field_validator, ConfigDict, BaseModel, Field, StrictStr
from typing_extensions import Annotated

class ApiV3SecretsTagsSecretNameDeleteRequest(BaseModel):
    """
    ApiV3SecretsTagsSecretNameDeleteRequest
    """
    project_slug: StrictStr = Field(default=..., alias="projectSlug", description="The slug of the project where the secret is located")
    environment: StrictStr = Field(default=..., description="The slug of the environment where the secret is located")
    secret_path: Optional[StrictStr] = Field(default='/', alias="secretPath", description="The path of the secret to detach tags from.")
    type: Optional[StrictStr] = Field(default='shared', description="The type of the secret to attach tags to. (shared/personal)")
    tag_slugs: Annotated[List[StrictStr], Field(min_length=1)] = Field(default=..., alias="tagSlugs", description="An array of existing tag slugs to detach from the secret.")
    __properties = ["projectSlug", "environment", "secretPath", "type", "tagSlugs"]

    @field_validator('type')
    @classmethod
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('shared', 'personal'):
            raise ValueError("must be one of enum values ('shared', 'personal')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV3SecretsTagsSecretNameDeleteRequest:
        """Create an instance of ApiV3SecretsTagsSecretNameDeleteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV3SecretsTagsSecretNameDeleteRequest:
        """Create an instance of ApiV3SecretsTagsSecretNameDeleteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV3SecretsTagsSecretNameDeleteRequest.parse_obj(obj)

        _obj = ApiV3SecretsTagsSecretNameDeleteRequest.parse_obj({
            "project_slug": obj.get("projectSlug"),
            "environment": obj.get("environment"),
            "secret_path": obj.get("secretPath") if obj.get("secretPath") is not None else '/',
            "type": obj.get("type") if obj.get("type") is not None else 'shared',
            "tag_slugs": obj.get("tagSlugs")
        })
        return _obj


