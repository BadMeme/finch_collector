from email.mime import image
from unicodedata import name
from django.shortcuts import render
from django.views import View # view class to handle requests
from django.http import HttpResponse # < class to handle sending a type of response

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Finch
# Create your views here.

# Here we will be creating a class called Home and extending it from the View class


class Home(TemplateView):
    template_name = "home.html"

# class Home(View):

#     #here we are adding a method that will be run when we are dealing with a GET request
#     def get(self, request): 
#         # similar to response.send() in express
#         return HttpResponse("Corby Home")

class About(TemplateView):
    template_name = "about.hmtl"

# class About(View):

#     #here we are adding a method that will be run when we are dealing with a GET request
#     def get(self, request): 
#         # similar to response.send() in express
#         return HttpResponse("Corby About")

class Finch2: 
    def __init__ (self, name, rating, bio, image="https://keithwitmer.com/keithwitmer/wp-content/uploads/2013/01/keith-witmer-engraving-motley-pawn1-300x300.jpg"):
        self.name = name
        self.rating = rating
        self.bio = bio
        self.image = image

finches = [
    Finch2("Magnus Carlsen", 2864, 'GOAT'),
    Finch2('Hikaru Nakamura', 2750, 'Blitz GOAT'),
    Finch2('Hans Niemann', 2699, 'Cheater lol')
]

class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name)
        else:
            context["finches"] = Finch.objects.all()
        return context

class Game :
    def __init__ (self, player1, player2, date="01/01/00", winner="Draw", image="https://static01.nyt.com/images/2022/06/13/crosswords/13chess-how-to-start/13chess-how-to-start-articleLarge.png?quality=75&auto=webp&disable=upscale"):
        self.white = player1.name
        self.black = player2.name
        self.title = f"{player1.name}({player1.rating}) vs. {player2.name}({player2.rating})"
        self.image = image
        self.winner = winner 

games = [
    Game(finches[0], finches[1]),
    Game(finches[0], finches[2], winner=finches[2].name)
]

class GamesList(TemplateView):
    template_name = "game_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games"] = games
        return context

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'bio', 'verified_player']
    template_name = 'finch_create.html'
    success_url = '/finches/'