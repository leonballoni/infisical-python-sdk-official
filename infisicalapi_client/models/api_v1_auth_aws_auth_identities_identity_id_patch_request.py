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
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_auth_token_auth_identities_identity_id_post_request_access_token_trusted_ips_inner import ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner
from typing_extensions import Annotated

class ApiV1AuthAwsAuthIdentitiesIdentityIdPatchRequest(BaseModel):
    """
    ApiV1AuthAwsAuthIdentitiesIdentityIdPatchRequest
    """
    sts_endpoint: Optional[Annotated[str, StringConstraints(strict=True, min_length=1)]] = Field(default=None, alias="stsEndpoint", description="The new endpoint URL for the AWS STS API.")
    allowed_principal_arns: Optional[StrictStr] = Field(default='', alias="allowedPrincipalArns", description="The new comma-separated list of trusted IAM principal ARNs that are allowed to authenticate with Infisical.")
    allowed_account_ids: Optional[StrictStr] = Field(default='', alias="allowedAccountIds", description="The new comma-separated list of trusted AWS account IDs that are allowed to authenticate with Infisical.")
    access_token_trusted_ips: Optional[Annotated[List[ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner], Field(min_length=1)]] = Field(default=None, alias="accessTokenTrustedIps", description="The new IPs or CIDR ranges that access tokens can be used from.")
    access_token_ttl: Optional[Annotated[int, Field(strict=True, le=315360000, ge=0)]] = Field(default=None, alias="accessTokenTTL", description="The new lifetime for an acccess token in seconds.")
    access_token_num_uses_limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="accessTokenNumUsesLimit", description="The new maximum number of times that an access token can be used.")
    access_token_max_ttl: Optional[Annotated[int, Field(strict=True, le=315360000)]] = Field(default=None, alias="accessTokenMaxTTL", description="The new maximum lifetime for an acccess token in seconds.")
    __properties = ["stsEndpoint", "allowedPrincipalArns", "allowedAccountIds", "accessTokenTrustedIps", "accessTokenTTL", "accessTokenNumUsesLimit", "accessTokenMaxTTL"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1AuthAwsAuthIdentitiesIdentityIdPatchRequest:
        """Create an instance of ApiV1AuthAwsAuthIdentitiesIdentityIdPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in access_token_trusted_ips (list)
        _items = []
        if self.access_token_trusted_ips:
            for _item in self.access_token_trusted_ips:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accessTokenTrustedIps'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AuthAwsAuthIdentitiesIdentityIdPatchRequest:
        """Create an instance of ApiV1AuthAwsAuthIdentitiesIdentityIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AuthAwsAuthIdentitiesIdentityIdPatchRequest.parse_obj(obj)

        _obj = ApiV1AuthAwsAuthIdentitiesIdentityIdPatchRequest.parse_obj({
            "sts_endpoint": obj.get("stsEndpoint"),
            "allowed_principal_arns": obj.get("allowedPrincipalArns") if obj.get("allowedPrincipalArns") is not None else '',
            "allowed_account_ids": obj.get("allowedAccountIds") if obj.get("allowedAccountIds") is not None else '',
            "access_token_trusted_ips": [ApiV1AuthTokenAuthIdentitiesIdentityIdPostRequestAccessTokenTrustedIpsInner.from_dict(_item) for _item in obj.get("accessTokenTrustedIps")] if obj.get("accessTokenTrustedIps") is not None else None,
            "access_token_ttl": obj.get("accessTokenTTL"),
            "access_token_num_uses_limit": obj.get("accessTokenNumUsesLimit"),
            "access_token_max_ttl": obj.get("accessTokenMaxTTL")
        })
        return _obj


