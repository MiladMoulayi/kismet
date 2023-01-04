from django.shortcuts import render
from django.views import View
from kismet_app.models import Character

# Create your views here.

class HomeView(View):
  def get(self, request):
    characters = Character.objects.all()

    html_data = {
      'character_list': characters,
    }

    return render(
        request=request,
        template_name='index.html',
        context=html_data,
    )
