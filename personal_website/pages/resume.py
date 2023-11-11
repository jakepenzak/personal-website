"""The resume page."""
from personal_website.styles import RESUME_PAGE
from personal_website.templates import template
from personal_website.components.spline import spline_component_404

import reflex as rx


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.container(
        *children,
        **kwargs,
    )


## Resume Page Heading
def heading():
    """The heading section of the resume page."""

    heading = rx.heading(
        """
        Professional Resume
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
        Professional Resume
        """,
        font_size="2.75em",
        font_family="HackBold",
        text_align="center",
        color=["#522181"],
        padding_bottom="0.5em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.box(container(**RESUME_PAGE["header_container_style"]), heading, heading_mobile)

    return header


## Resume Body
def body():
    """The body section of the resume page."""

    # Resume
    resume = rx.link(
        rx.center(
            rx.image(
                src="/documents/resume.png",
                width="100%",
                height="100%",
                border_radius="15px 50px",
                border="3px solid #555",
            )
        ),
        href="/documents/resume.pdf",
        _as="resume_pieniazek.pdf",
        is_external=True,
        padding_top="0.5em",
        padding_bottom="2em",
        padding_x="2em",
    )

    return resume


@template(route="/resume", title="Professional Resume")
def resume() -> rx.Component:
    """The resume page.

    Returns:
        The UI for the resume page.
    """
    return rx.vstack(
        heading(),
        rx.divider(width="80vh"),
        body(),
        position="relative",
        min_height="80vh",
        width="100%",
    )
