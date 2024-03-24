"""The projects page."""

import reflex as rx

from personal_website.styles import PROJECTS_PAGE
from personal_website.templates import template


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )


## Projects Page Heading
def header():
    heading = rx.chakra.heading(
        "Projects",
        font_size="4em",
        font_family="HackBold",
        text_align="center",
        color=["#522181"],
        padding_bottom="0.5em",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )

    heading_mobile = rx.chakra.heading(
        "Projects",
        font_size="2.75em",
        font_family="HackBold",
        text_align="center",
        color=["#522181"],
        padding_bottom="0.5em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.chakra.box(
        container(**PROJECTS_PAGE["HEADER_CONTAINER_STYLE"]), heading, heading_mobile
    )

    return header


@template(route="/projects", title="Projects")
def projects() -> rx.Component:
    """The projects page.

    Returns:
        The UI for the projects page.
    """
    return rx.chakra.vstack(
        header(),
        rx.chakra.divider(width="80vh"),
        rx.chakra.text(
            "Under construction...",
            font_size="flex",
            padding_y="2em",
            font_family="Hack",
            text_align="center",
            width="100%",
        ),
        rx.chakra.center(rx.chakra.image(src="/shared/website_bar.png", width="100%")),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )
