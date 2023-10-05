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

from openapi_client.models.insights_api_models_responses_generation_dataset_rows_availability_weekly import InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly  # noqa: E501

class TestInsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly(unittest.TestCase):
    """InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly:
        """Test InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly`
        """
        model = InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly()  # noqa: E501
        if include_optional:
            return InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly(
                dataset = '',
                publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                system_zone = '',
                calendar_week_number = 56,
                year = 56,
                output_usable = 56
            )
        else:
            return InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly(
        )
        """

    def testInsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly(self):
        """Test InsightsApiModelsResponsesGenerationDatasetRowsAvailabilityWeekly"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()