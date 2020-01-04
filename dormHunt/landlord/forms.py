from django import forms
from landlord.models import Property

class PropertyForm(forms.ModelForm):

    class Meta():
        model = Property
        fields = ('name', 'house_number', 'street', 'barangay', 'city', 'zip_code', 'capacity', 'deposit', 'price', 'thumbnail')

        labels = {
            "name": "Property Name" ,
            "address": "Address",
            "capacity": "Capacity", 
            "deposit": "Security Deposit",
            "price": "Monthly Payment",
            "thumbnail": "Thumbnail",
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(PropertyForm, self).__init__(*args, **kwargs)
        
