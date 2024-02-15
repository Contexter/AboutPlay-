# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.characterrelationship import Characterrelationship  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCharacterrelationshipController(BaseTestCase):
    """CharacterrelationshipController integration test stubs"""

    def test_characterrelationship_delete(self):
        """Test case for characterrelationship_delete

        
        """
        query_string = [('relationship_id', 'relationship_id_example'),
                        ('character1_id', 'character1_id_example'),
                        ('character2_id', 'character2_id_example'),
                        ('relationship_type', 'relationship_type_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//characterrelationship',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characterrelationship_get(self):
        """Test case for characterrelationship_get

        
        """
        query_string = [('relationship_id', 'relationship_id_example'),
                        ('character1_id', 'character1_id_example'),
                        ('character2_id', 'character2_id_example'),
                        ('relationship_type', 'relationship_type_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//characterrelationship',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characterrelationship_patch(self):
        """Test case for characterrelationship_patch

        
        """
        body = Characterrelationship()
        query_string = [('relationship_id', 'relationship_id_example'),
                        ('character1_id', 'character1_id_example'),
                        ('character2_id', 'character2_id_example'),
                        ('relationship_type', 'relationship_type_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//characterrelationship',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_characterrelationship_post(self):
        """Test case for characterrelationship_post

        
        """
        body = Characterrelationship()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//characterrelationship',
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
