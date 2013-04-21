from django import template
from markdown import markdown

register = template.Library()

def md2html(value):
    return (markdown(value).replace('---', '&mdash;')
            .replace('--', '&ndash;'))

register.filter('markdown', md2html)

