"""The projects page."""

from personal_website.styles import PROJECTS_PAGE
from personal_website.templates import template
from personal_website.components.spline import spline_component_404

import reflex as rx


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.container(
        *children,
        **kwargs,
    )


## Projects Page Heading
def header():
    heading = rx.heading(
        "Projects",
        font_size="4em",
        font_family="HackBold",
        text_align="center",
        color=["#522181"],
        padding_bottom="0.5em",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )

    heading_mobile = rx.heading(
        "Projects",
        font_size="2.75em",
        font_family="HackBold",
        text_align="center",
        color=["#522181"],
        padding_bottom="0.5em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.box(
        container(**PROJECTS_PAGE["header_container_style"]), heading, heading_mobile
    )

    return header


@template(route="/projects", title="Projects")
def projects() -> rx.Component:
    """The projects page.

    Returns:
        The UI for the projects page.
    """
    return rx.vstack(
        header(),
        rx.divider(width="80vh"),
        rx.text(
            "Under construction...",
            font_size="flex",
            padding_y="2em",
            font_family="Hack",
            text_align="center",
            width="100%",
        ),
        rx.center(rx.image(src="/website_bar.png", width="100%")),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )
