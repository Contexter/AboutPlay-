# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.character import Character  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCharacterController(BaseTestCase):
    """CharacterController integration test stubs"""

    def test_character_delete(self):
        """Test case for character_delete

        
        """
        query_string = [('character_id', 'character_id_example'),
                        ('script_id', 'script_id_example'),
                        ('name', 'name_example'),
                        ('description', 'description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//character',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_character_get(self):
        """Test case for character_get

        
        """
        query_string = [('character_id', 'character_id_example'),
                        ('script_id', 'script_id_example'),
                        ('name', 'name_example'),
                        ('description', 'description_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//character',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_character_patch(self):
        """Test case for character_patch

        
        """
        body = Character()
        query_string = [('character_id', 'character_id_example'),
                        ('script_id', 'script_id_example'),
                        ('name', 'name_example'),
                        ('description', 'description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//character',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_character_post(self):
        """Test case for character_post

        
        """
        body = Character()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//character',
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
