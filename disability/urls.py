from django.urls import path
from disability import views

urlpatterns = [
    path('disabilities/', views.disabilities,name='disabilities'),
    path('disabilities/create/', views.create_disability,name='create_disability'),
    path('disabilities/delete/<int:id>', views.delete_disability,name='delete_disability'),
    path('disabilities/update/<int:id>', views.edit_disability,name='edit_disability')
]
