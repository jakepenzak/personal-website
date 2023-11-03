"""The research page."""

from personal_website.templates import template

import reflex as rx


@template(route="/research", title="Research")
def research() -> rx.Component:
    """The research page.

    Returns:
        The UI for the research page.
    """
    return rx.vstack(
        rx.heading("research", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/research.py"),
        ),
    )
