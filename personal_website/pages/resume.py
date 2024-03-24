"""The resume page."""
import reflex as rx

from personal_website.styles import RESUME_PAGE
from personal_website.templates import template


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )


## Resume Page Heading
def heading():
    """The heading section of the resume page."""

    heading = rx.chakra.heading(
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

    heading_mobile = rx.chakra.heading(
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

    header = rx.chakra.box(
        container(**RESUME_PAGE["HEADER_CONTAINER_STYLE"]), heading, heading_mobile
    )

    return header


## Resume Body
def body():
    """The body section of the resume page."""

    # Resume
    resume = rx.chakra.link(
        rx.chakra.center(
            rx.chakra.image(
                src="/resume/resume.jpg",
                border_radius="15px 50px",
                border="3px solid #555",
            )
        ),
        href="/resume/resume.pdf",
        is_external=True,
        padding_top="0.5em",
        padding_bottom="2em",
        padding_x="2em",
        max_width="80vh",
    )

    return resume


@template(route="/resume", title="Professional Resume")
def resume() -> rx.Component:
    """The resume page.

    Returns:
        The UI for the resume page.
    """
    return rx.chakra.vstack(
        heading(),
        rx.chakra.divider(width="80vh"),
        body(),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )
