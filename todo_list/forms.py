from django import forms
from .models import List

# Create your views here.
class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed"]
