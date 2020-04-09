from django import forms
from .models import Reservation

class ReservationTableForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'