from django.forms import ModelForm
from .models import *
class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = '__all__'
