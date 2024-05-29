from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gemscript.html')
def Gemscript():
    return {}