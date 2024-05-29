from django import template
register = template.Library()

@register.inclusion_tag('calculator/endGemp.html')
def endGemp():
    return {}