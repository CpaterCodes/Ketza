import pytest
from ..ketza.format import indent, linebreaks

def test_linebreaks():
    linebroken_html = '<body id="A">\n<p>\n1\n</p>\n<p>\n2\n</p>\n</body>\n'
    unbroken_html = '<body id="A"><p>1</p><p>2</p></body>'
    assert linebreaks(unbroken_html) == linebroken_html


def test_indent():
    indented_html = '<p>\n'
    indented_html += ''.join(
            [ f'\t<s>\n\t\t{n}\n\t</s>\n' for n in ['1', '2'] ]
    )
    indented_html += '</p>\n'
    unindented_html = '<p><s>1</s><s>2</s></p>'
    assert indent(unindented_html) == indented_html

