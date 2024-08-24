
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('data', views.data),
    path('test', views.test)
]