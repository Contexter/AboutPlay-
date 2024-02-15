# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.casting import Casting  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCastingController(BaseTestCase):
    """CastingController integration test stubs"""

    def test_casting_delete(self):
        """Test case for casting_delete

        
        """
        query_string = [('casting_id', 'casting_id_example'),
                        ('character_id', 'character_id_example'),
                        ('actor_characteristics_choices', 'actor_characteristics_choices_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//casting',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_casting_get(self):
        """Test case for casting_get

        
        """
        query_string = [('casting_id', 'casting_id_example'),
                        ('character_id', 'character_id_example'),
                        ('actor_characteristics_choices', 'actor_characteristics_choices_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//casting',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_casting_patch(self):
        """Test case for casting_patch

        
        """
        body = Casting()
        query_string = [('casting_id', 'casting_id_example'),
                        ('character_id', 'character_id_example'),
                        ('actor_characteristics_choices', 'actor_characteristics_choices_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//casting',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_casting_post(self):
        """Test case for casting_post

        
        """
        body = Casting()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//casting',
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
