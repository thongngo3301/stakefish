import connexion
import six
import time
import os

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util
from flask import make_response, jsonify

def get_root():  # noqa: E501
    """Root endpoint

    Root endpoint providing version, current date, and Kubernetes status # noqa: E501

    :rtype: InlineResponse2001
    """
    # Get the current UNIX epoch time
    current_time = int(time.time())
    
    # Check if the application is running in Kubernetes
    kubernetes = os.environ.get('KUBERNETES_SERVICE_HOST') is not None
    
    # Create the response data
    response_data = InlineResponse2001(
        version="0.1.0",
        date=current_time,
        kubernetes=kubernetes
    )

    print(type(response_data.to_dict()))
    
    # Create the response with the response code 200
    response = make_response(jsonify(response_data.to_dict()), 200)
    return response
