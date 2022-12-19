# Ketza
## HTML defined in python!

---

## Rationale

With this project I want to create a toolset for defining reusable pieces
of html; I'm looking to build something centered around doing so at the 
component level rather than the page level, providing an alternative to html
templating engines.

Despite this, I also want to preserve simplicity and flexibility such that
users can find useful and creative ways to integrate ketza with whichever 
other tools they need or desire to.

## A brief illustration with an unordered list

Let's say, for argument's sake, I would like to define a list like tnis:
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

However, notice we're still repeating ourselves a bunch!
But fret not, this is where the ability to define components in python
rather than raw html comes in:

```python
from ketza import ul, li

# Watch! This actually creates a function which will wrap content in a <li>

triplet = li({"class": "list-triplet"})

list_of_three = ul({"id": "list-of-three"})(
    triplet("Foo"),
    triplet("Bar"),
    triplet("Baz")
)

# As you can see, this gives us some power to build reuseable components!

```

## A quick note to end

This readme page is, needless to say, far from comprehensive.
It is my hope to flesh it out and add more examples of what Ketza can do 
especially as I continue to improve it.

Users should also be warned that while the output of ketza functionality
should function the same as the example html, the amount of indentation will
differ as of the time of writing.

I am hoping to further elaborate on giving the option to indent or not, as 
well as including the proper number of tabs (or spaces?) in the output.
