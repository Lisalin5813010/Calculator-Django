from django import template
register = template.Library()
@register.inclusion_tag('calculator/endGembody.html')
def endGembody():
    return {}