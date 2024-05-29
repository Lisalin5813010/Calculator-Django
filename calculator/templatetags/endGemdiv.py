from django import template
register = template.Library()

@register.inclusion_tag('calculator/endGemdiv.html')
def endGemdiv():
    return {}