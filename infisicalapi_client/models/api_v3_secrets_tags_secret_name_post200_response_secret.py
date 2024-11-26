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
from typing import Any, List, Optional, Union
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from infisicalapi_client.models.api_v3_secrets_tags_secret_name_post200_response_secret_tags_inner import ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner
from typing_extensions import Annotated

class ApiV3SecretsTagsSecretNamePost200ResponseSecret(BaseModel):
    """
    ApiV3SecretsTagsSecretNamePost200ResponseSecret
    """
    id: StrictStr = Field(...)
    version: Optional[Union[StrictFloat, StrictInt]] = 1
    type: Optional[StrictStr] = 'shared'
    secret_key_ciphertext: StrictStr = Field(default=..., alias="secretKeyCiphertext")
    secret_key_iv: StrictStr = Field(default=..., alias="secretKeyIV")
    secret_key_tag: StrictStr = Field(default=..., alias="secretKeyTag")
    secret_value_ciphertext: StrictStr = Field(default=..., alias="secretValueCiphertext")
    secret_value_iv: StrictStr = Field(default=..., alias="secretValueIV")
    secret_value_tag: StrictStr = Field(default=..., alias="secretValueTag")
    secret_comment_ciphertext: Optional[StrictStr] = Field(default=None, alias="secretCommentCiphertext")
    secret_comment_iv: Optional[StrictStr] = Field(default=None, alias="secretCommentIV")
    secret_comment_tag: Optional[StrictStr] = Field(default=None, alias="secretCommentTag")
    secret_reminder_note: Optional[StrictStr] = Field(default=None, alias="secretReminderNote")
    secret_reminder_repeat_days: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="secretReminderRepeatDays")
    skip_multiline_encoding: Optional[StrictBool] = Field(default=False, alias="skipMultilineEncoding")
    algorithm: Optional[StrictStr] = 'aes-256-gcm'
    key_encoding: Optional[StrictStr] = Field(default='utf8', alias="keyEncoding")
    metadata: Optional[Any] = None
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
    folder_id: StrictStr = Field(default=..., alias="folderId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    tags: Annotated[List[ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner], Field()] = Field(...)
    __properties = ["id", "version", "type", "secretKeyCiphertext", "secretKeyIV", "secretKeyTag", "secretValueCiphertext", "secretValueIV", "secretValueTag", "secretCommentCiphertext", "secretCommentIV", "secretCommentTag", "secretReminderNote", "secretReminderRepeatDays", "skipMultilineEncoding", "algorithm", "keyEncoding", "metadata", "userId", "folderId", "createdAt", "updatedAt", "tags"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV3SecretsTagsSecretNamePost200ResponseSecret:
        """Create an instance of ApiV3SecretsTagsSecretNamePost200ResponseSecret from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # set to None if secret_comment_ciphertext (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_comment_ciphertext is None and "secret_comment_ciphertext" in self.__fields_set__:
            _dict['secretCommentCiphertext'] = None

        # set to None if secret_comment_iv (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_comment_iv is None and "secret_comment_iv" in self.__fields_set__:
            _dict['secretCommentIV'] = None

        # set to None if secret_comment_tag (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_comment_tag is None and "secret_comment_tag" in self.__fields_set__:
            _dict['secretCommentTag'] = None

        # set to None if secret_reminder_note (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_reminder_note is None and "secret_reminder_note" in self.__fields_set__:
            _dict['secretReminderNote'] = None

        # set to None if secret_reminder_repeat_days (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_reminder_repeat_days is None and "secret_reminder_repeat_days" in self.__fields_set__:
            _dict['secretReminderRepeatDays'] = None

        # set to None if skip_multiline_encoding (nullable) is None
        # and __fields_set__ contains the field
        if self.skip_multiline_encoding is None and "skip_multiline_encoding" in self.__fields_set__:
            _dict['skipMultilineEncoding'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id is None and "user_id" in self.__fields_set__:
            _dict['userId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV3SecretsTagsSecretNamePost200ResponseSecret:
        """Create an instance of ApiV3SecretsTagsSecretNamePost200ResponseSecret from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV3SecretsTagsSecretNamePost200ResponseSecret.parse_obj(obj)

        _obj = ApiV3SecretsTagsSecretNamePost200ResponseSecret.parse_obj({
            "id": obj.get("id"),
            "version": obj.get("version") if obj.get("version") is not None else 1,
            "type": obj.get("type") if obj.get("type") is not None else 'shared',
            "secret_key_ciphertext": obj.get("secretKeyCiphertext"),
            "secret_key_iv": obj.get("secretKeyIV"),
            "secret_key_tag": obj.get("secretKeyTag"),
            "secret_value_ciphertext": obj.get("secretValueCiphertext"),
            "secret_value_iv": obj.get("secretValueIV"),
            "secret_value_tag": obj.get("secretValueTag"),
            "secret_comment_ciphertext": obj.get("secretCommentCiphertext"),
            "secret_comment_iv": obj.get("secretCommentIV"),
            "secret_comment_tag": obj.get("secretCommentTag"),
            "secret_reminder_note": obj.get("secretReminderNote"),
            "secret_reminder_repeat_days": obj.get("secretReminderRepeatDays"),
            "skip_multiline_encoding": obj.get("skipMultilineEncoding") if obj.get("skipMultilineEncoding") is not None else False,
            "algorithm": obj.get("algorithm") if obj.get("algorithm") is not None else 'aes-256-gcm',
            "key_encoding": obj.get("keyEncoding") if obj.get("keyEncoding") is not None else 'utf8',
            "metadata": obj.get("metadata"),
            "user_id": obj.get("userId"),
            "folder_id": obj.get("folderId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "tags": [ApiV3SecretsTagsSecretNamePost200ResponseSecretTagsInner.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None
        })
        return _obj


