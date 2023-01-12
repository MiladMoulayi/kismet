from django.forms import ModelForm
from kismet_app.models import Character, Scenario, Choice, Outcome

class CharacterForm(ModelForm):
  class Meta:
    model = Character
    fields = ['name','alignment']

class ScenarioForm(ModelForm):
  class Meta:
    model = Scenario
    fields = ['name', 'description', 'option1', 'option2', 'option3', 'winning_option']

class ChoiceForm(ModelForm):
  class Meta:
    model = Choice
    fields = ['name', 'type']

class OutcomeForm(ModelForm):
  class Meta:
    model = Outcome
    fields = ['name', 'type']


