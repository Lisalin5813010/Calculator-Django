from django import template
register = template.Library()
@register.inclusion_tag('calculator/Gembutton.html')

def Gembutton(buttonType=None,  buttonName=None, buttonContent=None, buttonEvent=None):
    return {"buttonType": buttonType, "buttonName": buttonName, "buttonContent": buttonContent, "buttonEvent": buttonEvent}