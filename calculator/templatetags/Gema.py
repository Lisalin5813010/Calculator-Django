from django import template
from django.urls import reverse

register = template.Library()
@register.inclusion_tag('calculator/Gema.html')

def Gema(aId=None, item_pk=None, aText=None):
  if item_pk is None:
    url = reverse(aText)
  else:
    url = reverse(aText, kwargs={'pk': item_pk})
  return { 'aId':aId, 'url': url, 'aText':aText}