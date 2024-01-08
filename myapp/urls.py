from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('other/', views.otherpage),
    path('hello/<str:username>', views.testext),
    path('hellonum/<int:id>',views.testnum),

    path('projects/', views.projects),
    path('tasks/<str:title>', views.task),
]