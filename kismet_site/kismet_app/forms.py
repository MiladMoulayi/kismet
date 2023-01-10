from django.forms import ModelForm
from kismet_app.models import Character

class CharacterForm(ModelForm):
  class Meta:
    model = Character
    fields = ['name']