from .models import User
from django.views import View
from django.http import JsonResponse
from utils.user_exceptions import UserWarningException


class AuthLogin(View):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise UserWarningException(error_msg="用户不存在或密码错误")
        else:
            if user.password != password:
                raise UserWarningException(error_msg="用户不存在或密码错误")
            else:
                request.session['userid'] = user.id
                request.session.save()
                return JsonResponse(user.get_dict())


class AuthLogout(View):
    def post(self, request):
        request.session.clear()
        return JsonResponse({})


class UserInfo(View):
    def get(self, request):
        user_id = request.userid
        return JsonResponse(User.objects.get(id=user_id).get_dict())
