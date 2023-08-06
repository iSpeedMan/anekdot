from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnekdotListView, name='AnekdotListView'),
]
