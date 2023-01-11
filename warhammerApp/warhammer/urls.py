from django.urls import path, include

from .views import welcome_warhammer_view

urlpatterns = [
    path('', welcome_warhammer_view, name='welcome-warhammer'),
    
]
