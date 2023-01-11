from django.shortcuts import render, redirect
from django.views import View
from kismet_app.forms import CharacterForm, ScenarioForm, ChoiceForm, OutcomeForm
from kismet_app.models import Character, Scenario, Choice, Outcome
# Create your views here.

class HomeView(View):
  def get(self, request):
    character_form = CharacterForm()
    characters = Character.objects.all()

    html_data = {
      'character_list': characters,
      'form': character_form,
    }

    return render(
        request=request,
        template_name='index.html',
        context=html_data,
    )

  def post(self, request):
    print(request.POST)
    character_form = CharacterForm(request.POST)
    character_form.save()

    return redirect('home')

class CharacterDetailView(View):
  def get(self, request, character_id):
    character=Character.objects.get(id=character_id)

class GameplayView(View):
  def get(self, request):
    character_form = CharacterForm()
    characters = Character.objects.all()
    choice_form = ChoiceForm()
    choices = Choice.objects.all()
    outcome_form = OutcomeForm()
    outcomes = Outcome.objects.all()
    scenario_form = ScenarioForm()
    scenarios = Scenario.objects.all()

    html_data = {
      'character_list': characters,
      'character_form': character_form,
      'choice_list': choices,
      'choice_form': choice_form,
      'outcome_list': outcomes,
      'outcome_form': outcome_form,
      'scenario_list': scenarios,
      'scenario_form': scenario_form
    }

    return render(
        request=request,
        template_name='index.html',
        context=html_data,
    )




