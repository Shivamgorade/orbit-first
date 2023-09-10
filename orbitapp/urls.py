from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
     path('find-job/', views.find_job, name='find_job'),

     path('find-talent/',views.find_talent, name='find-talent'),

     path('find-senior/',views.find_senior, name='find-senior'),
    
    # Define any other URL patterns specific to your app here
]
