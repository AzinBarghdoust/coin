from django.urls import path
from . import views

urlpatterns = [
    path('', views.PositionList.as_view(), name='position'),
    path('create/', views.CreatePosition.as_view(), name='create_position'),
]