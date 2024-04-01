"""The research page."""
import reflex as rx

from personal_website.structural import styles
from personal_website.structural import template
from personal_website.components.utilities.markdown import read_markdown
from personal_website.components.utilities.container import container
from personal_website.components.utilities.header import create_heading
from personal_website.components.utilities.page_vstack import page_vstack
from assets import asset_data


# Create the research page
@template(route="/research", title="Research")
def research() -> rx.Component:
    """The research page.

    Returns:
        rx.Component: The UI for the research page.
    """
    return page_vstack(
        header(),
        rx.chakra.divider(width="80vh"),
        body(),
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")
            ),
            padding_top="5em",
        ),
    )


## Header Section
def header() -> rx.Component:
    """
    Returns the heading component for the research page.

    Returns:
        rx.Component: The heading component.
    """

    heading_txt = "Research"

    heading = create_heading(heading_txt)
    heading_mobile = create_heading(
        heading_txt,
        font_size="2.5em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.chakra.box(
        container(**styles.RESEARCH_PAGE["HEADER_CONTAINER_STYLE"]),
        heading,
        heading_mobile,
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
        read_markdown(asset_data.THESIS_TITLE),
        href=asset_data.THESIS_LINK,
        _as="thesis_pieniazek.pdf",
        is_external=True,
    )

    p2 = read_markdown(asset_data.CAPSTONE_TITLE)

    body = rx.chakra.box(
        container(**styles.RESEARCH_PAGE["BODY_CONTAINER_STYLE"]),
        rx.chakra.vstack(p1, p2, spacing="3em", text_align="left"),
        padding_x="2em",
    )

    return body
