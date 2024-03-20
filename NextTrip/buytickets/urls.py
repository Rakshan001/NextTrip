from django.urls import path
from . import views 
from .views import ticket_details

app_name = 'buytickets'

urlpatterns = [
    path('buy_ticket/', views.buy_ticket, name='buy_ticket'),
    path('paypalbuy_ticket/', views.paypalbuy_ticket, name='paypalbuy_ticket'),

    path('payment_success/', views.payment_success, name='payment_success'),
    # path('verify_ticket/<int:ticket_id>/', views.verify_ticket, name='verify_ticket'),
    # path('manager/', views.manager_view, name='manager_view'),
    # Other URL patterns
    path('ticket-details/', ticket_details, name='ticket_details'),
]
