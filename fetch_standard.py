from httpx import get 
from logging import exception


STANDARD_URL = "https://html.spec.whatwg.org/multipage/indices.html"


def get_standard(url: str) -> str:
    return get(url).text 


def save_html(html: str):
    with open("HTML_living_standard.html", "w") as standard:
        standard.write(html)


def main():
    standard = get_standard(STANDARD_URL)
    save_html(standard)


__name__ == "__main__" and main()

