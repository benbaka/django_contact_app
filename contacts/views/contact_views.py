from django.http import HttpResponse
from django.shortcuts import render
from contacts.models import Contact

def index(request):
    all_contacts = Contact.objects.all()
    context = {'contacts':all_contacts}
    return render(request, 'contacts/index.html', context)

def new(request):
    return HttpResponse(status=200)