"""The articles page."""
import reflex as rx

from assets import asset_data
from personal_website.structural import styles
from personal_website.structural import template
from personal_website.components.utilities.markdown import read_markdown


# Create the articles page
@template(route="/articles", title="Articles")
def articles() -> rx.Component:
    """The articles page.

    Returns:
        The UI for the articles page.
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
    The header section of the articles page.

    Returns:
        rx.Component: The header section of the articles page.
    """

    heading = rx.heading("Articles")
    heading_mobile = rx.heading(
        "Articles",
        font_size="2em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    markdown_content = rx.vstack(
            read_markdown(
                asset_data.ARTICLES_INTRO,
                component_map=styles.ARTICLES_PAGE["MARKDOWN_STYLE_INTRO"],
            ),
        width="100%",
        padding_x="2em",
        align="center",
    )

    header = rx.vstack(
        heading,
        heading_mobile,
        markdown_content,
        align="center",
        padding_top="2em",
        padding_x="2em",
        max_height="100vh",
        width="100%",
    )

    return header


## Body Section
def body() -> rx.Component:
    """
    Returns the body component for the articles page.

    Returns:
        rx.Component: The body component for the articles page.
    """

    article_grid = rx.box(
        create_article_grid(
            columns="3", display=["None", "None", "flex", "flex", "flex", "flex"]
        ),
        create_article_grid(
            columns="1", display=["flex", "flex", "None", "None", "None", "None"]
        ),
    )

    return article_grid


def image_link_description(
    img_src: str, href: str, title_src: str, descr_src: str
) -> rx.Component:
    """
    Creates a component that represents an image link with a title and description.

    Args:
        img_src (str): The source URL of the image.
        href (str): The URL that the link should navigate to.
        title_src (str): The source URL of the title content.
        descr_src (str): The source URL of the description content.

    Returns:
        rx.Component: The generated component.
    """
    return rx.link(
        rx.vstack(
            rx.flex(
                rx.image(src=img_src),
                direction="column",
                align="center",
                justify="center",
            ),
            read_markdown(
                title_src,
                component_map=styles.ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK_HEADER"],
                height="100%",
                width="100%",
            ),
            read_markdown(
                descr_src,
                component_map=styles.ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK_BODY"],
                height="100%",
                width="100%",
            ),
        ),
        href=href,
        target="_blank",
    )


def create_article_grid(
    columns: str, display: list = ["flex", "flex", "flex", "flex", "flex", "flex"]
) -> rx.Component:
    """
    Creates a grid of articles with specified number of columns and display style.

    Args:
        columns (str): The number of columns in the grid.
        display (list, optional): The display style. Defaults to ["flex", "flex", "flex", "flex", "flex", "flex"].

    Returns:
        rx.Component: The grid of articles.
    """

    article_grid = rx.box(
        rx.grid(
            *[
                image_link_description(
                    asset_data.ARTICLES_META_DICT[article].img_src,
                    asset_data.ARTICLES_META_DICT[article].href,
                    asset_data.ARTICLES_META_DICT[article].title_src,
                    asset_data.ARTICLES_META_DICT[article].descr_src,
                )
                for article in list(asset_data.ARTICLES_META_DICT.keys())
            ],
            columns=columns,
            spacing="9",
            align="center",
            justify="center",
            padding_y="1em",
            padding_x="2em",
        ),
        display=display,
        padding_top="1em",
        max_width=["80vw", "80vw", "80vw", "60vw", "60vw", "60vw"],
    )

    return article_grid
