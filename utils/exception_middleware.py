import logging
import traceback
from django.http import JsonResponse

logger = logging.getLogger("middle_ware")


class ExceptionReportMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if hasattr(exception, "response"):
            return exception.response
        if isinstance(exception, JsonResponse):
            return exception
        stack_info = traceback.format_exc()
        error_info = "Exception is thrown for request: {0}. Stacktrace: {1}, Exception: {1}".format(request.path, stack_info, exception)
        logger.error(error_info)
        return JsonResponse({"msg": error_info}, status=417)
