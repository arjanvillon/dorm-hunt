from django import forms
from landlord.models import Property

class PropertyForm(forms.ModelForm):

    class Meta():
        model = Property
        fields = ('name', 'address', 'capacity', 'deposit', 'price', 'thumbnail')