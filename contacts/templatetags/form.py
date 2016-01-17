from django import template

register = template.Library()

@register.inclusion_tag('contacts/contact_form.html')
def contact_form(form, contact, categories):
    return {'form':form,
            'categories': categories,
            'url': "/contacts/%s/update"%contact.id}