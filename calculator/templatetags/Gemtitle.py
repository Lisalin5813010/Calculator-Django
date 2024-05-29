from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gemtitle.html')
def Gemtitle(titleContent= None):
    return {'titleContent': titleContent}