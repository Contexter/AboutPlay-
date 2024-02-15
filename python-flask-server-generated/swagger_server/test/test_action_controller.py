# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.action import Action  # noqa: E501
from swagger_server.test import BaseTestCase


class TestActionController(BaseTestCase):
    """ActionController integration test stubs"""

    def test_action_delete(self):
        """Test case for action_delete

        
        """
        query_string = [('action_id', 'action_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('character_id', 'character_id_example'),
                        ('original_text', 'original_text_example'),
                        ('modernized_text', 'modernized_text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//action',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_action_get(self):
        """Test case for action_get

        
        """
        query_string = [('action_id', 'action_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('character_id', 'character_id_example'),
                        ('original_text', 'original_text_example'),
                        ('modernized_text', 'modernized_text_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//action',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_action_patch(self):
        """Test case for action_patch

        
        """
        body = Action()
        query_string = [('action_id', 'action_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('character_id', 'character_id_example'),
                        ('original_text', 'original_text_example'),
                        ('modernized_text', 'modernized_text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//action',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_action_post(self):
        """Test case for action_post

        
        """
        body = Action()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//action',
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
