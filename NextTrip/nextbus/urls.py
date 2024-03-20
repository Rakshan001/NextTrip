from django.urls import path
from nextbus import views

urlpatterns = [
    path('search/', views.search_buses, name='search_buses'),
    path('bus/<str:bus_name>/', views.bus_reviews, name='bus_reviews'),
    
    #  path('get_stations/', views.get_stations, name='get_stations'),


    # path('get_station_suggestions/', views.get_station_suggestions, name='get_station_suggestions'),

    


]
