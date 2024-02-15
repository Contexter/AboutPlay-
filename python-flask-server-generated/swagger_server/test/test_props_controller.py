# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.props import Props  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPropsController(BaseTestCase):
    """PropsController integration test stubs"""

    def test_props_delete(self):
        """Test case for props_delete

        
        """
        query_string = [('prop_id', 'prop_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('description', 'description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//props',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_props_get(self):
        """Test case for props_get

        
        """
        query_string = [('prop_id', 'prop_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('description', 'description_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//props',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_props_patch(self):
        """Test case for props_patch

        
        """
        body = Props()
        query_string = [('prop_id', 'prop_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('description', 'description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//props',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_props_post(self):
        """Test case for props_post

        
        """
        body = Props()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//props',
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
