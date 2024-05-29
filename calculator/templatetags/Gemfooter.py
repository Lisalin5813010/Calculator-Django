from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gemfooter.html')
def Gemfooter():
    return {}