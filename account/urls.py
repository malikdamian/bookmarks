from django.urls import path, include

from account.views import dashboard, register, edit

urlpatterns = [
    path('edit/', edit, name='edit'),
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
]
