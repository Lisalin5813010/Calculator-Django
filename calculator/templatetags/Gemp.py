from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gemp.html')
def Gemp(pText=None):
    return {"pText": pText}