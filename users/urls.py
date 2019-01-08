from django.urls import path
from .views import UserInfo

urlpatterns = [
    path('basic/info', UserInfo.as_view()),
]
