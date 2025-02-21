"""The research page."""

import reflex as rx

from personal_website.structural import template
from personal_website.components.utilities.markdown import read_markdown
from assets import asset_data


# Create the research page
@template(route="/research", title="Research")
def research() -> rx.Component:
    """The research page.

    Returns:
        rx.Component: The UI for the research page.
    """
    return rx.vstack(
        header(),
        rx.divider(width="25%", border_top="1px solid rgba(0, 0, 0, 0.25)"),
        body(),
        rx.spacer(),
        rx.center(rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")),
        align="center",
        min_height="80vh",
    )


## Header Section
def header() -> rx.Component:
    """
    Returns the heading component for the research page.

    Returns:
        rx.Component: The heading component.
    """

    heading_txt = "Research"

    heading = rx.heading(heading_txt)
    heading_mobile = rx.heading(
        heading_txt,
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


## Body Section
def body() -> rx.Component:
    """
    Returns the body component for the research page.

    Returns:
        rx.Component: The body component.
    """
    p1 = rx.link(
        read_markdown(asset_data.THESIS_TITLE),
        href=asset_data.THESIS_LINK,
        _as="thesis_pieniazek.pdf",
        is_external=True,
        color="black",
    )

    p2 = read_markdown(asset_data.CAPSTONE_TITLE)

    body = rx.box(
        rx.vstack(p1, p2, spacing="3", text_align="left"),
        padding_x="2em",
    )

    return body
