# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow(BaseModel):
    """
    InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow
    """
    dataset: Optional[StrictStr] = None
    document_id: Optional[StrictStr] = Field(None, alias="documentId")
    document_revision_number: Optional[StrictInt] = Field(None, alias="documentRevisionNumber")
    publish_time: Optional[datetime] = Field(None, alias="publishTime")
    business_type: Optional[StrictStr] = Field(None, alias="businessType")
    psr_type: Optional[StrictStr] = Field(None, alias="psrType")
    market_agreement_type: Optional[StrictStr] = Field(None, alias="marketAgreementType")
    flow_direction: Optional[StrictStr] = Field(None, alias="flowDirection")
    settlement_date: Optional[date] = Field(None, alias="settlementDate")
    quantity: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["dataset", "documentId", "documentRevisionNumber", "publishTime", "businessType", "psrType", "marketAgreementType", "flowDirection", "settlementDate", "quantity"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow:
        """Create an instance of InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if dataset (nullable) is None
        # and __fields_set__ contains the field
        if self.dataset is None and "dataset" in self.__fields_set__:
            _dict['dataset'] = None

        # set to None if document_id (nullable) is None
        # and __fields_set__ contains the field
        if self.document_id is None and "document_id" in self.__fields_set__:
            _dict['documentId'] = None

        # set to None if business_type (nullable) is None
        # and __fields_set__ contains the field
        if self.business_type is None and "business_type" in self.__fields_set__:
            _dict['businessType'] = None

        # set to None if psr_type (nullable) is None
        # and __fields_set__ contains the field
        if self.psr_type is None and "psr_type" in self.__fields_set__:
            _dict['psrType'] = None

        # set to None if market_agreement_type (nullable) is None
        # and __fields_set__ contains the field
        if self.market_agreement_type is None and "market_agreement_type" in self.__fields_set__:
            _dict['marketAgreementType'] = None

        # set to None if flow_direction (nullable) is None
        # and __fields_set__ contains the field
        if self.flow_direction is None and "flow_direction" in self.__fields_set__:
            _dict['flowDirection'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow:
        """Create an instance of InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.parse_obj(obj)

        _obj = InsightsApiModelsResponsesTransparencyDatasetRowsAbucDatasetRow.parse_obj({
            "dataset": obj.get("dataset"),
            "document_id": obj.get("documentId"),
            "document_revision_number": obj.get("documentRevisionNumber"),
            "publish_time": obj.get("publishTime"),
            "business_type": obj.get("businessType"),
            "psr_type": obj.get("psrType"),
            "market_agreement_type": obj.get("marketAgreementType"),
            "flow_direction": obj.get("flowDirection"),
            "settlement_date": obj.get("settlementDate"),
            "quantity": obj.get("quantity")
        })
        return _obj

