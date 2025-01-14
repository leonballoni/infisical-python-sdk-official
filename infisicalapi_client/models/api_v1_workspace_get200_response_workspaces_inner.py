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
from typing import List, Optional, Union
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from infisicalapi_client.models.api_v1_secret_imports_get200_response_secret_imports_inner_import_env import ApiV1SecretImportsGet200ResponseSecretImportsInnerImportEnv
from typing_extensions import Annotated

class ApiV1WorkspaceGet200ResponseWorkspacesInner(BaseModel):
    """
    ApiV1WorkspaceGet200ResponseWorkspacesInner
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    slug: StrictStr = Field(...)
    auto_capitalization: Optional[StrictBool] = Field(default=True, alias="autoCapitalization")
    org_id: StrictStr = Field(default=..., alias="orgId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    version: Optional[Union[StrictFloat, StrictInt]] = 1
    upgrade_status: Optional[StrictStr] = Field(default=None, alias="upgradeStatus")
    pit_version_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=10, alias="pitVersionLimit")
    kms_certificate_key_id: Optional[StrictStr] = Field(default=None, alias="kmsCertificateKeyId")
    audit_logs_retention_days: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="auditLogsRetentionDays")
    id: StrictStr = Field(default=..., alias="_id")
    environments: Annotated[List[ApiV1SecretImportsGet200ResponseSecretImportsInnerImportEnv], Field()] = Field(...)
    __properties = ["id", "name", "slug", "autoCapitalization", "orgId", "createdAt", "updatedAt", "version", "upgradeStatus", "pitVersionLimit", "kmsCertificateKeyId", "auditLogsRetentionDays", "_id", "environments"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceGet200ResponseWorkspacesInner:
        """Create an instance of ApiV1WorkspaceGet200ResponseWorkspacesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in environments (list)
        _items = []
        if self.environments:
            for _item in self.environments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['environments'] = _items
        # set to None if auto_capitalization (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_capitalization is None and "auto_capitalization" in self.__fields_set__:
            _dict['autoCapitalization'] = None

        # set to None if upgrade_status (nullable) is None
        # and __fields_set__ contains the field
        if self.upgrade_status is None and "upgrade_status" in self.__fields_set__:
            _dict['upgradeStatus'] = None

        # set to None if kms_certificate_key_id (nullable) is None
        # and __fields_set__ contains the field
        if self.kms_certificate_key_id is None and "kms_certificate_key_id" in self.__fields_set__:
            _dict['kmsCertificateKeyId'] = None

        # set to None if audit_logs_retention_days (nullable) is None
        # and __fields_set__ contains the field
        if self.audit_logs_retention_days is None and "audit_logs_retention_days" in self.__fields_set__:
            _dict['auditLogsRetentionDays'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceGet200ResponseWorkspacesInner:
        """Create an instance of ApiV1WorkspaceGet200ResponseWorkspacesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceGet200ResponseWorkspacesInner.parse_obj(obj)

        _obj = ApiV1WorkspaceGet200ResponseWorkspacesInner.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "auto_capitalization": obj.get("autoCapitalization") if obj.get("autoCapitalization") is not None else True,
            "org_id": obj.get("orgId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "version": obj.get("version") if obj.get("version") is not None else 1,
            "upgrade_status": obj.get("upgradeStatus"),
            "pit_version_limit": obj.get("pitVersionLimit") if obj.get("pitVersionLimit") is not None else 10,
            "kms_certificate_key_id": obj.get("kmsCertificateKeyId"),
            "audit_logs_retention_days": obj.get("auditLogsRetentionDays"),
            "id": obj.get("_id"),
            "environments": [ApiV1SecretImportsGet200ResponseSecretImportsInnerImportEnv.from_dict(_item) for _item in obj.get("environments")] if obj.get("environments") is not None else None
        })
        return _obj


