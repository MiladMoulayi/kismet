from django.urls import path
from kismet_app.views import HomeView, CreateView, GameView, WinView, LoseView
from . import views

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('game', GameView.as_view(), name='game'),
  path('win', WinView.as_view(), name='win'),
  path('lose', LoseView.as_view(), name='lose'),
  path('create', CreateView.as_view(), name='create'),
]


# path('game', GameplayView.as_view(), name='game'),
  # path('start', StartView.as_view(), name='start'),