"""The home page of the app."""

from personal_website import styles
from personal_website.templates import template
from personal_website.components.spline import spline_component_index_page

import reflex as rx


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.container(
        *children,
        **kwargs,
    )


## Header
def header():
    """The header section of the home page."""

    heading = container(
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
            spline_component_index_page(),
            display=["none", "none", "none", "flex", "flex", "flex"],
        ),
        rx.center(
            rx.heading(
                """
                    Jacob \n
                    Pieniazek
                    """,
                font_size="6em",
                font_family="HackBold",
                color=["#522181"],
                text_align="center",
            ),
            display=["flex", "flex", "flex", "none", "none", "none"],
        ),
        **styles.header_container_style,
    )

    return heading


## Introduction
def intro():
    """The introduction section of the home page."""

    welcome = rx.heading(
        """
        Welcome!
        """,
        font_size="2em",
        font_family="HackBold",
        text_align="center",
        padding_top="1em",
    )

    with open("assets/text/index_intro.md", encoding="utf-8") as intro:
        content = intro.read()

    markdown_content = rx.box(
        rx.vstack(
            rx.markdown(content, component_map=styles.markdown_style),
        ),
    )

    intro = rx.box(
        container(**styles.intro_container_style),
        rx.center(
            rx.hstack(
                rx.image(src="/self.jpg", height="35em", width="35em"),
                rx.vstack(welcome, markdown_content, padding_left="12em"),
                padding_x="5em",
                display=["none", "none", "none", "none", "none", "flex"],
            ),
            rx.hstack(
                rx.image(src="/self.jpg", height="35em", width="35em"),
                rx.vstack(welcome, markdown_content, padding_left="6em"),
                padding_x="5em",
                display=["none", "none", "none", "flex", "flex", "none"],
            ),
            rx.vstack(
                rx.image(src="/self.jpg", height="75%", width="75%"),
                rx.vstack(welcome, markdown_content),
                padding_x="5em",
                display=["flex", "flex", "flex", "none", "none", "none"],
            ),
        ),
    )

    return intro


@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    return rx.box(header(), intro(), width="100%", **styles.index_page_style)
