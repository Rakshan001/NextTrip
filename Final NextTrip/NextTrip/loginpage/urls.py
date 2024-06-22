# urls.py
from django.contrib import admin
from django.urls import path, include
from . import views 

# Django admin header customization
admin.site.site_header= "NextTrip Dashboard"
admin.site.site_title = "Welcome to NextTrip Dashboard"
admin.site.index_title="Welcome to NextTrip"


urlpatterns = [
    path('signup/',views.SignupPage,name='signup'),
    path('',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
]
