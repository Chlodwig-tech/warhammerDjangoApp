from django.urls import path, include

from .views import welcome_warhammer_view

app_name = 'warhammer'
urlpatterns = [
    path('', welcome_warhammer_view, name='welcome-warhammer'),
    path('weapons/', include('warhammer.applications.weapons.urls'))
]
