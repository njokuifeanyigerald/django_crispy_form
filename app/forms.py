from django import forms
from django.db.models import fields
from .models import CrispyModel

class CrispyForm(forms.ModelForm):
    class Meta:
        model = CrispyModel
        fields = '__all__'