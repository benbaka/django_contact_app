from django.template import Library

register = Library()


@register.filter(name='addcss')
def addcss(field, class_attr):
    return field.as_widget(attrs={'class': class_attr})