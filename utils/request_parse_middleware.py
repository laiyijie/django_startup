# -*- coding: utf-8 -*-

import logging
import json
import copy
from django.conf import settings

logger = logging.getLogger("access")


class RequestBodyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.data = {}
        if request.body is not None:
            try:
                request.data = json.loads(request.body.decode("utf-8"))
            except json.decoder.JSONDecodeError as e:
                pass
        request.data.update(request.GET.dict())
        request.data.update(request.POST.dict())
        path_info = request.path_info
        if "password" in request.data:
            tmp_data = copy.deepcopy(request.data)
            tmp_data["password"] = "***"
            param_json_str = json.dumps(tmp_data)
        else:
            param_json_str = json.dumps(request.data)
        response = self.get_response(request)

        logger.info('request_path: {}, request_param:{}, user_id: {}, response_code: {}, ip_address: {}'.format(path_info, param_json_str, request.session.get('userid', 0), response.status_code, self.get_client_ip(request)))

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
