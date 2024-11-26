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

class ApiV1PkiCertificatesSerialNumberCertificateGet200Response(BaseModel):
    """
    ApiV1PkiCertificatesSerialNumberCertificateGet200Response
    """
    certificate: StrictStr = Field(default=..., description="The certificate body of the certificate")
    certificate_chain: StrictStr = Field(default=..., alias="certificateChain", description="The certificate chain of the certificate")
    serial_number: StrictStr = Field(default=..., alias="serialNumber", description="The serial number of the certificate")
    __properties = ["certificate", "certificateChain", "serialNumber"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1PkiCertificatesSerialNumberCertificateGet200Response:
        """Create an instance of ApiV1PkiCertificatesSerialNumberCertificateGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1PkiCertificatesSerialNumberCertificateGet200Response:
        """Create an instance of ApiV1PkiCertificatesSerialNumberCertificateGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1PkiCertificatesSerialNumberCertificateGet200Response.parse_obj(obj)

        _obj = ApiV1PkiCertificatesSerialNumberCertificateGet200Response.parse_obj({
            "certificate": obj.get("certificate"),
            "certificate_chain": obj.get("certificateChain"),
            "serial_number": obj.get("serialNumber")
        })
        return _obj


