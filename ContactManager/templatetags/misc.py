from django import template

register = template.Library()


@register.filter
def concat(str1, str2):
    return str(str1)+str(str2)
