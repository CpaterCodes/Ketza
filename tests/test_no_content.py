import pytest
from ..ketza import a

def test_no_content():

    example_link = a({"href": "www.example.com"})()
    assert example_link == '<a href="www.example.com" />'


