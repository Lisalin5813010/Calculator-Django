from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gemlink.html')
def Gemlink():
    return {}