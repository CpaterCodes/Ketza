from typing import Literal
from re import findall

def indent(
        raw_html: str, 
        indenter: Literal['tabs', 'spaces'] = 'tabs'
):

    # Mark out linebreaks
    raw_html = linebreaks(raw_html)

    # Add indents, starting by getting full rows
    rows = raw_html.split('\n')
    indented_rows = [''] * len(rows)
    depth: int = 0
    tab = '\t' if indenter == 'tabs' else "    "
    for i in range(len(rows)):
        row = rows[i]

        if _is_closing_tag(row):
            depth -= 1
            indented_rows[i] = f"{tab * depth}{row}\n"

        elif _is_opening_tag(row):
            indented_rows[i] = f"{tab * depth}{row}\n"
            depth += 1

        else:
            indented_rows[i] = f"{tab * depth}{row}\n"


    return ''.join(indented_rows[:-1])

def linebreaks(raw_html: str):
    return raw_html.replace(
            '>', ">\n"
        ).replace(
            '<', "\n<"
        ).replace(
            "\n\n", "\n"
            )[1:]


def _is_closing_tag(row: str): 
    return "</" in row


def _is_opening_tag(row: str):
    return _is_tag(row) and not _is_oneline_tag(row)


def _is_oneline_tag(row: str):
    return "/>" in row


def _is_tag(row: str):
    return "<" in row and ">" in row
