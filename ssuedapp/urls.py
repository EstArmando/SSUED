from django.urls import path
from ssuedapp import views

urlpatterns = [
    path('', views.index, name = 'home'),
]
