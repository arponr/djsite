from django import template
from markdown import markdown

register = template.Library()

def mdown(value):
    return (markdown(value).replace('---', '&mdash;')
            .replace('--', '&ndash;'))

register.filter('mdown', mdown)

