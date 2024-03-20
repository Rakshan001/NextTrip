# # forms.py

# from django import forms
# from nextbus.models import Bus
# from .models import Ticket

# class TicketForm(forms.ModelForm):
#     bus = forms.ModelChoiceField(queryset=Bus.objects.all(), label='Bus')

#     class Meta:
#         model = Ticket
#         fields = ['origin', 'destination', 'date', 'time', 'cost', 'bus']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['date'].widget.attrs['class'] = 'datepicker'  # Add CSS class for datepicker
#         self.fields['time'].widget.attrs['class'] = 'timepicker'  # Add CSS class for timepicker























# ##################

from django import forms
from .models import Ticket
from django.utils import timezone

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['origin','destination', 'date', 'time', 'cost','bus']

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.initial['date'] = timezone.now().date()
        self.initial['time'] = timezone.now().strftime('%H:%M')


################################################



