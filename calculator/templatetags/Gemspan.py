from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gemspan.html')
def Gemspan(text):
    return {'text': text}