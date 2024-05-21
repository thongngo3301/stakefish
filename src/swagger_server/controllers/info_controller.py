import connexion
import six

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util


def get_root():  # noqa: E501
    """Root endpoint

    Root endpoint providing version, current date, and Kubernetes status # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'
