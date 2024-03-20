# In admin.py

# from django.contrib import admin
# from .models import Ticket
# from nextbus.models import Bus


# class TicketAdmin(admin.ModelAdmin):
#     list_display = ('id','user','origin', 'destination', 'is_verified')

# admin.site.register(Ticket, TicketAdmin)



#################################

from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'origin', 'destination', 'is_verified')
    list_filter = ('bus','date','is_verified')  # Add this line to enable filtering by bus
    

admin.site.register(Ticket, TicketAdmin)