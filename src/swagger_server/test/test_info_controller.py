# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInfoController(BaseTestCase):
    """InfoController integration test stubs"""

    def test_get_root(self):
        """Test case for get_root

        Root endpoint
        """
        response = self.client.open(
            '/',
            method='GET')
        self.assert200(response, 'Expected response code 200')

        # Parse the response data
        response_data = json.loads(response.data.decode('utf-8'))

        # Validate the response data structure
        self.assertIsInstance(response_data, dict)
        self.assertIn('version', response_data)
        self.assertIn('date', response_data)
        self.assertIn('kubernetes', response_data)

        # Validate the type of each response data field
        self.assertIsInstance(response_data['version'], str)
        self.assertIsInstance(response_data['date'], int)
        self.assertIsInstance(response_data['kubernetes'], bool)


if __name__ == '__main__':
    import unittest
    unittest.main()
