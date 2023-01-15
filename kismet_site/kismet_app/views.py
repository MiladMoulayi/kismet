from django.shortcuts import render, redirect
from django.views import View
from kismet_app.forms import CharacterForm, ScenarioForm, ChoiceForm, OutcomeForm
from kismet_app.models import Character, Scenario, Choice, Outcome
import random
# Create your views here.

# in_time_of_need = Scenario.objects.create(name='In time of need', description='Decide whether or not to help your neighbor jumpstart his car')
# choice1 = Choice.objects.create(name='Get your jumper cables and help him', type='Good', scenario=in_time_of_need)
# choice2 = Choice.objects.create(name='Ignore him and continue to your car', type='Neutral', scenario=in_time_of_need)
# choice3 = Choice.objects.create(name='Laugh at him and tell him that\'s what he gets for buying a Chevy', type='Evil', scenario=in_time_of_need)


# Updated code

class CreateView(View):
    def get(self, request):
        return render(request, 'create.html')

    def post(self, request):
        character = request.POST.get('character')
        name = request.POST.get('name')
        try:
            player = Character.objects.get(name=name) # try to retrieve the player by name
        except Character.DoesNotExist:
            player = Character.objects.create(name=name, character=character) #create a new player
        return redirect('game')

class GameView(View):
    def get(self, request):
        scenarios = Scenario.objects.all() #fetches all of the made scenarios
        scenario = random.choice(scenarios)
        # scenario = Scenario.objects.get(name='In Time of Need') #retrieves a scenario
        # character = request.session.get('character') > Troubleshooting adding the charatcher to the database
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
            # check if the choice matches the winning option of the scenario
            # if choice == Choice.objects.get(type='Good').name:
            return redirect('outcome', type=choice.type)
            # elif choice == Choice.objects.get(type='Neutral').name:
            #     return redirect('outcome', type=choice.type)
            # elif choice == Choice.objects.get(type='Evil').name:
            #     return redirect('outcome')

class OutcomeView(View):
    def get(self, request, type):
        outcome = Outcome.objects.get(type=type)
        choice1 = outcome.choices.get(type='Good')
        choice2 = outcome.choices.get(type='Neutral')
        choice3 = outcome.choices.get(type='Evil')
        context = {
            'outcome': outcome,
            'choice1': choice1.name,
            'choice2': choice2.name,
            'choice3': choice3.name
        }
        return render(request, 'outcome.html', context)

class WinView(View):
    def get(self, request):
        return render(request, 'win.html')

class LoseView(View):
    def get(self, request):
        return render(request, 'lose.html')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



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

    return redirect('game')

class CharacterDetailView(View):
  def get(self, request, character_id):
    character=Character.objects.get(id=character_id)

# class GameplayView(View):
#   def get(self, request):
#     character_form = CharacterForm()
#     characters = Character.objects.all()
#     choice_form = ChoiceForm()
#     choices = Choice.objects.all()
#     outcome_form = OutcomeForm()
#     outcomes = Outcome.objects.all()
#     scenario_form = ScenarioForm()
#     scenarios = Scenario.objects.all()

#     html_data = {
#       'character_list': characters,
#       'character_form': character_form,
#       'choice_list': choices,
#       'choice_form': choice_form,
#       'outcome_list': outcomes,
#       'outcome_form': outcome_form,
#       'scenario_list': scenarios,
#       'scenario_form': scenario_form
#     }

#     return render(
#         request=request,
#         template_name='game.html',
#         context=html_data,
#     )

# class StartView(View):
#   def get(self, request):
#     character_form = CharacterForm()
#     characters = Character.objects.all()

#     html_data = {
#       'character_list': characters,
#       'form': character_form,
#     }

#     return render(
#         request=request,
#         template_name='index.html',
#         context=html_data,
#     )

#   def post(self, request):
#     print(request.POST)
#     character_form = CharacterForm(request.POST)
#     character_form.save()

#     return redirect('start')



