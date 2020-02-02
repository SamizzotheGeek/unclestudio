from django.shortcuts import render
#from django.http import Http404
# Create your views here.
def index(request):
    name = 'UNCLE S STUDIO WORLD'
    #context= {'name':name}
    return render(request, 'index.html',{'page':name})

def contact(request):
    name = "Contact Us"
    return render(request, 'contact.html', {'page':name})