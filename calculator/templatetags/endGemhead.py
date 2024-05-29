from django import template
register = template.Library()
@register.inclusion_tag('calculator/endGemhead.html')
def endGemhead():
    return {}