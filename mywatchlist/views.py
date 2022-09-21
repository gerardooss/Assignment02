from urllib import request
from django.shortcuts import render
from mywatchlist.models import MovieDetails
from django.http import HttpResponse
from django.core import serializers


# Create your views here.
def show_html(request):
    data_source = MovieDetails.objects.all()
    context = {
    "movie_details": data_source,
    "nama": "Bobi 88 Gaming",
    "npm": "2106708324",
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MovieDetails.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MovieDetails.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")