"""The home page of the app."""

import reflex as rx

from personal_website.components.spline import spline_component_index_page
from personal_website.styles import INDEX_PAGE
from personal_website.templates import template
from personal_website.utilities.markdown import read_markdown


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
                font_size="4em",
                font_family="HackBold",
                color=["#522181"],
                text_align="center",
            ),
            display=["flex", "flex", "flex", "none", "none", "none"],
        ),
        **INDEX_PAGE["HEADER_CONTAINER_STYLE"],
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

    body = rx.box(
        rx.vstack(
            read_markdown(
                "assets/index/index_intro.md",
                component_map=INDEX_PAGE["MARKDOWN_STYLE"],
            ),
        ),
    )

    intro = rx.box(
        container(**INDEX_PAGE["INTRO_CONTAINER_STYLE"]),
        rx.center(
            rx.hstack(
                rx.image(src="/index/self.jpg", height="35em", width="35em"),
                rx.vstack(welcome, body, padding_left="12em"),
                padding_x="5em",
                display=["none", "none", "none", "none", "none", "flex"],
            ),
            rx.hstack(
                rx.image(src="/index/self.jpg", height="35em", width="35em"),
                rx.vstack(welcome, body, padding_left="6em"),
                padding_x="5em",
                display=["none", "none", "none", "flex", "flex", "none"],
            ),
            rx.vstack(
                rx.image(src="/index/self.jpg", height="50%", width="50%"),
                rx.vstack(welcome, body),
                padding_x="3em",
                display=["none", "none", "flex", "none", "none", "none"],
            ),
            rx.vstack(
                rx.image(src="/index/self.jpg", height="75%", width="75%"),
                rx.vstack(welcome, body),
                padding_x="3em",
                display=["none", "flex", "none", "none", "none", "none"],
            ),
            rx.vstack(
                rx.image(src="/index/self.jpg", height="flex", width="flex"),
                rx.vstack(welcome, body),
                padding_x="3em",
                display=["flex", "none", "none", "none", "none", "none"],
            ),
        ),
    )

    return intro


# def skills():
#     skills = rx.box(
#         container(**INDEX_PAGE["INTRO_CONTAINER_STYLE"])
#     )

#     return skills


@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    return rx.box(
        header(),
        intro(),
        # skills(),
        width="100%",
        max_width="100%",
        overflow_x="hidden",
        **INDEX_PAGE["INDEX_PAGE_STYLE"],
    )
