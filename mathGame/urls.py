from django.urls import path
from mathGame.views import HomeView, mathGameView, anagramGaneView

app_name = 'mathGame'
urlPatterns = [
    path('', HomeView.as_view(), name = 'homepage'),
    path('math-game/', mathGameView.as_view(), name = 'math-game'),
    path('anagram-game/', anagramGaneView.as_view(), name = 'anagram-game'),
]