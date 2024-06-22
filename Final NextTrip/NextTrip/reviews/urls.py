from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('review/', views.review_form, name='review_form'),
    path('all/', views.all_reviews, name='all_reviews'),
    path('bus/<str:bus_name>/', views.bus_reviews, name='bus_reviews'),

    path('submit_query/', views.submit_query, name='submit_query'),
    
    # URL pattern for submitting the query form data
    # path('submit_query/', views.submit_query, name='submit_query'),
]
