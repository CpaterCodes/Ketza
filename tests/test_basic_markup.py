import pytest
from ..ketza import p, div, section

def test_tags():
    target = '<p class="tag" id="hello-world">\n\tHello world!\n</p>'
    output = p({"class": "tag", "id": "hello-world"})(
            'Hello world!'
            )

    target2 = '<div class="tag2">\n\tHello python!\n</div>'
    output2 = div({"class": "tag2"})('Hello python!')
    assert output == target
    assert output2 == target2


def test_no_attributes():
    # Let's make sure we can generate a section without ne
    assert section()(
            'Nothing special'
            ) == '<section>\n\tNothing special\n</section>'

