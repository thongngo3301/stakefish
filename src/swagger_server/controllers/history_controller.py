import connexion
import six

from swagger_server.models.model_query import ModelQuery  # noqa: E501
from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
from swagger_server import util


def queries_history():  # noqa: E501
    """List queries

    List queries # noqa: E501


    :rtype: List[ModelQuery]
    """
    return 'do some magic!'
