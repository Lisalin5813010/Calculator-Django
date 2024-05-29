from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.inclusion_tag('calculator/Gemimg.html')
def Gemimg(imgSrc):
    src = f"/static/css/images/{imgSrc}"
    return {"src": src}