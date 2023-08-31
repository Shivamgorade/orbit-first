from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Define any other URL patterns specific to your app here
]
