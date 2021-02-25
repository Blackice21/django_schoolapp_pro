from .models import School
from django.forms import ModelForm

class Schoolform(ModelForm):
    class Meta:
        model = School
        fields = ('__all__')