from html.parser import HTMLParser

class S(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.inside = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.inside = False

    def handle_data(self, data):
        if self.inside:
            self.data.append(data)

parser = S()
with open('birthday.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

script = ''.join(parser.data)
with open('tmp_script_check.js', 'w', encoding='utf-8') as out:
    out.write(script)
print('script-length', len(script))
