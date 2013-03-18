import sys, subprocess

if __name__ == '__main__':    
    fname = sys.argv[1]
    with open('blog/entries/' + fname + '.txt') as f:
        _title = f.readline()
        _slug = f.readline()
        _cats = f.readline()
        p = subprocess.Popen(['pandoc', '--from=markdown',
                              '--mathjax', '--to=html'], 
                             stdin=subprocess.PIPE, 
                             stdout=subprocess.PIPE)
        _content = (p.communicate(f.read().lstrip())[0]
                    .replace('\n', '\n\n')
                    .replace('---', '&mdash;')
                    .replace('--', '&ndash;'))
        with open('upload-temp', 'w') as g:
            g.write(_title + _slug + _cats)
            g.write('\n' + _content)
