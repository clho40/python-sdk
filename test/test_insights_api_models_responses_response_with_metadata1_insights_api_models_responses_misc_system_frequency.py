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

from openapi_client.models.insights_api_models_responses_response_with_metadata1_insights_api_models_responses_misc_system_frequency import InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency  # noqa: E501

class TestInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency(unittest.TestCase):
    """InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency:
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency`
        """
        model = InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency(
                data = [
                    openapi_client.models.insights/api/models/responses/misc/system_frequency.Insights.Api.Models.Responses.Misc.SystemFrequency(
                        measurement_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        frequency = 1.337, )
                    ],
                metadata = openapi_client.models.insights/api/models/metadata/api_response_source_metadata.Insights.Api.Models.Metadata.ApiResponseSourceMetadata(
                    datasets = ["DATASET"], )
            )
        else:
            return InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency(
        )
        """

    def testInsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency(self):
        """Test InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()