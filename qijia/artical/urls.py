from django.urls import path
from artical import views

urlpatterns = [
    path('', views.artical_display, name='index'),
]