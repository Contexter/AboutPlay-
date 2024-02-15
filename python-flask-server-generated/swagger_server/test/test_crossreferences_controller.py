# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.crossreferences import Crossreferences  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCrossreferencesController(BaseTestCase):
    """CrossreferencesController integration test stubs"""

    def test_crossreferences_delete(self):
        """Test case for crossreferences_delete

        
        """
        query_string = [('cross_reference_id', 'cross_reference_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('referenced_scene_id', 'referenced_scene_id_example'),
                        ('description', 'description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//crossreferences',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crossreferences_get(self):
        """Test case for crossreferences_get

        
        """
        query_string = [('cross_reference_id', 'cross_reference_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('referenced_scene_id', 'referenced_scene_id_example'),
                        ('description', 'description_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//crossreferences',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crossreferences_patch(self):
        """Test case for crossreferences_patch

        
        """
        body = Crossreferences()
        query_string = [('cross_reference_id', 'cross_reference_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('referenced_scene_id', 'referenced_scene_id_example'),
                        ('description', 'description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//crossreferences',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crossreferences_post(self):
        """Test case for crossreferences_post

        
        """
        body = Crossreferences()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//crossreferences',
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
