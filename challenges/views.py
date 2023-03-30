from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = 'This works!'
    elif month == "february":
        challenge_text = 'Challenges for February!'
    else:
        return HttpResponseNotFound("this month is not supported!!!")
    return HttpResponse(challenge_text)
