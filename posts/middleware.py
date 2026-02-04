import time 
import logging

logger = logging.getLogger('django.request')

class RequestInfoLogger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        logger.info(f"Incoming Request: {request.scheme} {request.method} {request.path}")

        response = self.get_response(request)

        duration = time.time() - start_time

        logger.info(
            f"TimeTaken: {duration:.4f}"
            f"Status: {response.status_code} "
        )

        return response 
