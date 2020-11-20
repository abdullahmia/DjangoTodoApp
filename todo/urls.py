from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('single/<int:id>', views.single_view, name='single'),
    path('delete/<int:id>', views.delete_todo, name='delete')
]