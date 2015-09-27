from contacts.models.category import Category
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


class CategoryCreateView(CreateView):
    template_name = "categories/category_form.html"
    model = Category
    fields = ['name', 'description']


class CategoryDetailView(DetailView):
    template_name = "categories/category_detail.html"
    model = Category

class CategoryListView(ListView):
    template_name = "categories/category_list.html"
    model = Category

class CategoryUpdateView(UpdateView):
    template_name = "categories/category_update.html"
    model = Category
    fields = ['name', 'description']
