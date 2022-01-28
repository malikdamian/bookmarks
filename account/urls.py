from django.urls import path, include

from account.views import dashboard, register, edit, user_list, user_detail, \
    user_follow

urlpatterns = [
    path('users/follow/', user_follow, name='user_follow'),
    path('users/', user_list, name='user_list'),
    path('users/<str:username>/', user_detail, name='user_detail'),
    path('edit/', edit, name='edit'),
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
]
