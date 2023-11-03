"""The articles page."""
from personal_website.templates import template

import reflex as rx


@template(route="/articles", title="Articles")
def articles() -> rx.Component:
    """The articles page.

    Returns:
        The UI for the articles page.
    """
    return rx.vstack(
        rx.heading("Articles", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/articles.py"),
        ),
    )
