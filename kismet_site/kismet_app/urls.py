from django.urls import path
from kismet_app.views import HomeView, CreateView, GameView, WinView, LoseView, OutcomeView, CharacterDetailView, CharacterListView, OutcomeTattleTaleView
from . import views

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('game', GameView.as_view(), name='game'),
  path('win', WinView.as_view(), name='win'),
  path('lose', LoseView.as_view(), name='lose'),
  path('create', CreateView.as_view(), name='create'),
  path('outcome/<str:type>', OutcomeView.as_view(), name='outcome'),
  path('character_detail/<int:character_id>', CharacterDetailView.as_view(), name='character_detail'),
  path('character_list', CharacterListView.as_view(), name='character_list'),
  path('outcome_tattle_tale', OutcomeTattleTaleView.as_view(), name='outcome_tattle_tale')
]


# path('game', GameplayView.as_view(), name='game'),
  # path('start', StartView.as_view(), name='start'),