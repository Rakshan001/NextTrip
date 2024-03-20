# from django.shortcuts import render, redirect
# from .forms import TicketForm
# from .models import Ticket
# from django.contrib.auth.decorators import login_required
# from nextbus.models import Station
# import uuid

# @login_required
# def buy_ticket(request):
#     origin_stations = Station.objects.all()
#     destination_stations = Station.objects.all()

#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             ticket = form.save(commit=False)
#             ticket.user = request.user
#             ticket.ticket_number = uuid.uuid4().hex[:10]
#             ticket.save()
#             return redirect('buytickets:payment_success')

#     else:
#         form = TicketForm()
#     return render(request, 'buytickets/buy_ticket.html', {'form': form, 'user_name': request.user.username,
#                                                           'origin_stations': origin_stations,
#                                                           'destination_stations': destination_stations})

# def payment_success(request):
#     # return render(request, 'buytickets/payment_success.html')
#     latest_ticket = Ticket.objects.filter(user=request.user).latest('id')

#     return render(request, 'buytickets/payment_success.html', {'latest_ticket': latest_ticket})




# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import Ticket

# @login_required
# def ticket_details(request):
#     user_tickets = Ticket.objects.filter(user=request.user)
#     return render(request, 'buytickets/ticket_details.html', {'user_tickets': user_tickets})


















#Final working views


from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket
from django.contrib.auth.decorators import login_required
from nextbus.models import Station,Bus
import uuid

@login_required
def buy_ticket(request):
    origin_stations = Station.objects.all()
    destination_stations = Station.objects.all()
    available_buses = Bus.objects.all() 

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.ticket_number = uuid.uuid4().hex[:10]
            ticket.save()
            return redirect('buytickets:payment_success')

    else:
        form = TicketForm()
    return render(request, 'buytickets/buy_ticket.html', {'form': form, 'user_name': request.user.username,
                                                          'origin_stations': origin_stations,
                                                          'destination_stations': destination_stations,
                                                          'available_buses': available_buses})



# Pay with paypal

@login_required
def paypalbuy_ticket(request):
    origin_stations = Station.objects.all()
    destination_stations = Station.objects.all()
    available_buses = Bus.objects.all() 

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.ticket_number = uuid.uuid4().hex[:10]
            ticket.save()
            return redirect('buytickets:payment_success')

    else:
        form = TicketForm()
    return render(request, 'buytickets/paypalbuy_ticket.html', {'form': form, 'user_name': request.user.username,
                                                          'origin_stations': origin_stations,
                                                          'destination_stations': destination_stations,
                                                          'available_buses': available_buses})





def payment_success(request):
    # return render(request, 'buytickets/payment_success.html')
    latest_ticket = Ticket.objects.filter(user=request.user).latest('id')

    return render(request, 'buytickets/payment_success.html', {'latest_ticket': latest_ticket})







from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket

@login_required
def ticket_details(request):
    user_tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'buytickets/ticket_details.html', {'user_tickets': user_tickets})

