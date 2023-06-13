from django.urls import path
from student import views

urlpatterns = [
    path('students/', views.students, name = 'students'),
    path('students/delete/<int:id>', views.delete_student, name='delete_student'),
    path('students/update/<int:id>', views.edit_student, name='edit_student'),
    path('students/create/', views.create_student, name='create_student'),
]