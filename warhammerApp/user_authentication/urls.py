from django.urls import path

from .views import(
    register_view,
    login_view,
    logout_view,
)

app_name = 'user_authentication'
urlpatterns = [
    path('register/', register_view, name='user_authentication-register'),
    path('login/', login_view, name='user_authentication-login'),
    path('logout/', logout_view, name='user_authentication-logout'),
]
