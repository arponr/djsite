import sys, subprocess

def conv(s):
    p = subprocess.Popen((['pandoc', '--from=markdown',
                           '--mathjax', '--to=html']
                          stdin=subprocess.PIPE,  
                          stdout=subprocess.PIPE))
    return ((p.communicate(s)[0]
             .replace('\n', '\n\n')
             .replace('---', '&mdash;')
             .replace('--', '&ndash;')))

if __name__ == '__main__':    
    fname = sys.argv[1]
    with open('blog/posts/' + fname + '.txt') as f:
        sep = '\n' + ('-' * 70) + '\n'
        fields = f.read().split(sep)
        preview, content = conv(fields[3]), conv(fields[4])
        with open('upload-temp', 'w') as g:
            for i in xrange(3):
                g.write(fields[i] + sep)
            g.write(preview + sep + content)
