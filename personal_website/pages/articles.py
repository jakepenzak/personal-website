"""The articles page."""
import reflex as rx

from assets import asset_data
from assets.asset_data import articles_meta_dict
from personal_website.styles import ARTICLES_PAGE
from personal_website.templates import template
from personal_website.utilities.markdown import read_markdown
from personal_website.utilities.container import container


# Create the articles page
@template(route="/articles", title="Articles")
def articles() -> rx.Component:
    """The articles page.

    Returns:
        The UI for the articles page.
    """
    return rx.chakra.vstack(
        header(),
        rx.chakra.divider(width="80vh"),
        body(),
        rx.chakra.center(
            rx.chakra.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")
        ),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )


## Header Section
def header() -> rx.Component:
    """
    The header section of the articles page.

    Returns:
        rx.Component: The header section of the articles page.
    """

    heading = rx.chakra.heading(
        """
        Articles
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
        Articles
        """,
        font_size="2.75em",
        font_family="HackBold",
        text_align="center",
        color=["#522181"],
        padding_bottom="0.5em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    markdown_content = rx.chakra.box(
        rx.chakra.vstack(
            read_markdown(
                asset_data.ARTICLES_INTRO,
                component_map=ARTICLES_PAGE["MARKDOWN_STYLE_INTRO"],
            ),
        ),
        width="100%",
        padding_x="12em",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )

    markdown_content_mobile = rx.chakra.box(
        rx.chakra.vstack(
            read_markdown(
                asset_data.ARTICLES_INTRO,
                component_map=ARTICLES_PAGE["MARKDOWN_STYLE_INTRO"],
            ),
        ),
        width="100%",
        padding_x="6em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    header = rx.chakra.box(
        container(**ARTICLES_PAGE["HEADER_CONTAINER_STYLE"]),
        rx.chakra.vstack(
            heading, heading_mobile, markdown_content, markdown_content_mobile
        ),
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
            columns="3", display=["None", "None", "None", "flex", "flex", "flex"]
        ),
        create_article_grid(
            columns="1", display=["flex", "flex", "flex", "None", "None", "None"]
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
                rx.image(src=img_src, max_height="25em", width="100%"),
                direction="column",
                align="center",
                justify="center",
                width="100%",
            ),
            read_markdown(
                title_src,
                component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK_HEADER"],
                height="100%",
                width="100%",
            ),
            read_markdown(
                descr_src,
                component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK_BODY"],
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
        container(**ARTICLES_PAGE["BODY_CONTAINER_STYLE"]),
        rx.grid(
            *[
                image_link_description(
                    articles_meta_dict[article].img_src,
                    articles_meta_dict[article].href,
                    articles_meta_dict[article].title_src,
                    articles_meta_dict[article].descr_src,
                )
                for article in list(articles_meta_dict.keys())
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
