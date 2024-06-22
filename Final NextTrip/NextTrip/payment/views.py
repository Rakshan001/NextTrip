
import paypalrestsdk
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse




from django.shortcuts import render, redirect
from buytickets .forms import TicketForm
from buytickets .models import Ticket
from django.contrib.auth.decorators import login_required
from nextbus.models import Station,Bus
import uuid

# paypalrestsdk.configure({
#     "mode": "sandbox",  # Change to "live" for production
#     "client_id": settings.PAYPAL_CLIENT_ID,
#     "client_secret": settings.PAYPAL_SECRET,
# })

# def create_payment(request):
#     payment = paypalrestsdk.Payment({
#         "intent": "sale",
#         "payer": {
#             "payment_method": "paypal",
#         },
#         "redirect_urls": {
#             "return_url": request.build_absolute_uri(reverse('execute_payment')),
#             "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
#         },
#         "transactions": [
#             {
#                 "amount": {
                    
#                     "total": "1.00",  # Total amount in USD
#                     "currency": "USD",
#                 },
#                 "description": "Payment for Product/Service",
#             }
#         ],
#     })

#     if payment.create():
#         return redirect(payment.links[1].href)  # Redirect to PayPal for payment
#     else:
#         return render(request, 'payment/payment_failed.html')
    






import paypalrestsdk
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings

paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_SECRET,
})

def create_payment(request):
    if request.method == 'POST':
        # Retrieve the cost value from the form submission
        cost = request.POST.get('cost')
        
        # Create a PayPal payment object with the cost value
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal",
            },
            "redirect_urls": {
                "return_url": request.build_absolute_uri(reverse('execute_payment')),
                "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
            },
            "transactions": [
                {
                    "amount": {
                        "total": cost,  # Use the value from the form submission as the total amount
                        "currency": "USD",
                    },
                    "description": "Payment for Product/Service",
                }
            ],
        })

        # Create the PayPal payment
        if payment.create():
            return redirect(payment.links[1].href)  # Redirect to PayPal for payment
        else:
            return render(request, 'payment/payment_failed.html')
    else:
        # Handle cases where the request method is not POST
        pass








def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        latest_ticket = Ticket.objects.filter(user=request.user).latest('id')

        return render(request, 'buytickets/payment_success.html', {'latest_ticket': latest_ticket})

    else:
        return render(request, 'payment/payment_failed.html')

def payment_checkout(request):
    return render(request, 'payment/checkout.html')

# views.py

from django.shortcuts import render

def payment_failed(request):
    return render(request, 'payment/payment_failed.html')
