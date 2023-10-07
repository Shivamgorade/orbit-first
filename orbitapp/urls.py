from django.urls import path
from . import views

urlpatterns = [

     path('search/', views.search_seniors, name='search_seniors'),

    path('', views.home, name='home'),
    
     path('find-job/', views.find_job, name='find_job'),

     path('find-talent/',views.find_talent, name='find-talent'),

    path('register/', views.register_senior, name='register_senior'),

    path('show-seniors/', views.show_senior, name='show_senior'),
    # Define any other URL patterns specific to your app here
]
