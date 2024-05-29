from django import template
register = template.Library()

@register.inclusion_tag('calculator/Gemnav.html')
def Gemnav():
    return {}