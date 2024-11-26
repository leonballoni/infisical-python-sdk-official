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



from pydantic import ConfigDict, BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_organization_get200_response_organizations_inner import ApiV1OrganizationGet200ResponseOrganizationsInner

class ApiV1OrganizationOrganizationIdPatch200Response(BaseModel):
    """
    ApiV1OrganizationOrganizationIdPatch200Response
    """
    message: StrictStr = Field(...)
    organization: ApiV1OrganizationGet200ResponseOrganizationsInner = Field(...)
    __properties = ["message", "organization"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1OrganizationOrganizationIdPatch200Response:
        """Create an instance of ApiV1OrganizationOrganizationIdPatch200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1OrganizationOrganizationIdPatch200Response:
        """Create an instance of ApiV1OrganizationOrganizationIdPatch200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1OrganizationOrganizationIdPatch200Response.parse_obj(obj)

        _obj = ApiV1OrganizationOrganizationIdPatch200Response.parse_obj({
            "message": obj.get("message"),
            "organization": ApiV1OrganizationGet200ResponseOrganizationsInner.from_dict(obj.get("organization")) if obj.get("organization") is not None else None
        })
        return _obj


