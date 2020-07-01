#Lets import the libraries, first the django libraires and also the views.py file thtat we created where we have our models

from django.urls import path
from . import views

#If someone goes to the main home it will call the method home of the file view
urlpatterns = [
    path('', views.home, name = 'home'),
    path('new_search', views.new_search, name = 'new_search'),
]


