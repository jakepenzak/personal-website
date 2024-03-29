"""The research page."""
import reflex as rx

from personal_website.styles import RESEARCH_PAGE
from personal_website.templates import template
from personal_website.utilities.markdown import read_markdown
from personal_website.utilities.container import container


# Create the research page
@template(route="/research", title="Research")
def research() -> rx.Component:
    """The research page.

    Returns:
        rx.Component: The UI for the research page.
    """
    return rx.chakra.vstack(
        header(),
        rx.chakra.divider(width="80vh"),
        body(),
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.image(src="/shared/website_bar.png", width="100%")
            ),
            padding_top="5em",
        ),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )


## Header Section
def header() -> rx.Component:
    """
    Returns the heading component for the research page.

    Returns:
        rx.Component: The heading component.
    """
    heading = rx.chakra.heading(
        """
        Research
        """,
        font_size="4em",
        font_family="HackBold",
        text_align="center",
        color=["#522181"],
        padding_bottom="0.5em",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )

    heading_mobile = rx.chakra.heading(
        """
        Research
        """,
        font_size="2.75em",
        font_family="HackBold",
        text_align="center",
        color=["#522181"],
        padding_bottom="0.5em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.chakra.box(
        container(**RESEARCH_PAGE["HEADER_CONTAINER_STYLE"]), heading, heading_mobile
    )

    return header


## Body Section
def body() -> rx.Component:
    """
    Returns the body component for the research page.

    Returns:
        rx.Component: The body component.
    """
    p1 = rx.chakra.link(
        read_markdown("assets/research/thesis.md"),
        href="/research/thesis.pdf",
        _as="thesis_pieniazek.pdf",
        is_external=True,
    )

    p2 = read_markdown("assets/research/capstone.md")

    body = rx.chakra.box(
        container(**RESEARCH_PAGE["BODY_CONTAINER_STYLE"]),
        rx.chakra.vstack(p1, p2, spacing="3em", text_align="left"),
        padding_x="2em",
    )

    return body
