"""warhammerApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import welcome_view
import user_authentication.views


urlpatterns = [
    path('', welcome_view),
    path('welcome/', welcome_view),
    path('admin/', admin.site.urls),
    #path('auth/', include('user_authentication.urls')),
    path('register/', user_authentication.views.register_view),
    path('login/', user_authentication.views.login_view),
    path('logout/', user_authentication.views.logout_view),

    path('warhammer/', include('warhammer.urls')),

    #path('warhammer/', include('warhammer.urls')),
]
