# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.revisionhistory import Revisionhistory  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRevisionhistoryController(BaseTestCase):
    """RevisionhistoryController integration test stubs"""

    def test_revisionhistory_delete(self):
        """Test case for revisionhistory_delete

        
        """
        query_string = [('revision_id', 'revision_id_example'),
                        ('script_id', 'script_id_example'),
                        ('_date', '2013-10-20'),
                        ('change_description', 'change_description_example'),
                        ('editor', 'editor_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//revisionhistory',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_revisionhistory_get(self):
        """Test case for revisionhistory_get

        
        """
        query_string = [('revision_id', 'revision_id_example'),
                        ('script_id', 'script_id_example'),
                        ('_date', '2013-10-20'),
                        ('change_description', 'change_description_example'),
                        ('editor', 'editor_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//revisionhistory',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_revisionhistory_patch(self):
        """Test case for revisionhistory_patch

        
        """
        body = Revisionhistory()
        query_string = [('revision_id', 'revision_id_example'),
                        ('script_id', 'script_id_example'),
                        ('_date', '2013-10-20'),
                        ('change_description', 'change_description_example'),
                        ('editor', 'editor_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//revisionhistory',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_revisionhistory_post(self):
        """Test case for revisionhistory_post

        
        """
        body = Revisionhistory()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//revisionhistory',
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
