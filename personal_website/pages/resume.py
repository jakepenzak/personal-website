"""The resume page."""
import reflex as rx

from personal_website.structural import styles
from personal_website.structural import template
from personal_website.components.utilities.container import container
from personal_website.components.utilities.header import create_heading
from personal_website.components.utilities.page_vstack import page_vstack
from assets import asset_data


# Create the resume page
@template(route="/resume", title="Professional Resume")
def resume() -> rx.Component:
    """The resume page.

    Returns:
        rx.Component: The UI for the resume page.
    """
    return page_vstack(
        heading(),
        rx.chakra.divider(width="80vh"),
        body(),
    )


## Header Section
def heading() -> rx.Component:
    """The heading section of the resume page."""

    heading = create_heading("Professional Resume")
    heading_mobile = create_heading(
        "Professional Resume",
        font_size="2.75em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.chakra.box(
        container(**styles.RESUME_PAGE["HEADER_CONTAINER_STYLE"]),
        heading,
        heading_mobile,
    )

    return header


## Resume Body
def body() -> rx.Component:
    """The body section of the resume page."""

    # Resume
    resume = rx.chakra.link(
        rx.chakra.center(
            rx.chakra.image(
                src=asset_data.RESUME_IMAGE,
                border_radius="15px 50px",
                border="3px solid #555",
            )
        ),
        href=asset_data.RESUME_LINK,
        is_external=True,
        padding_top="0.5em",
        padding_bottom="2em",
        padding_x="2em",
        max_width="80vh",
    )

    return resume
