from django import template
import markdown

register = template.Library()

def mdown(value):
    md = markdown.Markdown(extensions=[MathJaxExtension()])
    return (md.convert(value).replace('---', '&mdash;')
            .replace('--', '&ndash;') )

register.filter('mdown', mdown)

class MathJaxPattern(markdown.inlinepatterns.SimpleTextPattern):
    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(
            self, r'(?<!\\)(\$\$?)(.+?)\2'
        )



class MathJaxExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('mathjax', MathJaxPattern(), '<escape') 

