from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.inclusion_tag('calculator/Gemtable.html')

def Gemtable(data_list):
    if not data_list:
        return ""
    else:
        return {"data_list": data_list}