from typing import Union, Optional

# The base piece of functionality... currying is the answer!
# Let's take a look at how this works...

def tag(name: str):

    #Here, we make (and return) a function to add attributes for our tag
    def add_attrs(attributes: dict = {}):

        attrs_str = _stringify_attrs(attributes)

        #Here we, in turn, make and return a function to put in the content!
        def add_content(*content: Optional[str]):
            if len(content) == 0:
                return f"<{name}{attrs_str} />"
            
            content = ''.join(content)

            return f"<{name}{attrs_str}>{content}</{name}>"
        return add_content

    return add_attrs

def _stringify_attrs(attributes: dict) -> str:
    return ''.join([f' {attr}="{val}"' for attr, val in attributes.items()])

# For convenience, let's also predefine some common tags
# Examples of their use can be found under tests/, but docs are to come!!

a = tag('a')
article = tag('article')
body = tag('body')
div = tag('div')
h1 = tag('h1')
li = tag('li')
main = tag('main')
p = tag('p')
section = tag('section')
ul = tag('ul')

