# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.parenthetical import Parenthetical  # noqa: E501
from swagger_server.test import BaseTestCase


class TestParentheticalController(BaseTestCase):
    """ParentheticalController integration test stubs"""

    def test_parenthetical_delete(self):
        """Test case for parenthetical_delete

        
        """
        query_string = [('parenthetical_id', 'parenthetical_id_example'),
                        ('dialogue_id', 'dialogue_id_example'),
                        ('original_text', 'original_text_example'),
                        ('modernized_text', 'modernized_text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//parenthetical',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parenthetical_get(self):
        """Test case for parenthetical_get

        
        """
        query_string = [('parenthetical_id', 'parenthetical_id_example'),
                        ('dialogue_id', 'dialogue_id_example'),
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
            '//parenthetical',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parenthetical_patch(self):
        """Test case for parenthetical_patch

        
        """
        body = Parenthetical()
        query_string = [('parenthetical_id', 'parenthetical_id_example'),
                        ('dialogue_id', 'dialogue_id_example'),
                        ('original_text', 'original_text_example'),
                        ('modernized_text', 'modernized_text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//parenthetical',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_parenthetical_post(self):
        """Test case for parenthetical_post

        
        """
        body = Parenthetical()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//parenthetical',
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
