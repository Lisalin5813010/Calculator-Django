from django import template
register = template.Library()
@register.inclusion_tag('calculator/Geminput.html')

def Geminput(inputType=None, inputValue=None, inputId=None, inputPlaceholder=None, inputName=None, inputRequired=None):
    return {'inputType': inputType, 'inputName' : inputName, 'inputId' : inputId, 'inputPlaceholder' : inputPlaceholder,'inputValue' : inputValue, 'inputRequired' : inputRequired}