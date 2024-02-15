# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.titlepage import Titlepage  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTitlepageController(BaseTestCase):
    """TitlepageController integration test stubs"""

    def test_titlepage_delete(self):
        """Test case for titlepage_delete

        
        """
        query_string = [('title_page_id', 'title_page_id_example'),
                        ('script_id', 'script_id_example'),
                        ('text', 'text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//titlepage',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_titlepage_get(self):
        """Test case for titlepage_get

        
        """
        query_string = [('title_page_id', 'title_page_id_example'),
                        ('script_id', 'script_id_example'),
                        ('text', 'text_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//titlepage',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_titlepage_patch(self):
        """Test case for titlepage_patch

        
        """
        body = Titlepage()
        query_string = [('title_page_id', 'title_page_id_example'),
                        ('script_id', 'script_id_example'),
                        ('text', 'text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//titlepage',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_titlepage_post(self):
        """Test case for titlepage_post

        
        """
        body = Titlepage()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//titlepage',
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
