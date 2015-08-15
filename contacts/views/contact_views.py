from contacts.forms.contact_form import ContactForm
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
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
            try:
                age = form.cleaned_data['age']
                name = form.cleaned_data['name']
                contact = Contact(age=age, name=name)
                contact.save()
                return redirect('/contacts/')
            except:
                return render(request, 'contacts/new_contact_form.html', {'form':form})
        else:
            return render(request, 'contacts/new_contact_form.html', {'form':form})