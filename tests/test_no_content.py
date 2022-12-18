import pytest
from ..ketza import a

def test_no_content():

    example_link_base = a({"href": "www.example.com"})

    without_text = example_link_base() 
    assert without_text == '<a href="www.example.com" />'

    with_text = example_link_base("Example")
    assert with_text == '<a href="www.example.com">\n\tExample\n</a>'

