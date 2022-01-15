from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, \
    PasswordChangeDoneView

from account.views import user_login, dashboard

urlpatterns = [
    # path('login/', user_login, name='login'),

    path('password_change/', PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', dashboard, name='dashboard'),
]
