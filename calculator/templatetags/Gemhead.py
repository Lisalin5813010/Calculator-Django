from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gemhead.html')

def Gemhead():
    return {}