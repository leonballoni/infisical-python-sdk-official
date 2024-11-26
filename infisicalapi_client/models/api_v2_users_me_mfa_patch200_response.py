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



from pydantic import ConfigDict, BaseModel, Field
from infisicalapi_client.models.api_v1_password_email_password_reset_verify_post200_response_user import ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser

class ApiV2UsersMeMfaPatch200Response(BaseModel):
    """
    ApiV2UsersMeMfaPatch200Response
    """
    user: ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser = Field(...)
    __properties = ["user"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV2UsersMeMfaPatch200Response:
        """Create an instance of ApiV2UsersMeMfaPatch200Response from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV2UsersMeMfaPatch200Response:
        """Create an instance of ApiV2UsersMeMfaPatch200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV2UsersMeMfaPatch200Response.parse_obj(obj)

        _obj = ApiV2UsersMeMfaPatch200Response.parse_obj({
            "user": ApiV1PasswordEmailPasswordResetVerifyPost200ResponseUser.from_dict(obj.get("user")) if obj.get("user") is not None else None
        })
        return _obj


