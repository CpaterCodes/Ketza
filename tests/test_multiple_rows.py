import pytest
from ..ketza import ul, li

def test_multiple_contents():
    intent ="<ul>\n\t<li>\n\tFoo\n</li>\n<li>\n\tBar\n</li>\n</ul>"

    attempt = ul()(
            li()('Foo'),
            li()('Bar')
    )
    assert attempt == intent
