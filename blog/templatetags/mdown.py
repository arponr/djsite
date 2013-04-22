from django import template
import markdown

register = template.Library()

def mdown(value):
    md = markdown.Markdown(extensions=[MathJaxExtension()])
    return (md.convert(value).replace('---', '&mdash;')
            .replace('--', '&ndash;') )

register.filter('mdown', mdown)

class MathJaxPattern(markdown.inlinepatterns.Pattern):
    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(
            self, r'(?<!\\)(\$\$?)(.+?)\2'
        )

    def handleMatch(self, m):
        el = markdown.util.etree.Element('span')
        el.set('class', 'math')
        el.text = m.group(2) + m.group(3) + m.group(2)
        return el

class MathJaxExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('mathjax', MathJaxPattern(), '<escape') 

