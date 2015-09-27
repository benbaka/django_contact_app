from contacts.models.category import Category
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


class CategoryCreateView(CreateView):
    template_name = "categories/category_form.html"
    model = Category
    fields = ['name', 'description']


class CategoryDetailView(DetailView):
    template_name = "categories/category_detail.html"
    model = Category
