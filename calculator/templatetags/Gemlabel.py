from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.inclusion_tag('calculator/Gemlabel.html')

def Gemlabel(labelContent=None):
    return {'labelContent': labelContent}
