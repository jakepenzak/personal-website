"""The projects page."""

from personal_website.templates import template

import reflex as rx


@template(route="/projects", title="Projects")
def projects() -> rx.Component:
    """The projects page.

    Returns:
        The UI for the projects page.
    """
    return rx.vstack(
        rx.heading("projects", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/projects.py"),
        ),
    )
