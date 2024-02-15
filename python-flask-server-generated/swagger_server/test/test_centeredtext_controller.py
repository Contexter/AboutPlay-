# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.centeredtext import Centeredtext  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCenteredtextController(BaseTestCase):
    """CenteredtextController integration test stubs"""

    def test_centeredtext_delete(self):
        """Test case for centeredtext_delete

        
        """
        query_string = [('centered_id', 'centered_id_example'),
                        ('script_id', 'script_id_example'),
                        ('text', 'text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//centeredtext',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_centeredtext_get(self):
        """Test case for centeredtext_get

        
        """
        query_string = [('centered_id', 'centered_id_example'),
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
            '//centeredtext',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_centeredtext_patch(self):
        """Test case for centeredtext_patch

        
        """
        body = Centeredtext()
        query_string = [('centered_id', 'centered_id_example'),
                        ('script_id', 'script_id_example'),
                        ('text', 'text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//centeredtext',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_centeredtext_post(self):
        """Test case for centeredtext_post

        
        """
        body = Centeredtext()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//centeredtext',
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
