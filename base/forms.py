from django.forms import ModelForm
from .models import Room
from django.contrib.auth.forms import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # Gives all fields of Room class
        exclude = ['host', 'participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
