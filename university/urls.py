from django.urls import path
from university import views

urlpatterns = [
    path('universities/', views.universities,name='universities'),
    path('universities/create/', views.create_university,name='create_university'),
    path('universities/delete/<str:id>', views.delete_university,name='delete_university'),
    path('universities/update/<str:id>', views.edit_university,name='edit_university')
]