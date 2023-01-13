from django.urls import path, include

from .views import welcome_warhammer_view

app_name = 'warhammer'
urlpatterns = [
    path('', welcome_warhammer_view, name='warhammer-welcome'),
    path('weapons/', include('warhammer.applications.weapons.urls')),
    path('characters/', include('warhammer.applications.creatures.characters.urls')),
]
