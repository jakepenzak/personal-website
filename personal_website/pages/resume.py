"""The resume page."""
from personal_website.styles import resume_page
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
        padding_bottom="0.5em"
    )

    header = rx.box(
        container(**resume_page['header_container_style']),
            heading
            )
    
    return header

## Resume Body
def body():
    """The body section of the resume page."""

    # Resume 
    # resume = rx.link(
    resume=rx.image(src="/documents/resume.png") 

                    # href="/assets/documents/Resume-JacobPieniazek.pdf"
                    # )
    
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
        rx.box(rx.center(spline_component_404()), padding_bottom="5em"),
        position="relative", 
        min_height="80vh",
        width="100%"
    )
