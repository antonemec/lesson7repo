from django.urls import path

from teachers_app.views import (
    generate_teacher, teachers_list, teachers_add, teachers_edit
)

urlpatterns = [
    path('gen/', generate_teacher, name='gen-t'),
    path('list/', teachers_list, name='list-t'),
    path('add/', teachers_add, name='add-t'),
    path('edit/<int:pk>/', teachers_edit, name='edit-t'),
]
