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

from datetime import datetime
from typing import Any, Optional, Union
from pydantic import ConfigDict, BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ApiV1AuthAwsAuthIdentitiesIdentityIdGet200ResponseIdentityAwsAuth(BaseModel):
    """
    ApiV1AuthAwsAuthIdentitiesIdentityIdGet200ResponseIdentityAwsAuth
    """
    id: StrictStr = Field(...)
    access_token_ttl: Optional[Union[StrictFloat, StrictInt]] = Field(default=7200, alias="accessTokenTTL")
    access_token_max_ttl: Optional[Union[StrictFloat, StrictInt]] = Field(default=7200, alias="accessTokenMaxTTL")
    access_token_num_uses_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=0, alias="accessTokenNumUsesLimit")
    access_token_trusted_ips: Optional[Any] = Field(default=None, alias="accessTokenTrustedIps")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    identity_id: StrictStr = Field(default=..., alias="identityId")
    type: StrictStr = Field(...)
    sts_endpoint: StrictStr = Field(default=..., alias="stsEndpoint")
    allowed_principal_arns: StrictStr = Field(default=..., alias="allowedPrincipalArns")
    allowed_account_ids: StrictStr = Field(default=..., alias="allowedAccountIds")
    __properties = ["id", "accessTokenTTL", "accessTokenMaxTTL", "accessTokenNumUsesLimit", "accessTokenTrustedIps", "createdAt", "updatedAt", "identityId", "type", "stsEndpoint", "allowedPrincipalArns", "allowedAccountIds"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1AuthAwsAuthIdentitiesIdentityIdGet200ResponseIdentityAwsAuth:
        """Create an instance of ApiV1AuthAwsAuthIdentitiesIdentityIdGet200ResponseIdentityAwsAuth from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if access_token_trusted_ips (nullable) is None
        # and __fields_set__ contains the field
        if self.access_token_trusted_ips is None and "access_token_trusted_ips" in self.__fields_set__:
            _dict['accessTokenTrustedIps'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AuthAwsAuthIdentitiesIdentityIdGet200ResponseIdentityAwsAuth:
        """Create an instance of ApiV1AuthAwsAuthIdentitiesIdentityIdGet200ResponseIdentityAwsAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AuthAwsAuthIdentitiesIdentityIdGet200ResponseIdentityAwsAuth.parse_obj(obj)

        _obj = ApiV1AuthAwsAuthIdentitiesIdentityIdGet200ResponseIdentityAwsAuth.parse_obj({
            "id": obj.get("id"),
            "access_token_ttl": obj.get("accessTokenTTL") if obj.get("accessTokenTTL") is not None else 7200,
            "access_token_max_ttl": obj.get("accessTokenMaxTTL") if obj.get("accessTokenMaxTTL") is not None else 7200,
            "access_token_num_uses_limit": obj.get("accessTokenNumUsesLimit") if obj.get("accessTokenNumUsesLimit") is not None else 0,
            "access_token_trusted_ips": obj.get("accessTokenTrustedIps"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "identity_id": obj.get("identityId"),
            "type": obj.get("type"),
            "sts_endpoint": obj.get("stsEndpoint"),
            "allowed_principal_arns": obj.get("allowedPrincipalArns"),
            "allowed_account_ids": obj.get("allowedAccountIds")
        })
        return _obj


