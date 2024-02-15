# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.scenelocation import Scenelocation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScenelocationController(BaseTestCase):
    """ScenelocationController integration test stubs"""

    def test_scenelocation_delete(self):
        """Test case for scenelocation_delete

        
        """
        query_string = [('location_id', 'location_id_example'),
                        ('description', 'description_example'),
                        ('historical_cultural_significance', 'historical_cultural_significance_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//scenelocation',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scenelocation_get(self):
        """Test case for scenelocation_get

        
        """
        query_string = [('location_id', 'location_id_example'),
                        ('description', 'description_example'),
                        ('historical_cultural_significance', 'historical_cultural_significance_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//scenelocation',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scenelocation_patch(self):
        """Test case for scenelocation_patch

        
        """
        body = Scenelocation()
        query_string = [('location_id', 'location_id_example'),
                        ('description', 'description_example'),
                        ('historical_cultural_significance', 'historical_cultural_significance_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//scenelocation',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scenelocation_post(self):
        """Test case for scenelocation_post

        
        """
        body = Scenelocation()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//scenelocation',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
