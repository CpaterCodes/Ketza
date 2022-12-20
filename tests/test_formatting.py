import pytest
from ..ketza.format import indent, linebreaks

def test_linebreaks():
    linebroken_html: str
    with open("tests/linebreaks_sample.html", "r") as f:
        linebroken_html = f.read()

    unbroken_html = '<body id="App"><p>Hello</p><p>World</p></body>'
    assert linebreaks(unbroken_html) == linebroken_html


def test_indent():
    indented_html: str
    with open("tests/indent_sample.html", "r") as f:
        indented_html = f.read()
    
    unindented_html = '<body id="App"><p>Hello</p><p>World</p></body>'
    assert indent(unindented_html) == indented_html

