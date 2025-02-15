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
from infisicalapi_client.models.api_v1_auth_universal_auth_identities_identity_id_get200_response_identity_universal_auth import ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200ResponseIdentityUniversalAuth

class ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200Response(BaseModel):
    """
    ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200Response
    """
    identity_universal_auth: ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200ResponseIdentityUniversalAuth = Field(default=..., alias="identityUniversalAuth")
    __properties = ["identityUniversalAuth"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200Response:
        """Create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of identity_universal_auth
        if self.identity_universal_auth:
            _dict['identityUniversalAuth'] = self.identity_universal_auth.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200Response:
        """Create an instance of ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200Response.parse_obj(obj)

        _obj = ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200Response.parse_obj({
            "identity_universal_auth": ApiV1AuthUniversalAuthIdentitiesIdentityIdGet200ResponseIdentityUniversalAuth.from_dict(obj.get("identityUniversalAuth")) if obj.get("identityUniversalAuth") is not None else None
        })
        return _obj


