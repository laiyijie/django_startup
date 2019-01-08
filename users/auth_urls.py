from django.urls import path
from .views import AuthLogin, AuthLogout

urlpatterns = [
    path('login', AuthLogin.as_view()),
    path('logout', AuthLogout.as_view()),
]
