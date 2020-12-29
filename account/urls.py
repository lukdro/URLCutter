from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='auth_login'),
    path('logout/', views.logout_view, name='auth_logout'),    
]