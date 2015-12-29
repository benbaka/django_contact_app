from contacts.forms.contact_form import ContactForm
from contacts.models.category import Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from contacts.models import Contact

def get_user_profile(request):
    user = User.objects.get(id = request.user.id)
    profile = user.userprofile_set.get_or_create(user=user)
    return profile[0]

@login_required(login_url="/admin/login")
def index(request):
    all_contacts = Contact.objects.filter(public=True)
    context = {'contacts':all_contacts}
    return render(request, 'contacts/index.html', context)

@login_required(login_url="/admin/login")
def new(request):
    if request.method == "GET":
        current_user = request.user
        form = ContactForm(current_user=current_user)
        user_profile = request.user.userprofile_set.filter()[0]
        form_categories = Category.objects.filter(owner=user_profile)
        return render(request, 'contacts/new_contact_form.html', {'form':form,'form_categories':form_categories})
    else:
        form = ContactForm(data=request.POST, current_user=request.user)

        if form.is_valid():
            try:
                user_profile = get_user_profile(request)
                age = form.cleaned_data['age']
                name = form.cleaned_data['name']
                public = form.cleaned_data['public']
                category_id = form.cleaned_data['category']
                category = Category.objects.filter(id=category_id)[0]
                contact = Contact(age=age, name=name, public=public, owner=user_profile, category=category)
                contact.save()
                messages.add_message(request, messages.SUCCESS, "Contact successfully created" )
                return redirect('/contacts/')
            except:
                messages.add_message(request, messages.ERROR, "Contact creation unsuccessful" )
                return render(request, 'contacts/new_contact_form.html', {'form':form})
        else:
            messages.add_message(request, messages.ERROR, "Contact creation unsuccessful" )
            return render(request, 'contacts/new_contact_form.html', {'form':form})

@login_required(login_url="/admin/login")
def edit(request, id):

    if request.method == "GET":

        contact = Contact.objects.get(id=id)
        current_user = request.user
        edit_contact_form = ContactForm(current_user, {'name':contact.name, 'age': contact.age})
        return render(request, 'contacts/edit_contact_form.html', {'form':edit_contact_form, 'contact':contact})
    else:
        contact = Contact.objects.get(id=id)
        edit_contact_form = ContactForm(request.user, request.POST)

        if edit_contact_form.is_valid():
            contact.name = edit_contact_form.cleaned_data['name']
            contact.age = edit_contact_form.cleaned_data['age']
            contact.public = edit_contact_form.cleaned_data['public']
            contact.owner = get_user_profile(request)
            contact.save()

            messages.add_message(request, messages.SUCCESS, "Contact successfully edited" )
            return redirect('/contacts/')
        else:
            messages.add_message(request, messages.ERROR, "Contact editing unsuccessful" )
            return render(request, 'contacts/edit_contact_form.html', {'form':edit_contact_form, 'contact':contact})

@login_required(login_url="/admin/login")
def show(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contacts/show.html', {'contact': contact})

@login_required(login_url="/admin/login")
def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()

    return redirect('/contacts/')

@login_required(login_url="/admin/login")
def get_user_based_contacts(request):
    user_profile = get_user_profile(request)
    contacts = Contact.objects.filter(owner=user_profile)
    context = {'contacts':contacts}
    return render(request, 'contacts/user_based_contacts.html', context)



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

