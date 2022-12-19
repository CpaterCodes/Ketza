import pytest
from ..ketza import ul, li

def test_multiple_contents():
    intent ="<ul><li>Foo</li><li>Bar</li></ul>"

    attempt = ul()(
            li()('Foo'),
            li()('Bar')
    )
    assert attempt == intent
