# coding:utf-8
from django import template

register = template.Library()

@register.filter
def appc(value):
    return str(value) + "1222"

