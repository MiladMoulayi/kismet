from django.urls import path
from kismet_app.views import HomeView, CharacterListView, CharacterDetailView, GameView, OutcomeView, OutcomeTattleTaleView, WinView, LoseView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('character_list', CharacterListView.as_view(), name='character_list'),
  path('character_detail/<int:character_id>', CharacterDetailView.as_view(), name='character_detail'),
  path('game', GameView.as_view(), name='game'),
  path('outcome/<str:type>', OutcomeView.as_view(), name='outcome'),
  path('outcome_tattle_tale', OutcomeTattleTaleView.as_view(), name='outcome_tattle_tale'),
  path('win', WinView.as_view(), name='win'),
  path('lose', LoseView.as_view(), name='lose')
]
