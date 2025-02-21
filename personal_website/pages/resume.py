"""The resume page."""

import reflex as rx

from personal_website.structural import template
from assets import asset_data


# Create the resume page
@template(route="/resume", title="Professional Resume")
def resume() -> rx.Component:
    """The resume page.

    Returns:
        rx.Component: The UI for the resume page.
    """
    return rx.vstack(
        heading(),
        rx.divider(width="25%", border_top="1px solid rgba(0, 0, 0, 0.25)"),
        body(),
        rx.spacer(),
        rx.center(rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")),
        align="center",
        min_height="80vh",
    )


## Header Section
def heading() -> rx.Component:
    """The heading section of the resume page."""

    heading = rx.heading("Professional Resume")
    heading_mobile = rx.heading(
        "Professional Resume",
        font_size="2em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.vstack(
        heading,
        heading_mobile,
        align_items="center",
        padding_top="2em",
        padding_x="2em",
        max_height="100vh",
    )

    return header


## Resume Body
def body() -> rx.Component:
    """The body section of the resume page."""

    # Resume
    resume = rx.box(
        rx.link(
            rx.image(
                src=asset_data.RESUME_IMAGE,
                border_radius="15px 50px",
                border="3px solid #555",
            ),
            href=asset_data.RESUME_LINK,
            is_external=True,
        ),
        padding_top="0.5em",
        padding_bottom="2em",
        padding_x="2em",
        max_width="45em",
        max_height="70em",
        align="center",
    )

    return rx.box(resume)
