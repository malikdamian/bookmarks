from django.urls import path, include

from account.views import user_login, dashboard, register

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
]
