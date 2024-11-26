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


from typing import Optional, Union
from pydantic import ConfigDict, BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret(BaseModel):
    """
    ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret
    """
    id: StrictStr = Field(...)
    version: Union[StrictFloat, StrictInt] = Field(...)
    secret_key: StrictStr = Field(default=..., alias="secretKey")
    secret_value: Optional[StrictStr] = Field(default=None, alias="secretValue")
    secret_comment: Optional[StrictStr] = Field(default=None, alias="secretComment")
    __properties = ["id", "version", "secretKey", "secretValue", "secretComment"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret:
        """Create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret:
        """Create an instance of ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret.parse_obj(obj)

        _obj = ApiV1SecretApprovalRequestsIdGet200ResponseApprovalCommitsInnerSecret.parse_obj({
            "id": obj.get("id"),
            "version": obj.get("version"),
            "secret_key": obj.get("secretKey"),
            "secret_value": obj.get("secretValue"),
            "secret_comment": obj.get("secretComment")
        })
        return _obj


