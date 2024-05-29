from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.inclusion_tag('calculator/Gemh2.html')

def Gemh2(h2Content):
    return {"h2Content": h2Content}