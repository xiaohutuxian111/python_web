"""
@FileName：filter_dict.py
@Author：stone
@Time：2023/4/22 13:58
@Description:
"""
from django import template

register = template.Library()

@register.filter('get_dict_value')
def get_dict_value(d, key):
    return d[key]