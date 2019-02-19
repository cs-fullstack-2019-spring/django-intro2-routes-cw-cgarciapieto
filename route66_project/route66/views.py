from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# http response function
def goods(request):
    return HttpResponse("Here you go, POKEMON FOREVER")

def joy(request):
    return HttpResponse("This song drives me nuts")

def index(request):
    return HttpResponse("the goods or song of death")
# challenge variable is passed in
def response(request):
    return HttpResponse(challenge)
challenge =("I heard you")

