from django.forms import ModelForm
from .models import Room
#Creates formatting for already made model values such as name and description
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'