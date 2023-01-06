from django.shortcuts import render

# Create your views here.
def index(response):
    return render(response, "main/base.html", {})

def nba(response):
    return render(response, "main/nba.html", {})