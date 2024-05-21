# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMonitoringController(BaseTestCase):
    """MonitoringController integration test stubs"""

    def test_get_health(self):
        """Test case for get_health

        Health check
        """
        response = self.client.open(
            '/health',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_metrics(self):
        """Test case for get_metrics

        Metrics endpoint
        """
        response = self.client.open(
            '/metrics',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
