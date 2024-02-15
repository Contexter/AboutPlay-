# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.formattingrules import Formattingrules  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFormattingrulesController(BaseTestCase):
    """FormattingrulesController integration test stubs"""

    def test_formattingrules_delete(self):
        """Test case for formattingrules_delete

        
        """
        query_string = [('rule_id', 'rule_id_example'),
                        ('script_id', 'script_id_example'),
                        ('rule_description', 'rule_description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//formattingrules',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_formattingrules_get(self):
        """Test case for formattingrules_get

        
        """
        query_string = [('rule_id', 'rule_id_example'),
                        ('script_id', 'script_id_example'),
                        ('rule_description', 'rule_description_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//formattingrules',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_formattingrules_patch(self):
        """Test case for formattingrules_patch

        
        """
        body = Formattingrules()
        query_string = [('rule_id', 'rule_id_example'),
                        ('script_id', 'script_id_example'),
                        ('rule_description', 'rule_description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//formattingrules',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_formattingrules_post(self):
        """Test case for formattingrules_post

        
        """
        body = Formattingrules()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//formattingrules',
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
