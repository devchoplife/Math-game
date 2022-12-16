from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "math-game.html"

class mathGameView(TemplateView):
    template_name = "math-game.html"

class anagramGaneView(templateView):
    template_name = "anagram-game.html"