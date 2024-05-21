import connexion
import six
import socket
import json

from flask import request, make_response, jsonify
from datetime import datetime
from swagger_server.models.handler_validate_ip_request import HandlerValidateIPRequest  # noqa: E501
from swagger_server.models.handler_validate_ip_response import HandlerValidateIPResponse  # noqa: E501
from swagger_server.models.model_query import ModelAddress  # noqa: E501
from swagger_server.models.model_query import ModelQuery  # noqa: E501
from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
from swagger_server import util

from swagger_server.redis_util import redis_client


def lookup_domain(domain):  # noqa: E501
    """Lookup domain

    Lookup domain and return all IPv4 addresses # noqa: E501

    :param domain: Domain name
    :type domain: str

    :rtype: ModelQuery
    """
    if not domain:
        error = UtilsHTTPError(message="Domain parameter is required")
        response_obj = make_response(jsonify(error.to_dict()), 400)
        return response_obj

    try:
        # Perform DNS lookup to get IPv4 addresses
        ipv4_addresses = socket.gethostbyname_ex(str(domain))[2]
        ipv4_addresses = [ip for ip in ipv4_addresses if '.' in ip]

        if not ipv4_addresses:
            error = UtilsHTTPError(message="No IPv4 addresses found")
            response_obj = make_response(jsonify(error.to_dict()), 404)
            return response_obj

        # Create ModelAddress instances for each IP
        addresses = [ModelAddress(ip=ip) for ip in ipv4_addresses]

        # Create the ModelQuery instance
        query = ModelQuery(
            addresses=addresses,
            client_ip=request.remote_addr,
            created_at=int(datetime.now().timestamp()),
            domain=domain
        )

        # Log the query
        log_query(query)

        response_obj = make_response(jsonify(query.to_dict()), 200)
        return response_obj

    except socket.gaierror:
        error = UtilsHTTPError(message="Domain not found")
        response_obj = make_response(jsonify(error.to_dict()), 404)
        return response_obj

    except Exception as e:
        error = UtilsHTTPError(message=str(e))
        response_obj = make_response(jsonify(error.to_dict()), 500)
        return response_obj

def log_query(query):
    """
    Log successful queries and their results in Redis.

    :param query: The successful query to be stored.
    """

    # Convert log query to JSON string
    log_entry = {
        'domain': query.domain,
        'addresses': ', '.join([x.ip for x in query.addresses]),
        'created_at': query.created_at
    }
    log_entry_json = json.dumps(log_entry)

    # Push the log entry to a Redis list
    redis_client.lpush('query_logs', log_entry_json)

def validate_ip(body):  # noqa: E501
    """Simple IP validation

    Simple IP validation # noqa: E501

    :param body: IP to validate
    :type body: dict | bytes

    :rtype: HandlerValidateIPResponse
    """
    if not connexion.request.is_json:
        error = UtilsHTTPError(message="Invalid content type, must be application/json")
        response_obj = make_response(jsonify(error.to_dict()), 400)
        response_obj.headers['Content-Type'] = 'application/json'
        return response_obj

    body = HandlerValidateIPRequest.from_dict(connexion.request.get_json())  # noqa: E501

    if not body.ip:
        error = UtilsHTTPError(message="IP parameter is required")
        response_obj = make_response(jsonify(error.to_dict()), 400)
        response_obj.headers['Content-Type'] = 'application/json'
        return response_obj

    is_valid = util.is_valid_ipv4(body.ip)
    response = HandlerValidateIPResponse(status=is_valid)

    response_obj = make_response(jsonify(response.to_dict()), 200)
    response_obj.headers['Content-Type'] = 'application/json'
    return response_obj
