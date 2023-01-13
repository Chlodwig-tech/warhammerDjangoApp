from django.urls import path

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
    path('createrangeweapon/', weapon_range_create_view, name='warhammer-weapons-createrange'),
    path('createmeleeweapon/', weapon_melee_create_view, name='warhammer-weapons-createmelee'),
    path('<int:id>/', weapon_detail_view, name='warhammer-weapons-detail'),
    path('<int:id>/edit', weapon_edit_view, name='warhammer-weapons-edit'),
    path('<int:id>/delete', weapon_delete_view, name='warhammer-weapons-delete'),
]
