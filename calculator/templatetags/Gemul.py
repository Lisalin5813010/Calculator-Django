from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.inclusion_tag('calculator/Gemul.html')

def Gemul(ulStyle = None, ulClass = None):
    return {"ulStyle": ulStyle, "ulClass": ulClass}