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

class ApiV1PasswordPasswordResetPostRequest(BaseModel):
    """
    ApiV1PasswordPasswordResetPostRequest
    """
    protected_key: StrictStr = Field(default=..., alias="protectedKey")
    protected_key_iv: StrictStr = Field(default=..., alias="protectedKeyIV")
    protected_key_tag: StrictStr = Field(default=..., alias="protectedKeyTag")
    encrypted_private_key: StrictStr = Field(default=..., alias="encryptedPrivateKey")
    encrypted_private_key_iv: StrictStr = Field(default=..., alias="encryptedPrivateKeyIV")
    encrypted_private_key_tag: StrictStr = Field(default=..., alias="encryptedPrivateKeyTag")
    salt: StrictStr = Field(...)
    verifier: StrictStr = Field(...)
    __properties = ["protectedKey", "protectedKeyIV", "protectedKeyTag", "encryptedPrivateKey", "encryptedPrivateKeyIV", "encryptedPrivateKeyTag", "salt", "verifier"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1PasswordPasswordResetPostRequest:
        """Create an instance of ApiV1PasswordPasswordResetPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1PasswordPasswordResetPostRequest:
        """Create an instance of ApiV1PasswordPasswordResetPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1PasswordPasswordResetPostRequest.parse_obj(obj)

        _obj = ApiV1PasswordPasswordResetPostRequest.parse_obj({
            "protected_key": obj.get("protectedKey"),
            "protected_key_iv": obj.get("protectedKeyIV"),
            "protected_key_tag": obj.get("protectedKeyTag"),
            "encrypted_private_key": obj.get("encryptedPrivateKey"),
            "encrypted_private_key_iv": obj.get("encryptedPrivateKeyIV"),
            "encrypted_private_key_tag": obj.get("encryptedPrivateKeyTag"),
            "salt": obj.get("salt"),
            "verifier": obj.get("verifier")
        })
        return _obj


