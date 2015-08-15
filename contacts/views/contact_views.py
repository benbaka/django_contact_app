from contacts.forms.contact_form import ContactForm
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from contacts.models import Contact

def index(request):
    all_contacts = Contact.objects.all()
    context = {'contacts':all_contacts}
    return render(request, 'contacts/index.html', context)

def new(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'contacts/new_contact_form.html', {'form':form})
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('contacts/')
        else:
            import pdb; pdb.set_trace()
            return render(request, 'contacts/new_contact_form.html', {'form':form})