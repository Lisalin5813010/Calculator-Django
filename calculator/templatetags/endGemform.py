from django import template
register = template.Library()

@register.inclusion_tag('calculator/endGemform.html')
def endGemform():
    return {}