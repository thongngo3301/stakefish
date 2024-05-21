import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from flask import make_response, jsonify

from prometheus_client import generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST, REGISTRY


def get_health():  # noqa: E501
    """Health check

    Health check endpoint # noqa: E501


    :rtype: InlineResponse200
    """
    health_response = InlineResponse200(status="Service is healthy")
    response = make_response(health_response.to_dict(), 200)
    return response

def get_metrics():  # noqa: E501
    """Metrics endpoint

    Prometheus metrics endpoint # noqa: E501

    :rtype: str
    """
    registry = CollectorRegistry()
    metrics_data = generate_latest(registry)
    response = make_response(metrics_data, 200)
    response.headers['Content-Type'] = CONTENT_TYPE_LATEST
    return response
