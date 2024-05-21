import json
from datetime import datetime
from typing import List
from flask import make_response, jsonify

from swagger_server.models.model_query import ModelAddress  # noqa: E501
from swagger_server.models.model_query import ModelQuery  # noqa: E501
from swagger_server.models.utils_http_error import UtilsHTTPError  # noqa: E501
from swagger_server import util

from swagger_server.redis_util import redis_client

def queries_history():  # noqa: E501
    """List queries

    List queries # noqa: E501

    :rtype: List[ModelQuery]
    """
    # Retrieve the latest 20 saved queries from Redis
    query_logs = redis_client.lrange('query_logs', 0, 19)

    # Initialize list to store ModelQuery objects
    model_queries = []

    # Iterate over retrieved logs and create ModelQuery objects
    for log in query_logs:
        log_entry = json.loads(log)
        model_queries.append(log_entry)

    # Reverse the list to display the most recent queries first
    response_obj = make_response(jsonify(model_queries), 200)
    return response_obj
