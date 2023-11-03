"""The resume page."""

from personal_website.templates import template

import reflex as rx


@template(route="/resume", title="Professional Resume")
def resume() -> rx.Component:
    """The resume page.

    Returns:
        The UI for the resume page.
    """
    return rx.vstack(
        rx.heading("resume", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/resume.py"),
        ),
    )
