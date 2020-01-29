from django.shortcuts import render
from django.http import Http404
# Create your views here.
def index(request):
    name = 'UNCLE S STUDIO WORLD'
    return render('request', 'index.html', {'page': name})