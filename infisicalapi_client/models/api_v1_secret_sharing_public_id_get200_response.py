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
from typing import Optional, Union
from pydantic import ConfigDict, BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ApiV1SecretSharingPublicIdGet200Response(BaseModel):
    """
    ApiV1SecretSharingPublicIdGet200Response
    """
    encrypted_value: StrictStr = Field(default=..., alias="encryptedValue")
    iv: StrictStr = Field(...)
    tag: StrictStr = Field(...)
    expires_at: datetime = Field(default=..., alias="expiresAt")
    expires_after_views: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="expiresAfterViews")
    access_type: Optional[StrictStr] = Field(default='anyone', alias="accessType")
    org_name: Optional[StrictStr] = Field(default=None, alias="orgName")
    __properties = ["encryptedValue", "iv", "tag", "expiresAt", "expiresAfterViews", "accessType", "orgName"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretSharingPublicIdGet200Response:
        """Create an instance of ApiV1SecretSharingPublicIdGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if expires_after_views (nullable) is None
        # and __fields_set__ contains the field
        if self.expires_after_views is None and "expires_after_views" in self.__fields_set__:
            _dict['expiresAfterViews'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretSharingPublicIdGet200Response:
        """Create an instance of ApiV1SecretSharingPublicIdGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretSharingPublicIdGet200Response.parse_obj(obj)

        _obj = ApiV1SecretSharingPublicIdGet200Response.parse_obj({
            "encrypted_value": obj.get("encryptedValue"),
            "iv": obj.get("iv"),
            "tag": obj.get("tag"),
            "expires_at": obj.get("expiresAt"),
            "expires_after_views": obj.get("expiresAfterViews"),
            "access_type": obj.get("accessType") if obj.get("accessType") is not None else 'anyone',
            "org_name": obj.get("orgName")
        })
        return _obj


