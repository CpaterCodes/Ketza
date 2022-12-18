import pytest
from ..ketza import ul, li

def test_multiple_contents():
    intent ="<ul>\n<li>\nFoo\n</li>\n<li>\nBar\n</li>\n</ul>"

    attempt = ul()(
            li()('Foo'),
            li()('Bar')
    )
    assert attempt == intent
