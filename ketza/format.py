from typing import Literal

def indent(
        raw_html: str, 
        indenter: Literal['tabs', 'spaces'] = 'tabs'
):
    tab = '\t' if indenter == 'tabs' else "    "

    # Add linebreaks
    raw_html = raw_html.replace('>', ">\n")

   # Add indents
   # TODO...
    return ''.join(raw_html)

