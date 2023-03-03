from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from kismet_app.forms import CharacterForm, ScenarioForm, ChoiceForm, OutcomeForm
from kismet_app.models import Character, Scenario, Choice, Outcome
import random
# Create your views here.

# HomeView renders the home page of the Kismet app. It provides a character creation screen with
# the ability to input a character name and alignment.
class HomeView(View):
  def get(self, request):
    character_form = CharacterForm()

    html_data = {
      'form': character_form,
    }

    return render(
        request=request,
        template_name='index.html',
        context=html_data
    )

  def post(self, request):
    character_form = CharacterForm(request.POST)
    character_form.save()

    return redirect('game')

# The CharacterListView provides a list of all of the characters that have been created,
# with links to their detail views.
class CharacterListView(View):
  def get(self, request):
    characters = Character.objects.all()

    html_data = {
      'character_list': characters
    }

    return render(
        request=request,
        template_name='character_list.html',
        context=html_data
    )

# The CharacterDetailView renders a page with the characters name, alignment, and the option
# to either update or delete the character.
class CharacterDetailView(View):
  def get(self, request, character_id):
    character=Character.objects.get(id=character_id)
    character_form=CharacterForm(instance=character)
    html_data = {
        'character_name': character.name,
        'alignment': character.alignment,
        'form': character_form,
    }
    return render(
        request=request,
        template_name='character_detail.html',
        context=html_data
    )

  def post(self, request, character_id):
    character=Character.objects.get(id=character_id)

    if 'update' in request.POST:
        character_form = CharacterForm(request.POST, instance=character)
        character_form.save()
    elif 'delete' in request.POST:
        character.delete()

    return redirect('character_list')

# The GameView renders the gameplay portion of Kismet. It presents the player with a scenario and
# multiple options to choose from, which lead to outcomes with other potential choices.
class GameView(View):
    def get(self, request):
        scenarios = Scenario.objects.all()
        scenario = random.choice(scenarios)
        context = {
            'scenario': scenario,
            'choice1': Choice.objects.get(type='Good', the_scenario=scenario, level=0).name,
            'choice2': Choice.objects.get(type='Neutral', the_scenario=scenario, level=0).name,
            'choice3': Choice.objects.get(type='Evil', the_scenario=scenario, level=0).name
            }
        return render(request, 'game.html', context)

    def post(self, request):
            choice = Choice.objects.get(name=request.POST.get('choice'))
            choice.save()
            return redirect('outcome', type=choice.type)

# The OutcomeView is the result of making a choice in the GameView. It renders a page that is the
# outcome of the player's previous decision.
class OutcomeView(View):
    def get(self, request, type):
        outcome = Outcome.objects.get(type=type)
        try:
            choice1 = outcome.choices.get(type='Good')
            choice2 = outcome.choices.get(type='Neutral')
            choice3 = outcome.choices.get(type='Evil')
        except ObjectDoesNotExist:
            return redirect('outcome_tattle_tale')

        context = {
            'outcome': outcome,
            'choice1': choice1.name,
            'choice2': choice2.name,
            'choice3': choice3.name
        }
        return render(request, 'outcome.html', context)

    def post(self, request, type):
        choice = Choice.objects.get(name=request.POST.get('choice'))
        choice.save()

        if choice.type == "Good":
            return redirect('win')
        else:
            return redirect("lose")

# The OutcomeTattleTaleView renders the page of the outcome specific to the case of the player
# choosing to tell the teacher as their first choice.
class OutcomeTattleTaleView(View):
    def get(self, request):
        tattle_tale_choice=Choice.objects.get(name='Tell the teacher.')
        tattle_tale_outcome=Outcome.objects.get(type='Neutral')

        html_data= {
            'choice': tattle_tale_choice,
            'outcome': tattle_tale_outcome
        }

        return render(request, 'outcome_tattle_tale.html', context=html_data)

# The WinView renders the page that is the result of making the final correct choice.
class WinView(View):
    def get(self, request):
        return render(request, 'win.html')

# The LoseView renders the page that is the result of making the final incorrect choice.
class LoseView(View):
    def get(self, request):
        return render(request, 'lose.html')