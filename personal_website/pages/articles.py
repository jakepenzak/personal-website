"""The articles page."""
import reflex as rx

from assets import asset_data
from personal_website.structural import styles
from personal_website.structural import template
from personal_website.components.utilities.markdown import read_markdown
from personal_website.components.utilities.container import container
from personal_website.components.utilities.header import create_heading
from personal_website.components.utilities.page_vstack import page_vstack


# Create the articles page
@template(route="/articles", title="Articles")
def articles() -> rx.Component:
    """The articles page.

    Returns:
        The UI for the articles page.
    """
    return page_vstack(
        header(),
        rx.chakra.divider(width="80vh"),
        body(),
        rx.chakra.center(
            rx.chakra.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")
        ),
    )


## Header Section
def header() -> rx.Component:
    """
    The header section of the articles page.

    Returns:
        rx.Component: The header section of the articles page.
    """

    heading = create_heading("Articles")
    heading_mobile = create_heading(
        "Articles",
        font_size="2.75em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    markdown_content = rx.chakra.box(
        rx.chakra.vstack(
            read_markdown(
                asset_data.ARTICLES_INTRO,
                component_map=styles.ARTICLES_PAGE["MARKDOWN_STYLE_INTRO"],
            ),
        ),
        width="100%",
        padding_x="6em",
    )

    header = rx.chakra.box(
        container(**styles.ARTICLES_PAGE["HEADER_CONTAINER_STYLE"]),
        rx.chakra.vstack(heading, heading_mobile, markdown_content),
    )

    return header


## Body Section
def body() -> rx.Component:
    """
    Returns the body component for the articles page.

    Returns:
        rx.Component: The body component for the articles page.
    """

    article_grid = rx.chakra.box(
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

    article_grid = rx.container(
        container(**styles.ARTICLES_PAGE["BODY_CONTAINER_STYLE"]),
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
        padding_x="2em",
    )

    return article_grid
