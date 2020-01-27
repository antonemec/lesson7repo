from django.urls import path

from students_app.views import (
    generate_student, students_list, students_add, students_edit, contact
)

urlpatterns = [
    path('gen/', generate_student, name='gen-s'),
    path('list/', students_list, name='list-s'),
    path('add/', students_add, name='add-s'),
    path('edit/<int:pk>/', students_edit, name='edit-s'),
    path('contact/', contact, name='contact-s'),
]
