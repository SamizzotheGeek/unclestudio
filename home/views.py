from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from .forms import ContactForm
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
    form_class = ContactForm
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@unclesstudioworld.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact.html', {'page':name, 'form':form})
