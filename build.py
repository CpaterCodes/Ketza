from bs4 import BeautifulSoup
import logging


def uniq(collection: list):
    return list(dict.fromkeys(collection).keys())


def load_html() -> str:
    """ 
    Load the W3C HTML5 reference document.
    Aborts script if this fails.
    """
    with open("W3C_HTML5_Elements.html", "r") as w3c_html_file:
        return w3c_html_file.read()


def retrieve_tag_names(w3c_soup: BeautifulSoup) -> list[str]:
    """ 
    Extract the set of all tags from the document, removing duplicates.
    """
    tags = uniq(w3c_soup.find_all("span", "element"))
    
    return [tag.string for tag in tags]


def clean_tag_names(tag_names: list[str]) -> list[str]:
    """
    Filtering out 'del' as it is already reserved in python.
    Other reserved keywords shall also be replaced once made apparent.
    """
    reserved = ('del')
    return [tag_name for tag_name in tag_names if tag_name not in reserved]


def write_tag_functions(tag_names: list[str]):
    
    # Declare tag_name = tag('tag_name') for every W3C HTML5 tag
    tag_funcs = [
        f"{tag_name} = tag('{tag_name}')\n" for tag_name in tag_names
    ]
    
    # Add padding to the file for readability, and import tag function
    tag_funcs.insert(0, "\n")
    tag_funcs.insert(1, "from .tags import tag\n")
    tag_funcs.append("\n")

    # Write the lines to ketza/_elements.py
    with open("ketza/_elements.py", "w") as elements:
        elements.writelines(tag_funcs)


def main():
    
    w3c_document = load_html() 
    w3c_soup = BeautifulSoup(w3c_document, "html.parser")
    tag_names = retrieve_tag_names(w3c_soup)
    write_tag_functions(
        clean_tag_names(
            tag_names
        )
    )


__name__ =="__main__" and main()

