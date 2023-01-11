from django.urls import path
from kismet_app.views import HomeView, GameplayView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('game', GameplayView.as_view(), name='game')
]
