from django.urls import path

# from .views import Section2
from index import views

urlpatterns = [
    # path('', Section2.as_view(), name='home'),
    path('', views.home, name='home')
]
