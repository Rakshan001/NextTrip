from django.contrib import admin
from .models import Station, Bus, Trip, Route, Stop

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'capacity')
    search_fields = ('number', 'name')

@admin.register(Stop)
class BusStop(admin.ModelAdmin):
    list_filter = ('route',)  # Corrected tuple format

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_filter=('bus',)

@admin.register(Trip)
class BusTrip(admin.ModelAdmin):
    list_filter=('route__bus','departure_date')

admin.site.register(Station)
# admin.site.register(Route)
# admin.site.register(Trip)
