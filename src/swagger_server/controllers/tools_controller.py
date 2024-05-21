import connexion
import six

from swagger_server.models.handler_validate_ip_request import HandlerValidateIPRequest  # noqa: E501
from swagger_server.models.handler_validate_ip_response import HandlerValidateIPResponse  # noqa: E501
from swagger_server.models.model_query import ModelQuery  # noqa: E501
from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
from swagger_server import util


def lookup_domain(domain):  # noqa: E501
    """Lookup domain

    Lookup domain and return all IPv4 addresses # noqa: E501

    :param domain: Domain name
    :type domain: str

    :rtype: ModelQuery
    """
    return 'do some magic!'


def validate_ip(body):  # noqa: E501
    """Simple IP validation

    Simple IP valication # noqa: E501

    :param body: IP to validate
    :type body: dict | bytes

    :rtype: HandlerValidateIPResponse
    """
    if connexion.request.is_json:
        body = HandlerValidateIPRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
