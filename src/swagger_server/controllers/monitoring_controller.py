import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def get_health():  # noqa: E501
    """Health check

    Health check endpoint # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def get_metrics():  # noqa: E501
    """Metrics endpoint

    Prometheus metrics endpoint # noqa: E501


    :rtype: str
    """
    return 'do some magic!'
