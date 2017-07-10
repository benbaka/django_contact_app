from django.contrib import admin
from contacts.models.category import Category
from contacts.models.user_profile import UserProfile
from contacts.models.contact import Contact
# Register your models here.
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Contact)
