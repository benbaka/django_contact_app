from contacts.forms.categoryForm import CategoryForm
from contacts.models.category import Category
from contacts.models.user_profile import UserProfile
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


class CategoryCreateView(CreateView):
    template_name = "categories/category_form.html"
    model = Category
    form_class = CategoryForm

    def form_valid(self, form):
        category = form.save(commit=False)
        category.owner=self.request.user.userprofile_set.filter()[0]
        category.save()
        return super(CategoryCreateView, self).form_valid(form)


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
