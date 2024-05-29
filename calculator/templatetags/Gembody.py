from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gembody.html')
def Gembody():
    return {}