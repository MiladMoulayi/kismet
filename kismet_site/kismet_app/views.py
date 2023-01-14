from django.shortcuts import render, redirect
from django.views import View
from kismet_app.forms import CharacterForm, ScenarioForm, ChoiceForm, OutcomeForm
from kismet_app.models import Character, Scenario, Choice, Outcome
import random
# Create your views here.


# Updated code

class CreateView(View):
    def post(self, request):
        name = request.POST.get('name')
        alignment = request.POST.get('alignment')
        try:
            character = Character.objects.get(name=name)
        except Character.DoesNotExist:
            character = Character.objects.create(name=name, alignment=alignment)
        request.session['character'] = character
        return redirect('game')

class GameView(View):
    def get(self, request):
        character = request.session.get('character')
        if character:
            scenario = Scenario.objects.filter(characterName=character).order_by("?").first()
            context = {'scenario': scenario, 'character': character}
            return render(request, 'game.html', context)
        else:
            return redirect('create')
        
    def post(self, request):
        choice_id = request.POST.get('choice_id')
        try:
            choice = Choice.objects.get(pk=choice_id)
            outcome = Outcome.objects.get(choice=choice)
            if outcome.win:
                return redirect('win')
            else:
                return redirect('lose')
        except (Choice.DoesNotExist, Outcome.DoesNotExist):
            return redirect('game')




# class CreateView(View):
#     def get(self, request):
#         return render(request, 'create.html')

#     def post(self, request):
#         character = request.POST.get('character')
#         name = request.POST.get('name')
#         try:
#             player = Character.objects.get(name=name) # try to retrieve the player by name
#         except Character.DoesNotExist:
#             player = Character.objects.create(name=name, character=character) #create a new player
#         return redirect('game')

# class GameView(View):
#     def get(self, request):
#         scenarios = Scenario.objects.all() #fetches all of the made scenarios 
#         scenario = random.choice(scenarios) #retrieves a scenario at random
#         # character = request.session.get('character') > Troubleshooting adding the charatcher to the database
#         context = {'scenario': scenario}
#         return render(request, 'game.html', context)
    
#     def post(self, request):
#             choice = request.POST.get('choice')
#             scenario = Scenario.objects.get(pk=1)
#             # check if the choice matches the winning option of the scenario
#             if choice == scenario.winning_option:
#                 return render(request, 'win.html')
#             else:
#                 return render(request, 'lose.html')

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



