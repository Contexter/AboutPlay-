# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.scene import Scene  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSceneController(BaseTestCase):
    """SceneController integration test stubs"""

    def test_scene_delete(self):
        """Test case for scene_delete

        
        """
        query_string = [('scene_id', 'scene_id_example'),
                        ('act_id', 'act_id_example'),
                        ('scene_number', 'scene_number_example'),
                        ('synopsis', 'synopsis_example'),
                        ('notes', 'notes_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//scene',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scene_get(self):
        """Test case for scene_get

        
        """
        query_string = [('scene_id', 'scene_id_example'),
                        ('act_id', 'act_id_example'),
                        ('scene_number', 'scene_number_example'),
                        ('synopsis', 'synopsis_example'),
                        ('notes', 'notes_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//scene',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scene_patch(self):
        """Test case for scene_patch

        
        """
        body = Scene()
        query_string = [('scene_id', 'scene_id_example'),
                        ('act_id', 'act_id_example'),
                        ('scene_number', 'scene_number_example'),
                        ('synopsis', 'synopsis_example'),
                        ('notes', 'notes_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//scene',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scene_post(self):
        """Test case for scene_post

        
        """
        body = Scene()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//scene',
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
