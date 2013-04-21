from django import template
import markdown

register = template.Library()

def mdown(value):
    md = markdown.Markdown(extensions=['mathjax', 'smartypants'])
    return md.convert(value)

register.filter('mdown', mdown)

