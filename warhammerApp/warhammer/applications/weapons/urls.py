from django.urls import path, include

from .views import(
    weapon_list_view,
    weapon_create_view,
    weapon_melee_create_view,
    weapon_range_create_view,
    weapon_detail_view,
    weapon_edit_view,
    weapon_delete_view
)

app_name = 'warhammer-weapons'
urlpatterns = [
    path('', weapon_list_view, name='warhammer-weapons'),
    path('create/', weapon_create_view, name='warhammer-weapons-create'),
    path('createrangeweapon/', weapon_range_create_view, name='warhammer-weapons-range-create'),
    path('createmeleeweapon/', weapon_melee_create_view, name='warhammer-weapons-melee-create'),
    path('<int:id>/', weapon_detail_view, name='weapon-detail'),
    path('<int:id>/edit', weapon_edit_view, name='weapon-edit'),
    path('<int:id>/delete', weapon_delete_view, name='weapon-delete'),
]
