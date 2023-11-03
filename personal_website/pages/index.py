"""The home page of the app."""

from personal_website import styles
from personal_website.templates import template
from personal_website.components.spline import spline_component

import reflex as rx


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.container(
        *children,
        **kwargs,
    )


## Header
header = container(
    rx.hstack(
        rx.center(
            rx.heading(
                """
                Jacob \n
                Pieniazek
                """,
                font_size="6em",
                font_family="HackBold",
                color=["#522181"],
            )
        ),
        spline_component(),
    ),
    **styles.header_container_style,
)


## Introduction
def intro():
    """The introduction section of the home page."""

    ## Body
    welcome = rx.heading(
        """
        Welcome!
        """,
        font_size="2em",
        font_family="HackBold",
        text_align="center",
    )

    with open("assets/intro.md", encoding="utf-8") as intro:
        content = intro.read()

    markdown_content = rx.vstack(
        rx.markdown(content, component_map=styles.markdown_style)
    )

    intro = rx.box(
        container(**styles.intro_container_style),
        rx.hstack(
            rx.image(src="/self.jpg", height="35em", width="30em"),
            rx.vstack(welcome, markdown_content),
        ),
        width="100%"
    )

    return intro


@template(route="/", title="Index")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    return rx.box(header, intro(), width="100%",  **styles.index_page_style)