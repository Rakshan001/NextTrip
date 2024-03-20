from django import forms
from nextbus.models import Trip  # Assuming the model is in the "nextbus" app


class BookingForm(forms.ModelForm):
    has_seat = forms.BooleanField(label="I will have a seat", required=False)

    class Meta:
        model = Trip
        fields = ['origin', 'destination', 'date', 'time', 'has_seat',]
