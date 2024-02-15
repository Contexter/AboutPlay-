# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestIntrospectionController(BaseTestCase):
    """IntrospectionController integration test stubs"""

    def test_root_get(self):
        """Test case for root_get

        OpenAPI description (this document)
        """
        response = self.client.open(
            '//',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
