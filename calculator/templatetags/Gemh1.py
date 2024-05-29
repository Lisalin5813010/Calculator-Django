from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.inclusion_tag('calculator/Gemh1.html')

def Gemh1(h1Content=None):
    return {"h1Content": h1Content}