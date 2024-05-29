from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.inclusion_tag('calculator/endGemul.html')

def endGemul():
    return {}