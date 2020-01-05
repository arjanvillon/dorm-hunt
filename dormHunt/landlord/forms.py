from django import forms
from landlord.models import Property

class PropertyForm(forms.ModelForm):

    class Meta():
        model = Property
        fields = ('name', 'house_number', 'street', 'barangay', 'city', 'zip_code', 'capacity', 'deposit', 'price', 'thumbnail', 'description', 'is_air_conditioned', 'is_ceiling_fans', 'is_sink', 'is_garbage_disposal', 'is_hardwood_floors', 'is_internet', 'is_microwave', 'is_refrigerator', 'is_storage', 'is_stove', 'is_telephone', 'is_tile', 'is_window_covering', 'is_laundry', 'is_parking', 'is_elevator', 'is_furnished', 'is_pets_allowed')

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
        
