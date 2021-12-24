from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('modify/<int:pk>', views.modify, name='modify'),
    path('delete/<int:pk>', views.delete, name='delete'),
]