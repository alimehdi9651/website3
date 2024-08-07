from django import forms
from .models import recipe

class recipe_form(forms.ModelForm):
     class Meta:
        model = recipe
        fields = '__all__'