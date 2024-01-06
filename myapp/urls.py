from django.urls import path
from . import views

urlpatterns = [
    path('', views.testext),
    path('other/', views.otherpage)
]