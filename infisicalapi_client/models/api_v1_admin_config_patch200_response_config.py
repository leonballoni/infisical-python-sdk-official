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
from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr
from typing_extensions import Annotated

class ApiV1AdminConfigPatch200ResponseConfig(BaseModel):
    """
    ApiV1AdminConfigPatch200ResponseConfig
    """
    id: StrictStr = Field(...)
    initialized: Optional[StrictBool] = False
    allow_sign_up: Optional[StrictBool] = Field(default=True, alias="allowSignUp")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    allowed_sign_up_domain: Optional[StrictStr] = Field(default=None, alias="allowedSignUpDomain")
    instance_id: Optional[StrictStr] = Field(default='00000000-0000-0000-0000-000000000000', alias="instanceId")
    trust_saml_emails: Optional[StrictBool] = Field(default=False, alias="trustSamlEmails")
    trust_ldap_emails: Optional[StrictBool] = Field(default=False, alias="trustLdapEmails")
    trust_oidc_emails: Optional[StrictBool] = Field(default=False, alias="trustOidcEmails")
    default_auth_org_id: Optional[StrictStr] = Field(default=None, alias="defaultAuthOrgId")
    enabled_login_methods: Optional[Annotated[List[StrictStr], Field()]] = Field(default=None, alias="enabledLoginMethods")
    default_auth_org_slug: Optional[StrictStr] = Field(default=..., alias="defaultAuthOrgSlug")
    __properties = ["id", "initialized", "allowSignUp", "createdAt", "updatedAt", "allowedSignUpDomain", "instanceId", "trustSamlEmails", "trustLdapEmails", "trustOidcEmails", "defaultAuthOrgId", "enabledLoginMethods", "defaultAuthOrgSlug"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1AdminConfigPatch200ResponseConfig:
        """Create an instance of ApiV1AdminConfigPatch200ResponseConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if initialized (nullable) is None
        # and __fields_set__ contains the field
        if self.initialized is None and "initialized" in self.__fields_set__:
            _dict['initialized'] = None

        # set to None if allow_sign_up (nullable) is None
        # and __fields_set__ contains the field
        if self.allow_sign_up is None and "allow_sign_up" in self.__fields_set__:
            _dict['allowSignUp'] = None

        # set to None if allowed_sign_up_domain (nullable) is None
        # and __fields_set__ contains the field
        if self.allowed_sign_up_domain is None and "allowed_sign_up_domain" in self.__fields_set__:
            _dict['allowedSignUpDomain'] = None

        # set to None if trust_saml_emails (nullable) is None
        # and __fields_set__ contains the field
        if self.trust_saml_emails is None and "trust_saml_emails" in self.__fields_set__:
            _dict['trustSamlEmails'] = None

        # set to None if trust_ldap_emails (nullable) is None
        # and __fields_set__ contains the field
        if self.trust_ldap_emails is None and "trust_ldap_emails" in self.__fields_set__:
            _dict['trustLdapEmails'] = None

        # set to None if trust_oidc_emails (nullable) is None
        # and __fields_set__ contains the field
        if self.trust_oidc_emails is None and "trust_oidc_emails" in self.__fields_set__:
            _dict['trustOidcEmails'] = None

        # set to None if default_auth_org_id (nullable) is None
        # and __fields_set__ contains the field
        if self.default_auth_org_id is None and "default_auth_org_id" in self.__fields_set__:
            _dict['defaultAuthOrgId'] = None

        # set to None if enabled_login_methods (nullable) is None
        # and __fields_set__ contains the field
        if self.enabled_login_methods is None and "enabled_login_methods" in self.__fields_set__:
            _dict['enabledLoginMethods'] = None

        # set to None if default_auth_org_slug (nullable) is None
        # and __fields_set__ contains the field
        if self.default_auth_org_slug is None and "default_auth_org_slug" in self.__fields_set__:
            _dict['defaultAuthOrgSlug'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AdminConfigPatch200ResponseConfig:
        """Create an instance of ApiV1AdminConfigPatch200ResponseConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AdminConfigPatch200ResponseConfig.parse_obj(obj)

        _obj = ApiV1AdminConfigPatch200ResponseConfig.parse_obj({
            "id": obj.get("id"),
            "initialized": obj.get("initialized") if obj.get("initialized") is not None else False,
            "allow_sign_up": obj.get("allowSignUp") if obj.get("allowSignUp") is not None else True,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "allowed_sign_up_domain": obj.get("allowedSignUpDomain"),
            "instance_id": obj.get("instanceId") if obj.get("instanceId") is not None else '00000000-0000-0000-0000-000000000000',
            "trust_saml_emails": obj.get("trustSamlEmails") if obj.get("trustSamlEmails") is not None else False,
            "trust_ldap_emails": obj.get("trustLdapEmails") if obj.get("trustLdapEmails") is not None else False,
            "trust_oidc_emails": obj.get("trustOidcEmails") if obj.get("trustOidcEmails") is not None else False,
            "default_auth_org_id": obj.get("defaultAuthOrgId"),
            "enabled_login_methods": obj.get("enabledLoginMethods"),
            "default_auth_org_slug": obj.get("defaultAuthOrgSlug")
        })
        return _obj


