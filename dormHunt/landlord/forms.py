from django import forms
from landlord.models import Property

class PropertyForm(forms.ModelForm):

    class Meta():
        model = Property
        fields = ('name', 'house_number', 'street', 'barangay', 'city', 'zip_code', 'capacity', 'deposit', 'price', 'thumbnail')