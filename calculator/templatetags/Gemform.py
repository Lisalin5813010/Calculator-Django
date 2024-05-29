from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.inclusion_tag('calculator/Gemform.html')

def Gemform(formMethod=None):
    return {"formMethod": formMethod}