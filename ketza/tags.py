from typing import Union

# The base piece of functionality... currying is the answer!
# Let's take a look at how this works...

def tag(name: str):

    #Here, we make (and return) a function to add attributes for our tag
    def add_attrs(attributes: dict):
        
        attributes_str = ' '.join(
                [f'{attr}="{val}"' for attr, val in attributes.items()]
        )
        
        #Here we, in turn, make and return a function to put in the content!
        def add_content(content: str):
            return f"<{name} {attributes_str}>\n\t{content}\n</{name}>"
        
        return add_content

    return add_attrs

# For convenience, let's also predefine some common tags
# Examples of their use can be found under tests/, but docs are to come!!

article = tag('article')
div = tag('div')
h1 = tag('h1')
main = tag('main')
p = tag('p')
section = tag('section')

