# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.playwright import Playwright  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPlaywrightController(BaseTestCase):
    """PlaywrightController integration test stubs"""

    def test_playwright_delete(self):
        """Test case for playwright_delete

        
        """
        query_string = [('author_id', 'author_id_example'),
                        ('name', 'name_example'),
                        ('biography', 'biography_example'),
                        ('contact_information', 'contact_information_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//playwright',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playwright_get(self):
        """Test case for playwright_get

        
        """
        query_string = [('author_id', 'author_id_example'),
                        ('name', 'name_example'),
                        ('biography', 'biography_example'),
                        ('contact_information', 'contact_information_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//playwright',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playwright_patch(self):
        """Test case for playwright_patch

        
        """
        body = Playwright()
        query_string = [('author_id', 'author_id_example'),
                        ('name', 'name_example'),
                        ('biography', 'biography_example'),
                        ('contact_information', 'contact_information_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//playwright',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_playwright_post(self):
        """Test case for playwright_post

        
        """
        body = Playwright()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//playwright',
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
