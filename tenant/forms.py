from django import forms
from tenant.models import Application

class ApplicationForm(forms.ModelForm):
    class Meta():
        model = Application
        fields = ('move_in_date', 'bio')
