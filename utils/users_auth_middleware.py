from django.http import HttpResponse, JsonResponse
import re
import logging

logger = logging.getLogger(__name__)


class UsersAuthMiddleWare(object):
    module_pattern = re.compile('/api/v1/(\w+)/.*')

    no_need_privilege_modules = {'general', 'one_search', 'payment'}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        m = self.module_pattern.match(request.path_info)
        if m is None:
            return self.get_response(request)

        module_prefix = m.group(1)

        # here is the auth
        if module_prefix == 'auth':
            return self.get_response(request)

        session = request.session
        if session.get("userid") is None:
            return HttpResponse("not login", status=401)

        request.userid = int(session.get("userid"))

        return self.get_response(request)
