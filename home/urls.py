from django.urls import path

from . import views

urlpatterns = [
    path('urlcutter/', views.home, name='home'),
    path('urldispatcher/<str:slug>/', views.urlDispatcher, name='urlDispatcher'),
    path('urlcutter/export_file/', views.urlExporter, name='exportFile'),
]