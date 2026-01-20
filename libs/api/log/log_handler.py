"""
Logger for API calls
"""
import logging
from requests import HTTPError, Response

log = logging.getLogger(__name__)


class LogHandler:

    @staticmethod
    def logger(func):
        def log_wrapper(*args, **kwargs):
            try: 
                response: Response = func(*args, **kwargs)
                log.info(f"{'*'*80}")
                log.info(f"Request URL: {response.request.url}")
                log.info(f"Request Method: {response.request.method}")
                log.info(f"Request Body: {response.request.body}")
                log.info(f"Response Headers: {response.headers}")
                log.info(f"Response JSON: {response.json()}")
                log.info(f"{'*'*80}")
                return response
            except HTTPError as he:
                log.error(f"HTTPError occured: {he}")
        return log_wrapper
      
