"""The research page."""

from personal_website.styles import RESEARCH_PAGE
from personal_website.templates import template
from personal_website.components.spline import spline_component_404

import reflex as rx


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.container(
        *children,
        **kwargs,
    )


## Research Header
def heading():
    """The heading section of the resume page."""

    heading = rx.heading(
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

    heading_mobile = rx.heading(
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

    header = rx.box(container(**RESEARCH_PAGE["header_container_style"]), heading, heading_mobile)

    return header


## Research Body
def body():
    """The body section of the articles page."""

    p1 = rx.link(
        rx.markdown(
            "[1] High, But Not Happy? The Impact of Cannabis Consumption on Mental Health [2022 - Master's Thesis]",
            text_align="left",
        ),
        href="/documents/thesis.pdf",
        _as="thesis_pieniazek.pdf",
        is_external=True,
    )

    p2 = rx.markdown(
        "[2] Particule Happiness: How Air Pollution is Effecting Our Mental Health [2021 - Undergraduate Thesis]",
        text_align="left",
    )

    body = rx.box(
        container(**RESEARCH_PAGE["body_container_style"]),
        rx.vstack(p1, p2, spacing="3em", text_align="left"),
        padding_x="2em",
    )

    return body


@template(route="/research", title="Research")
def research() -> rx.Component:
    """The research page.

    Returns:
        The UI for the research page.
    """
    return rx.vstack(
        heading(),
        rx.divider(width="80vh"),
        body(),
        rx.desktop_only(rx.box(
            rx.center(spline_component_404()), padding_bottom="5em", padding_top="5em"
        )),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )
