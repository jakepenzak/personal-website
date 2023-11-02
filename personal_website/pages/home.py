"""The home page of the app."""

from personal_website import styles
from personal_website.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg") 
def home() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    header = rx.heading(
    """
    Jacob Pieniazek
    """,
    color=["purple", "green", "purple", "green", "purple"],
    )

    with open("assets/intro.md", encoding="utf-8") as intro:
        content = intro.read()

    body = rx.markdown(content, component_map=styles.markdown_style) 
    
    page_content = rx.vstack(
        header,
        body
        )

    return page_content
