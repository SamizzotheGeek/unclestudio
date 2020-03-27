from django.shortcuts import render
#from django.http import Http404
# Create your views here.
def index(request):
    name = 'UNCLE S STUDIO WORLD'
    carousel1= "We value your health, stay safe"
    carousel2 = "All the family moments, captures in vivid shots"
    carousel3 = 'What is more valuable than celebrating true love, Uncle S Studio Freezes these moments for you'
    carousel4 = "We make all you memories count"
    #context= {'name':name}
    return render(request, 'index.html',{'page':name, 'carousel1':carousel1, 'carousel2':carousel2,'carousel3':carousel3,'carousel4':carousel4})

def contact(request):
    name = "Contact Us"
    return render(request, 'contact.html', {'page':name})
