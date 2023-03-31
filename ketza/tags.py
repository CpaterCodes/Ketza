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

