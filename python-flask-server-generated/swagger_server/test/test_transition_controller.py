# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.transition import Transition  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransitionController(BaseTestCase):
    """TransitionController integration test stubs"""

    def test_transition_delete(self):
        """Test case for transition_delete

        
        """
        query_string = [('transition_id', 'transition_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('transition_text', 'transition_text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//transition',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transition_get(self):
        """Test case for transition_get

        
        """
        query_string = [('transition_id', 'transition_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('transition_text', 'transition_text_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//transition',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transition_patch(self):
        """Test case for transition_patch

        
        """
        body = Transition()
        query_string = [('transition_id', 'transition_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('transition_text', 'transition_text_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//transition',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transition_post(self):
        """Test case for transition_post

        
        """
        body = Transition()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//transition',
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
