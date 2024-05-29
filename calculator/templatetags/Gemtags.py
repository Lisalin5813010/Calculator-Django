from django import template
from termcolor import colored
from django.utils.html import format_html
register = template.Library()
@register.simple_tag
def modify_name(value, arg):
    # if arg is first_name: return the first string before space
    if arg == "first_name":
        return value.split(" ")[0]
    # if arg is last_name: return the last string before space
    if arg == "last_name":
        return value.split(" ")[-1]
    # if arg is title_case: return the title case of the string
    if arg == "title_case":
        return value.title()
    return value
register.filter('modify_name', modify_name)



@register.simple_tag
def Gemspan_with_Method(author, id):
    return format_html('<span id="{}">{{}}</span><br>', id, author|modify_name)







@register.simple_tag
def Gemlink1():
    return format_html('<link rel="stylesheet" type="text/css" href="/static/css/style.css" ></link>')

@register.simple_tag
def Gemlink2():
    return format_html('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous"></link>')







@register.simple_tag
def endGemp_with_text():
    return format_html('</p>')



@register.simple_tag
def Gembr():
    return format_html('<br/>')



@register.simple_tag
def Gemhead():
    return format_html('<head>')

@register.simple_tag
def endGemhead():
    return format_html('</head>')

@register.simple_tag
def Gemtitle(title):
    return format_html('<title>{}</title>', title)

@register.simple_tag
def Gembody():
    return format_html('<body>')

@register.simple_tag
def endGembody():
    return format_html('</body>')