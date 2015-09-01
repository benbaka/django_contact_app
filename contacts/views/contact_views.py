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

    if request.method == "GET":

        contact = Contact.objects.get(id=id)
        edit_contact_form = ContactForm({'name':contact.name, 'age': contact.age })
        return render(request, 'contacts/edit_contact_form.html', {'form':edit_contact_form, 'contact':contact})
    else:
        contact = Contact.objects.get(id=id)
        edit_contact_form = ContactForm(request.POST)

        if edit_contact_form.is_valid():
            contact.name = edit_contact_form.cleaned_data['name']
            contact.age = edit_contact_form.cleaned_data['age']
            contact.save()

            messages.add_message(request, messages.SUCCESS, "Contact successfully edited" )
            return redirect('/contacts/')
        else:
            messages.add_message(request, messages.ERROR, "Contact editing unsuccessful" )
            return render(request, 'contacts/edit_contact_form.html', {'form':edit_contact_form, 'contact':contact})

def show(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contacts/show.html', {'contact': contact})

def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()

    return redirect('/contacts/')


def my_decorator(original_func):


    def bad_func(request):
        if request.method == "GET":
            original_func(request)
            import pdb; pdb.set_trace()
        else:
            print "Send a redirect"

    return bad_func

@my_decorator
def me(request):
    return redirect('/contacts/')

