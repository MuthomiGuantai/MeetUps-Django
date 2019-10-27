import requests
from requests.compat import quote_plus
from django.shortcuts import render
from django.urls import reverse
from bs4 import BeautifulSoup
from . import models


# Create your views here.


def home(request):
    return render(request, 'base.html')


def meet_ups(request):
    return render(request, 'meet/meet_ups.html')


def profile(request):
    return render(request, 'meet/profile.html')


