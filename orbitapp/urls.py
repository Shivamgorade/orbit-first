from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
     path('find-job/', views.find_job, name='find_job'),
    
    # Define any other URL patterns specific to your app here
]
