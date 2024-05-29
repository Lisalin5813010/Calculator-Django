from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gemtextarea.html')
def Gemtextarea(name = None,placeholder= None):
    return {'name': name,'placeholder': placeholder}