import pytest
from ..ketza import a

def test_no_content():

    # To show we can create a tags with or without internal text, let's make a base!
    example_link_base = a({"href": "www.example.com"})

    example_link_no_text = example_link_base() 
    assert example_link_no_text == '<a href="www.example.com" />'

    example_link_with_text = example_link_base("Example")
    assert example_link_with_text == '<a href="www.example.com">\n\tExample\n</a>'

def test_multiple_elements():
    pass
