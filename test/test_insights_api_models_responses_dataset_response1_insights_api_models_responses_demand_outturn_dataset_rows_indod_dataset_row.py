# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_demand_outturn_dataset_rows_indod_dataset_row import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow(
                data = [
                    openapi_client.models.insights/api/models/responses/demand_outturn/dataset_rows/indod_dataset_row.Insights.Api.Models.Responses.DemandOutturn.DatasetRows.IndodDatasetRow(
                        dataset = 'INDOD', 
                        publish_time = '2023-08-26T23:15Z', 
                        settlement_date = 'Sat Aug 26 02:00:00 CEST 2023', 
                        demand = 494802, )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesDemandOutturnDatasetRowsIndodDatasetRow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()