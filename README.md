# Ketza - HTML defined in python

### Contents

- [Rationale](#rationale)
- [Basics](#basics) 
- [Example with an unordered list](#example-with-an-unordered-list)
- [Formatting](#formatting)
- [Future Intentions](#future-intentions)

## Rationale

This project provides a framework for defining reusable units of HTML in
python code, as opposed to being a runtime or a templating engine.

My intention is to provide a powerful but simple interface, allowing for 
extensibility and interplay with other technologies without headaches.

## Basics

At the core of Ketza is the `tag` function, which allows you to build a 
html element in a series of function calls as follows:
```python
from ketza import tag

main = tag("main") # Apply element name

app = main({"id": "app"}) # Apply attributes as key-value pairs

hello_world = app("Hello World!") # Apply inner string content

# hello_world is now equal to `<main id="app">Hello World!</main>`
```

However, Ketza also provides pre-defined named tags for recognised 
HTML elements based on the WHATWG living standard.
A further example is presented below, making use of predefined tags.

## Example with an unordered list

Let's say, for argument's sake, I would like to define a list like this:
```html
<ul id="list-of-three">
    <li class="list-triplet">
        Foo
    </li>
    <li class="list-triplet">
        Bar
    </li>
    <li class="list-triplet">
        Baz
    </li>
</ul>
```

This can be done as follows:
```python
from ketza import ul, li

list_of_three = ul({"id": "list-of-three"})(
    li({"class": "list-triplet"})(
        "Foo"
    ),
    li({"class": "list-triplet"})(
        "Bar"
    ),
    li({"class": "list-triplet"})(
        "Baz"
    ),
)
```

However, we can simplify this even further:
```python
from ketza import ul, li

triplet = li({"class": "list-triplet"})

list_of_three = ul({"id": "list-of-three"})(
    triplet("Foo"),
    triplet("Bar"),
    triplet("Baz")
)
```

For our purposes, this yields html which is functionally equivalent to our
intended `list-of-three`. Even so, the raw html will look more like this:

```html
<ul id="list-of-three"><li class="list-triplet">Foo</li><li class=.... 
```

While this does essentially result in pre-minified HTML output, there are 
situations which call for human-readable raw HTML. As such, the following
section shall briefly touch on formatting.

## Formatting

Ketza provides a utility function for indenting minified html:
```python
from ketza.formatters import indent 

list_of_three = indent(list_of_three)
```

The `indent` function turns this:
```html
<ul id="list-of-three"><li class="list-triplet">Foo</li><li class=.... 
```

Into this!
```html
<ul id="list-of-three">
    <li class="list-triplet">
        Foo
    </li>
    <li class="list-triplet">
        Bar
    </li>
    <li class="list-triplet">
        Baz
    </li>
</ul>
```

## Future Intentions

Though I am confident that Ketza provides the means to define 
components representing common HTML boilerplate, I am also considering
defining utilities to further streamline HTML boilerplate creation.

I am also open to feedback for how I can improve and 
extend Ketza, as well as its interoperability with other web technologies.

