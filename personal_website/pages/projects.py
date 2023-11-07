"""The projects page."""

from personal_website.templates import template
from personal_website.components.spline import spline_component_404

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
        rx.center(spline_component_404()),
        position="relative", 
        min_height="80vh",
        width="100%"
    )
