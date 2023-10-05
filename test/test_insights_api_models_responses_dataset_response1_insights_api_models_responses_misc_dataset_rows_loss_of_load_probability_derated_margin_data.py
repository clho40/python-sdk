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

from openapi_client.models.insights_api_models_responses_dataset_response1_insights_api_models_responses_misc_dataset_rows_loss_of_load_probability_derated_margin_data import InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData  # noqa: E501

class TestInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData(unittest.TestCase):
    """InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData:
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData`
        """
        model = InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData(
                data = [
                    openapi_client.models.insights/api/models/responses/misc/dataset_rows/loss_of_load_probability_derated_margin_data.Insights.Api.Models.Responses.Misc.DatasetRows.LossOfLoadProbabilityDeratedMarginData(
                        dataset = 'LOLPDRM', 
                        publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        publishing_period_commencing_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        settlement_date = 'Tue Jan 31 01:00:00 CET 2023', 
                        settlement_period = 38, 
                        loss_of_load_probability = 0, 
                        derated_margin = 12570.207, )
                    ]
            )
        else:
            return InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData(
        )
        """

    def testInsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData(self):
        """Test InsightsApiModelsResponsesDatasetResponse1InsightsApiModelsResponsesMiscDatasetRowsLossOfLoadProbabilityDeratedMarginData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()