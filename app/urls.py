from django.urls import path 
from . import views 

urlpatterns = [
    path("user-lc/", views.UserLC.as_view(), name = "user-lc"),
    path("login", views.AuthUserLoginView.as_view(), name = "login-view"),
    path("test", views.Test.as_view()),
    path("login-route", views.login_route, name = "login-route")
]
