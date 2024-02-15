# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.musicsound import Musicsound  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMusicsoundController(BaseTestCase):
    """MusicsoundController integration test stubs"""

    def test_musicsound_delete(self):
        """Test case for musicsound_delete

        
        """
        query_string = [('music_sound_id', 'music_sound_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('cue', 'cue_example'),
                        ('description', 'description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//musicsound',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_musicsound_get(self):
        """Test case for musicsound_get

        
        """
        query_string = [('music_sound_id', 'music_sound_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('cue', 'cue_example'),
                        ('description', 'description_example'),
                        ('select', 'select_example'),
                        ('order', 'order_example'),
                        ('offset', 'offset_example'),
                        ('limit', 'limit_example')]
        headers = [('range', 'range_example'),
                   ('range_unit', 'items'),
                   ('prefer', 'prefer_example')]
        response = self.client.open(
            '//musicsound',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_musicsound_patch(self):
        """Test case for musicsound_patch

        
        """
        body = Musicsound()
        query_string = [('music_sound_id', 'music_sound_id_example'),
                        ('scene_id', 'scene_id_example'),
                        ('cue', 'cue_example'),
                        ('description', 'description_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//musicsound',
            method='PATCH',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_musicsound_post(self):
        """Test case for musicsound_post

        
        """
        body = Musicsound()
        query_string = [('select', 'select_example')]
        headers = [('prefer', 'prefer_example')]
        response = self.client.open(
            '//musicsound',
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
