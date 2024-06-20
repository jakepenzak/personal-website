"""The projects page."""
import reflex as rx
from personal_website.structural import template
from assets import asset_data


# Create the projects page
@template(route="/projects", title="Projects")
def projects() -> rx.Component:
    """
    The projects page.

    Returns:
        rx.Component: The UI for the projects page.
    """
    return rx.vstack(
        header(),
        rx.divider(width="25%", border_top="1px solid rgba(0, 0, 0, 0.25)"),
        rx.text(
            "Under construction...",
            font_size="flex",
            padding_y="2em",
            font_family="Hack",
            text_align="center",
            width="100%",
        ),
        rx.spacer(),
        rx.center(rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")),
        align="center",
        min_height="80vh",
    )


## Header Section
def header():
    heading = rx.heading("Projects")
    heading_mobile = rx.heading(
        "Projects",
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
