# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.script import Script  # noqa: E501
from swagger_server.test import BaseTestCase


class TestScriptController(BaseTestCase):
    """ScriptController integration test stubs"""

    def test_script_delete(self):
        """Test case for script_delete

        
        """
        query_string = [('script_id', 'script_id_example'),
                        ('title', 'title_example'),
                        ('author_id', 'author_id_example'),
                        ('url', 'url_example'),
                        ('metadata_id', 'metadata_id_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//script',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_script_get(self):
        """Test case for script_get

        
        """
        query_string = [('script_id', 'script_id_example'),
                        ('title', 'title_example'),
                        ('author_id', 'author_id_example'),
                        ('url', 'url_example'),
                        ('metadata_id', 'metadata_id_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//script',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_script_patch(self):
        """Test case for script_patch

        
        """
        body = Script()
        query_string = [('script_id', 'script_id_example'),
                        ('title', 'title_example'),
                        ('author_id', 'author_id_example'),
                        ('url', 'url_example'),
                        ('metadata_id', 'metadata_id_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//script',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_script_post(self):
        """Test case for script_post

        
        """
        body = Script()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//script',
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
