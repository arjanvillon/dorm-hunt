from django import forms
from landlord.models import Property, Reminder, AddTenant

class PropertyForm(forms.ModelForm):

    class Meta():
        model = Property
        fields = ('name', 'house_number', 'street', 'barangay', 'city', 'zip_code', 'capacity', 'deposit', 'price', 'thumbnail', 'description', 'tagline', 'is_air_conditioned', 'is_ceiling_fans', 'is_sink', 'is_garbage_disposal', 'is_hardwood_floors', 'is_internet', 'is_microwave', 'is_refrigerator', 'is_storage', 'is_stove', 'is_telephone', 'is_tile', 'is_window_covering', 'is_laundry', 'is_parking', 'is_elevator', 'is_furnished', 'is_pets_allowed')

        labels = {
            "name": "Property Name" ,
            "address": "Address",
            "capacity": "Capacity", 
            "deposit": "Security Deposit",
            "price": "Monthly Payment",
            "thumbnail": "Thumbnail",
            "tagline": "Short Description",
            # Features
            "is_air_conditioned": "Air Conditioning",
            "is_ceiling_fans": "Ceiling Fans",
            "is_sink": "Sink",
            "is_garbage_disposal": "Garbage Disposal",
            "is_hardwood_floors": "Hardwood Flooring",
            "is_internet": "Internet",
            "is_microwave": "Microwave",
            "is_refrigerator": "Refrigerator",
            "is_storage": "Storage/Cabinet",
            "is_stove": "Stove",
            "is_telephone": "Telephone",
            "is_tile": "Tile",
            "is_window_covering": "Window Coverings",
            "is_laundry": "Laundry",
            "is_parking": "Parking Area",
            "is_furnished": "Furnished",
            "is_pets_allowed": "Pets Allowed",
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(PropertyForm, self).__init__(*args, **kwargs)

class ReminderForm(forms.ModelForm):

    class Meta():
        model = Reminder
        fields = ('property_name', 'category', 'sub_category', 'issue', 'next_service', 'days_before', 'description')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(ReminderForm, self).__init__(*args, **kwargs)

class AddTenantForm(forms.ModelForm):

    class Meta():
        model = AddTenant
        fields = ('account_user', 'dorm', 'room_description')
        labels = {
            "account_user": "Email Address",
            "dorm": "Property",
            "room_description": "Room Description",
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(AddTenantForm, self).__init__(*args, **kwargs)

        
        
