# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.extendednotesresearch import Extendednotesresearch  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExtendednotesresearchController(BaseTestCase):
    """ExtendednotesresearchController integration test stubs"""

    def test_extendednotesresearch_delete(self):
        """Test case for extendednotesresearch_delete

        
        """
        query_string = [('research_id', 'research_id_example'),
                        ('script_id', 'script_id_example'),
                        ('notes', 'notes_example'),
                        ('research_details', 'research_details_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//extendednotesresearch',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_extendednotesresearch_get(self):
        """Test case for extendednotesresearch_get

        
        """
        query_string = [('research_id', 'research_id_example'),
                        ('script_id', 'script_id_example'),
                        ('notes', 'notes_example'),
                        ('research_details', 'research_details_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//extendednotesresearch',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_extendednotesresearch_patch(self):
        """Test case for extendednotesresearch_patch

        
        """
        body = Extendednotesresearch()
        query_string = [('research_id', 'research_id_example'),
                        ('script_id', 'script_id_example'),
                        ('notes', 'notes_example'),
                        ('research_details', 'research_details_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//extendednotesresearch',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_extendednotesresearch_post(self):
        """Test case for extendednotesresearch_post

        
        """
        body = Extendednotesresearch()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//extendednotesresearch',
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
