"""
Logger for API calls
"""

import logging
from requests import Response
from json import JSONDecodeError

log = logging.getLogger(__name__)


class LogHandler:

    @staticmethod
    def logger(func):
        def log_wrapper(*args, **kwargs):
            response: Response = func(*args, **kwargs)
            log.info(f"{'*'*80}")
            log.info(f"Request URL: {response.request.url}")
            log.info(f"Request Method: {response.request.method}")
            log.info(f"Status Code: {response.status_code}")
            log.info(f"Request Body: {response.request.body}")
            log.info(f"Response Headers: {response.headers}")
            try:
                log.info(f"Response JSON: {response.json()}")
            except JSONDecodeError:
                log.info(f"Skipping response JSON")
            log.info(f"{'*'*80}")
            return response
        return log_wrapper
