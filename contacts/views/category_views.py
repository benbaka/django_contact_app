from contacts.models.category import Category
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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