from django.urls import path, include

from .views import(
    character_list_view,
    character_create_view,
    character_detail_view,
    character_edit_view,
    character_delete_view,
)

app_name = 'warhammer-characters'
urlpatterns = [
    path('', character_list_view, name='warhammer-characters'),
    path('create/', character_create_view, name='warhammer-characters-create'),
    path('<int:id>/', character_detail_view, name='warhammer-characters-detail'),
    path('<int:id>/edit', character_edit_view, name='warhammer-characters-edit'),
    path('<int:id>/delete', character_delete_view, name='warhammer-characters-delete'),
]
