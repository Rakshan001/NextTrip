from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('bus', 'user', 'rating', 'created_at')
    list_filter = ('bus', 'created_at')
    search_fields = ('user__username', 'comment')
    readonly_fields = ('created_at', 'user','comment','rating')
    list_per_page=5

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('bus',)
        return self.readonly_fields

    def bus_reg_number(self, obj):
        return obj.bus.reg_number
    

    # def bus_name(self, obj):
    #     return obj.bus.name


# Queries
    from django.contrib import admin
from .models import Query

class QueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    

admin.site.register(Query, QueryAdmin)
