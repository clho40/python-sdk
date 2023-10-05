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

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_balancing_market_index_response import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse  # noqa: E501

class TestInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse(unittest.TestCase):
    """InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse:
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse`
        """
        model = InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse(
                data = [
                    openapi_client.models.insights/api/models/responses/balancing/market_index_response.Insights.Api.Models.Responses.Balancing.MarketIndexResponse(
                        start_time = '2022-09-26T13:00Z', 
                        data_provider = 'N2EXMIDP', 
                        settlement_date = 'Mon Sep 26 02:00:00 CEST 2022', 
                        settlement_period = 3, 
                        price = 678.12, 
                        volume = 678.123, )
                    ],
                metadata = openapi_client.models.insights/api/models/metadata/api_response_source_metadata.Insights.Api.Models.Metadata.ApiResponseSourceMetadata(
                    datasets = ["DATASET"], )
            )
        else:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse(
        )
        """

    def testInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse(self):
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesBalancingMarketIndexResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()