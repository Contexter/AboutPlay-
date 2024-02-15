# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pagebreak import Pagebreak  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPagebreakController(BaseTestCase):
    """PagebreakController integration test stubs"""

    def test_pagebreak_delete(self):
        """Test case for pagebreak_delete

        
        """
        query_string = [('page_break_id', 'page_break_id_example'),
                        ('script_id', 'script_id_example'),
                        ('page_number', 'page_number_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//pagebreak',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pagebreak_get(self):
        """Test case for pagebreak_get

        
        """
        query_string = [('page_break_id', 'page_break_id_example'),
                        ('script_id', 'script_id_example'),
                        ('page_number', 'page_number_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//pagebreak',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pagebreak_patch(self):
        """Test case for pagebreak_patch

        
        """
        body = Pagebreak()
        query_string = [('page_break_id', 'page_break_id_example'),
                        ('script_id', 'script_id_example'),
                        ('page_number', 'page_number_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//pagebreak',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pagebreak_post(self):
        """Test case for pagebreak_post

        
        """
        body = Pagebreak()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//pagebreak',
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
