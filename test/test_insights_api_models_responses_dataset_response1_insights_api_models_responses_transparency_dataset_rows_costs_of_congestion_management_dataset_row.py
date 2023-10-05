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

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_transparency_dataset_rows_costs_of_congestion_management_dataset_row import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow(
                data = [
                    openapi_client.models.insights/api/models/responses/transparency/dataset_rows/costs_of_congestion_management_dataset_row.Insights.Api.Models.Responses.Transparency.DatasetRows.CostsOfCongestionManagementDatasetRow(
                        dataset = 'CCM', 
                        document_id = 'NGET-EMFIP-CCM-00688999', 
                        document_revision_number = 1, 
                        publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        business_type = 'Congestion costs', 
                        year = 2023, 
                        month = 'OCT', 
                        amount = 1.08, )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesTransparencyDatasetRowsCostsOfCongestionManagementDatasetRow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()