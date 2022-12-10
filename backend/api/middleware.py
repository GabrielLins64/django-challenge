from time import time
from django.http import HttpRequest
from api.models import RequestAudit


class AuditRequest:
    """
    Middleware for audit logging API requests and responses.
    """
    def __init__(self, get_response):
        self.get_response = get_response

        self.prefixs = [
            '/api'
        ]

    def __call__(self, request: HttpRequest):
        start = time()
        response = self.get_response(request)
        exec_time = int((time() - start) * 1000)

        if not list(filter(request.get_full_path().startswith, self.prefixs)):
            return response

        request_log = RequestAudit(
            endpoint=request.get_full_path(),
            response_code=response.status_code,
            method=request.method,
            remote_address=self.get_client_ip(request),
            exec_time=exec_time,
        )

        if not request.user.is_anonymous:
            request_log.user = request.user

        request_log.save()
        return response

    def get_client_ip(self, request: HttpRequest):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            _ip = x_forwarded_for.split(',')[0]
        else:
            _ip = request.META.get('REMOTE_ADDR')

        return _ip
