from django.http import JsonResponse
from django.shortcuts import render
from .models import Station, Route, Trip
from django.http import JsonResponse

# def search_buses(request):
#     if request.method == 'POST':
#         origin = request.POST.get('origin')
#         destination = request.POST.get('destination')
#         try:
#             origin_station = Station.objects.get(name=origin)
#             destination_station = Station.objects.get(name=destination)
#             trips = Trip.objects.filter(
#                 route__start_station=origin_station,
#                 route__end_station=destination_station,
#                 available_seats__gt=0
#             ).order_by('departure_time')
#             context = {'trips': trips}
#             return render(request, 'nextbus/search_results.html', context)
#         except Station.DoesNotExist:
#             # Handle invalid stations
#             return render(request, 'nextbus/search_form.html', {'error': 'Invalid stations'})
#     else:
#         return render(request, 'nextbus/search_form.html')







# def get_station_suggestions(request):
#     if request.method == "GET":
#         query = request.GET.get("query")
#         if query:
#             suggestions = Station.objects.filter(name__istartswith=query)[:5]  # Adjust limit as needed
#             return JsonResponse([station.name for station in suggestions], safe=False)
#     return JsonResponse([], safe=False)





# **************************************************

# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404
# from .models import Station, Route, Stop, Trip

# def search_buses(request):
#     if request.method == 'POST':
#         origin = request.POST.get('origin')
#         destination = request.POST.get('destination')
#         try:
#             origin_station = Station.objects.get(name=origin)
#             destination_station = Station.objects.get(name=destination)

#             # Filter routes based on origin and destination stations
#             routes = Route.objects.filter(
#                 start_station=origin_station,
#                 end_station=destination_station
#             )

#             # Include stops for each route in the results
#             trips = []
#             for route in routes:
#                 stops = Stop.objects.filter(route=route).order_by('order')
#                 trip = {
#                     'route': route,
#                     'stops': stops,
#                     'trips': Trip.objects.filter(route=route, available_seats__gt=0).order_by('departure_time')
#                 }
#                 trips.append(trip)

#             context = {'trips': trips}
#             return render(request, 'nextbus/search_results.html', context)
#         except Station.DoesNotExist:
#             # Handle invalid stations
#             return render(request, 'nextbus/search_form.html', {'error': 'Invalid stations'})
#     else:
#         return render(request, 'nextbus/search_form.html')


# ###########################

# from django.shortcuts import render
# from .models import Route, Stop

# def route_stops(request, route_id):
#     route = Route.objects.get(id=route_id)
#     stops = Stop.objects.filter(route=route).order_by('order')  # Assuming 'order' field specifies the sequence of stops
#     return render(request, 'nextbus/route_stops.html', {'route': route, 'stops': stops})













# Final working views
from django.db.models import Avg
from django.shortcuts import render
from .models import Station, Route, Stop, Trip
from reviews.models import Review

# def search_buses(request):
#     if request.method == 'POST':
#         origin = request.POST.get('origin')
#         destination = request.POST.get('destination')
#         try:
#             origin_station = Station.objects.get(name=origin)
#             destination_station = Station.objects.get(name=destination)

#             # Filter routes based on origin and destination stations
#             routes = Route.objects.filter(
#                 start_station=origin_station,
#                 end_station=destination_station
#             )

#             # Include stops for each route in the results
#             trips = []
#             for route in routes:
#                 stops = Stop.objects.filter(route=route).order_by('order')
#                 trip = {
#                     'route': route,
#                     'stops': stops,
#                     'trips': Trip.objects.filter(route=route, available_seats__gt=0).order_by('departure_time')
#                 }
                
#                 # Calculate average rating for the bus
#                 bus_reviews = Review.objects.filter(bus=route.bus)
#                 avg_rating = bus_reviews.aggregate(Avg('rating'))['rating__avg']
                
#                 # Handle the case where there are no reviews for a bus
#                 trip['avg_rating'] = round(avg_rating, 1) if avg_rating is not None else None
                
#                 trips.append(trip)

#             context = {'trips': trips}
#             return render(request, 'nextbus/search_results.html', context)
#         except Station.DoesNotExist:
#             # Handle invalid stations
#             return render(request, 'nextbus/search_form.html', {'error': 'Invalid stations'})
#     else:
#         return render(request, 'nextbus/search_form.html')


###########################

from django.shortcuts import render
from .models import Route, Stop

def route_stops(request, route_id):
    route = Route.objects.get(id=route_id)
    stops = Stop.objects.filter(route=route).order_by('order')  # Assuming 'order' field specifies the sequence of stops
    return render(request, 'nextbus/route_stops.html', {'route': route, 'stops': stops})


from django.shortcuts import render
from reviews.models import Review

def bus_reviews(request, bus_name):
    # Fetch reviews for the specified bus
    bus_reviews = Review.objects.filter(bus__name=bus_name)
    context = {'bus_reviews': bus_reviews, 'bus_name': bus_name}
    return render(request, 'reviews/bus_reviews.html', context)



# $=######################################
from django.shortcuts import render
from .models import Station, Route, Stop, Trip
from django.db.models import Avg

def search_buses(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        try:
            origin_station = Station.objects.get(name=origin)
            destination_station = Station.objects.get(name=destination)

            # Filter routes based on origin and destination stations
            routes = Route.objects.filter(
                start_station=origin_station,
                end_station=destination_station
            )

            # Include trips for each route in the results
            trips = []
            for route in routes:
                stops = Stop.objects.filter(route=route).order_by('order')
                route_trips = Trip.objects.filter(route=route, available_seats__gt=0).order_by('departure_time')
                for trip in route_trips:
                    # Calculate average rating for the bus
                    bus_reviews = Review.objects.filter(bus=route.bus)
                    avg_rating = bus_reviews.aggregate(Avg('rating'))['rating__avg']
                    
                    # Handle the case where there are no reviews for a bus
                    avg_rating = round(avg_rating, 1) if avg_rating is not None else None

                    trips.append({
                        'route': route,
                        'trip': trip,
                        'stops': stops,
                        'avg_rating': avg_rating
                    })

            context = {'trips': trips}
            return render(request, 'nextbus/search_results.html', context)
        except Station.DoesNotExist:
            # Handle invalid stations
            return render(request, 'nextbus/search_form.html', {'error': 'Invalid stations'})
    else:
        return render(request, 'nextbus/search_form.html')







