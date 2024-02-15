# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.metadata import Metadata  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMetadataController(BaseTestCase):
    """MetadataController integration test stubs"""

    def test_metadata_delete(self):
        """Test case for metadata_delete

        
        """
        query_string = [('metadata_id', 'metadata_id_example'),
                        ('creation_date', '2013-10-20'),
                        ('last_modified_date', '2013-10-20'),
                        ('version_number', 'version_number_example'),
                        ('additional_information', 'additional_information_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//metadata',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_metadata_get(self):
        """Test case for metadata_get

        
        """
        query_string = [('metadata_id', 'metadata_id_example'),
                        ('creation_date', '2013-10-20'),
                        ('last_modified_date', '2013-10-20'),
                        ('version_number', 'version_number_example'),
                        ('additional_information', 'additional_information_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//metadata',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_metadata_patch(self):
        """Test case for metadata_patch

        
        """
        body = Metadata()
        query_string = [('metadata_id', 'metadata_id_example'),
                        ('creation_date', '2013-10-20'),
                        ('last_modified_date', '2013-10-20'),
                        ('version_number', 'version_number_example'),
                        ('additional_information', 'additional_information_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//metadata',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_metadata_post(self):
        """Test case for metadata_post

        
        """
        body = Metadata()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//metadata',
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
