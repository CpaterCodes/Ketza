import pytest
from ..ketza.format import indent

def test_indent():
    indented_html: str
    with open("tests/indent_sample.html", "r") as f:
        indented_html = f.read()
    
    unindented_html = '<body id="App"><p>Hello</p><p>World</p></body>'
    assert indent(unindented_html) == indented_html

