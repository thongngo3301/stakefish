# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
from datetime import datetime
from unittest.mock import patch, MagicMock

from swagger_server.models.handler_validate_ip_request import HandlerValidateIPRequest  # noqa: E501
from swagger_server.models.handler_validate_ip_response import HandlerValidateIPResponse  # noqa: E501
from swagger_server.models.model_query import ModelQuery  # noqa: E501
from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
from swagger_server.test import BaseTestCase
from swagger_server.controllers.tools_controller import log_query
from swagger_server import redis_util

class TestToolsController(BaseTestCase):
    """ToolsController integration test stubs"""

    def test_lookup_domain(self):
        """Test case for lookup_domain

        Lookup domain
        """
        query_string = [('domain', 'google.com')]
        response = self.client.open(
            '/tools/lookup',
            method='GET',
            query_string=query_string)
        self.assert200(response)

    def test_validate_ip_valid(self):
        """Test case for validate_ip with valid IP address"""
        valid_ip_body = {
            "ip": "192.168.1.1"
        }
        valid_response = self.client.open(
            '/tools/validate',
            method='POST',
            data=json.dumps(valid_ip_body),
            content_type='application/json'
        )
        self.assertTrue(json.loads(valid_response.data.decode('utf-8'))['status'])

    def test_validate_ip_invalid(self):
        """Test case for validate_ip with invalid IP address"""
        invalid_ip_body = {
            "ip": "256.256.256.299"
        }
        invalid_response = self.client.open(
            '/tools/validate',
            method='POST',
            data=json.dumps(invalid_ip_body),
            content_type='application/json'
        )
        self.assertFalse(json.loads(invalid_response.data.decode('utf-8'))['status'])

if __name__ == '__main__':
    import unittest
    unittest.main()
