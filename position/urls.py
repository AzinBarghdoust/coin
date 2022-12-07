from django.urls import path
from . import views

urlpatterns = [
    path('', views.Position.as_view(), name='position'),
    path('', views.CreatePosition.as_view(), name='create_position'),
]