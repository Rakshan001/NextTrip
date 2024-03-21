# In admin.py

# from django.contrib import admin
# from .models import Ticket
# from nextbus.models import Bus


# class TicketAdmin(admin.ModelAdmin):
#     list_display = ('id','user','origin', 'destination', 'is_verified')

# admin.site.register(Ticket, TicketAdmin)




from django.contrib import admin
from django.db.models import Sum
from .models import Ticket

def calculate_total_cost(modeladmin, request, queryset):
    total_cost = queryset.aggregate(total_cost=Sum('cost')).get('total_cost')
    if total_cost is not None:
        message = f'Total Cost of Selected Ticket Bookings: {total_cost}'
        modeladmin.message_user(request, message)
    else:
        modeladmin.message_user(request, 'No ticket bookings selected.')

calculate_total_cost.short_description = 'Calculate Total Cost'




#################################

from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'origin', 'destination', 'is_verified','cost')
    list_filter = ('bus','date','is_verified')  # Add this line to enable filtering by bus
    list_per_page=10
    actions = [calculate_total_cost]

admin.site.register(Ticket, TicketAdmin)












