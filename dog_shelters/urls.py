from django.urls import path 
from . import views 

urlpatterns = [
    path('shelter_list/', views.shelter_list, name='shelter_list'),
    path('shelter<int:pk>/', views.shelter_details, name="shelter_details"),
]
