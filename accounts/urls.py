import django
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from chat import views as chatViews

#from django.contrib.auth.views import LogoutThenLoginView

urlpatterns = [
    path('', chatViews.getChats, name="dashboard"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('register/', views.register, name='register'),
    #path('logout/', LogoutThenLoginView.as_view(), name="logout_then_login"),

    #path('logout-then-login/', django.contrib.auth.views.logout_then_login, name="logout_then_login"),

]