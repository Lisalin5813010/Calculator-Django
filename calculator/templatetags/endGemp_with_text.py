from django import template
register = template.Library()

@register.inclusion_tag('calculator/endGemp_with_text.html')
def endGemp_with_text():
    return {}