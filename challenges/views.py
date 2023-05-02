from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk",
    "march": "learn Django",
    "april": "eat no meat",
    "may": "sleep on time",
    "june": "learn pythosdfasdfasdfn",
    "july": "plan a trip for nexy month",
    "august": "read 10 pages a night",
    "september": "learn react",
    "october" : "go on the trip planned",
    "november" : "read 100 pages",
    "december" : "learn Ddjango"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("this month is not supported")
    return HttpResponse(challenge_text)
