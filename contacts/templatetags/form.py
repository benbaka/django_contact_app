from django import template

register = template.Library()

@register.inclusion_tag('contacts/contact_form.html')
def contact_form(form, contact, categories, title):
    return {'form':form,
            'categories': categories,
            'title': title,
            'url': "/contacts/%s/update"%contact.id}