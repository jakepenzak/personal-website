"""The projects page."""
import reflex as rx

from personal_website.structural import styles
from personal_website.structural import template
from personal_website.components.utilities.container import container
from personal_website.components.utilities.header import create_heading
from personal_website.components.utilities.page_vstack import page_vstack
from assets import asset_data


# Create the projects page
@template(route="/projects", title="Projects")
def projects() -> rx.Component:
    """
    The projects page.

    Returns:
        rx.Component: The UI for the projects page.
    """
    return page_vstack(
        header(),
        rx.chakra.divider(width="80vh"),
        rx.chakra.text(
            "Under construction...",
            font_size="flex",
            padding_y="2em",
            font_family="Hack",
            text_align="center",
            width="100%",
        ),
        rx.chakra.center(
            rx.chakra.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")
        ),
    )


## Header Section
def header():
    heading = create_heading("Projects")
    heading_mobile = create_heading(
        "Projects",
        font_size="2.75em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.chakra.box(
        container(**styles.PROJECTS_PAGE["HEADER_CONTAINER_STYLE"]),
        heading,
        heading_mobile,
    )

    return header
