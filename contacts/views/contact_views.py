from contacts.forms.contact_form import ContactForm
from django.contrib import messages
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
                messages.add_message(request, messages.SUCCESS, "Contact successfully created" )
                return redirect('/contacts/')
            except:
                messages.add_message(request, messages.ERROR, "Contact creation unsuccessful" )
                return render(request, 'contacts/new_contact_form.html', {'form':form})
        else:
            messages.add_message(request, messages.ERROR, "Contact creation unsuccessful" )
            return render(request, 'contacts/new_contact_form.html', {'form':form})

def edit(request, id):

    contact = Contact.objects.get(id=id)

    edit_contact_form = ContactForm({'name':contact.name, 'age': contact.age })
    return render(request, 'contacts/new_contact_form.html', {'form':edit_contact_form, 'contact':contact})
