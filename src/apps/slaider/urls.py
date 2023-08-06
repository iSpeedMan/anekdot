from django.urls import path
from . import views

app_name = 'slaider'

urlpatterns = [
    path('', views.MemsListView, name='memslistview'),
]
