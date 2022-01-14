from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from account.views import user_login, dashboard

app_name = 'account'

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard')
]
