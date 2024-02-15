# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dialogue import Dialogue  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDialogueController(BaseTestCase):
    """DialogueController integration test stubs"""

    def test_dialogue_delete(self):
        """Test case for dialogue_delete

        
        """
        query_string = [('dialogue_id', 'dialogue_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('character_id', 'character_id_example'),
                        ('original_text', 'original_text_example'),
                        ('modernized_text', 'modernized_text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//dialogue',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dialogue_get(self):
        """Test case for dialogue_get

        
        """
        query_string = [('dialogue_id', 'dialogue_id_example'),
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
            '//dialogue',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dialogue_patch(self):
        """Test case for dialogue_patch

        
        """
        body = Dialogue()
        query_string = [('dialogue_id', 'dialogue_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('character_id', 'character_id_example'),
                        ('original_text', 'original_text_example'),
                        ('modernized_text', 'modernized_text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//dialogue',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_dialogue_post(self):
        """Test case for dialogue_post

        
        """
        body = Dialogue()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//dialogue',
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
