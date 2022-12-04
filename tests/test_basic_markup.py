import pytest
from ..ketza import p, div

def test_tags():
    target = '<p class="tag" id="hello-world">\n\tHello world!\n</p>'
    output = p({"class": "tag", "id": "hello-world"})(
            'Hello world!'
            )

    target2 = '<div class="tag2">\n\tHello python!\n</div>'
    output2 = div({"class": "tag2"})('Hello python!')
    assert output == target
    assert output2 == target2

