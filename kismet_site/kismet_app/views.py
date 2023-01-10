from django.shortcuts import render, redirect
from django.views import View
from kismet_app.forms import CharacterForm
from kismet_app.models import Character

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




