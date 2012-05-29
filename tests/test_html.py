# -*- coding: utf-8 -*-

import pyjade

import wiseguy as wg
import wiseguy.html


def test_process_jade():
    "Test that Jade basically works"
    d = "div#foo.bar Hullo"
    expected = '''<div id="foo" class="bar">Hullo</div>'''
    result = wg.html.process_jade(d)
    assert expected == result

def test_jade():
    d = wg.html.jade("html: body: div#main")
    assert d.tag == "html"

    expected = '''<html><body><div id="main"></div></body></html>'''
    result = d.to_string(pretty=False)
    assert result == expected

    expected = '''
<html><body><div id="main"></div></body></html>'''.strip()
    result = d.to_string().strip()
    assert result == expected

def test_template_insert():
    template = """
html
  head
    title
  body
    h1#title | placeholder text
    div#body"""
    t = wg.html.jade(template)
    t.insert("title, #title", "Hullo Mr Flibble")
    t.insert("#body", wg.html.Html("<span class='bar'>Welcome to my web</span>"))

    result = t.to_string().strip()
    expected = '''
<html>
<head><title>Hullo Mr Flibble</title></head>
<body>
<h1 id="title">Hullo Mr Flibble</h1>
<div id="body"><span class="bar">Welcome to my web</span></div>
</body>
</html>'''.strip()
    assert expected == result

def test_normalise_html():
    t = wg.html.Html('''<div id="foo" class="bar" style="bloop"> Hullo <strong>World!</strong><br>The End</div>''')
    result = wg.html.normalise_html(t).strip()
    expected = '''
<div class="bar" id="foo" style="bloop">
Hullo
<strong>
World!
</strong>
<br>
The End
</div>
'''.strip()
    assert result == expected
