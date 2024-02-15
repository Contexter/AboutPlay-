# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.act import Act  # noqa: E501
from swagger_server.test import BaseTestCase


class TestActController(BaseTestCase):
    """ActController integration test stubs"""

    def test_act_delete(self):
        """Test case for act_delete

        
        """
        query_string = [('act_id', 'act_id_example'),
                        ('script_id', 'script_id_example'),
                        ('act_number', 'act_number_example'),
                        ('synopsis', 'synopsis_example'),
                        ('notes', 'notes_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//act',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_act_get(self):
        """Test case for act_get

        
        """
        query_string = [('act_id', 'act_id_example'),
                        ('script_id', 'script_id_example'),
                        ('act_number', 'act_number_example'),
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
            '//act',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_act_patch(self):
        """Test case for act_patch

        
        """
        body = Act()
        query_string = [('act_id', 'act_id_example'),
                        ('script_id', 'script_id_example'),
                        ('act_number', 'act_number_example'),
                        ('synopsis', 'synopsis_example'),
                        ('notes', 'notes_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//act',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_act_post(self):
        """Test case for act_post

        
        """
        body = Act()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//act',
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
