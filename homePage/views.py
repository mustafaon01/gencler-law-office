import time

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from genclerLawOffice.settings import *


def home(request):
    return render(request, "index.html")
