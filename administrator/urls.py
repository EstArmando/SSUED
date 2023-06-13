from django.urls import path
from administrator import views

urlpatterns = [
    path('signin/', views.signin, name = 'signin'),
    path('logout/', views.signout, name = 'logout'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('admins/', views.administrators, name = 'admins'),
    path('admins/delete/<int:id>', views.delete_admin, name = 'delete_admin'),
    path('admins/update/<int:id>', views.edit_admin, name = 'edit_admin'),
    path('admins/create/', views.create_admin, name = 'create_admin'),
    path('admins/changepass/', views.change_pass, name = 'change_pass')
]