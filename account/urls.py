from django.urls import path, include

from account.views import user_login, dashboard

urlpatterns = [
    # path('login/', user_login, name='login'),

    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
]
