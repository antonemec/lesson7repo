from django.urls import path

from groups_app.views import (
    generate_group, groups_list, groups_add,  groups_edit
)

urlpatterns = [
    path('groups/gen/', generate_group, name='gen-group'),
    path('groups/list/', groups_list, name='list-groups'),
    path('groups/add/', groups_add, name='add-group'),
    path('groups/edit/<int:pk>/', groups_edit, name='edit-group'),
]
