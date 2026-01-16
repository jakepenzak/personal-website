"""The articles page."""

import reflex as rx

from assets import asset_data
from personal_website.components.utilities.markdown import read_markdown
from personal_website.structural import styles, template


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
        rx.spacer(),
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

    markdown_content = rx.vstack(
        read_markdown(
            asset_data.ARTICLES_INTRO,
            component_map=styles.ARTICLES_PAGE["MARKDOWN_STYLE_INTRO"],
        ),
        width=["90%", "80%", "60%", "50%", "50%", "50%"],
        padding_x="1em",
        align="center",
    )

    return rx.vstack(
        heading,
        markdown_content,
        align="center",
        padding_top=["1em", "1em", "2em", "2em", "2em", "2em"],
        padding_x=["1em", "1em", "2em", "2em", "2em", "2em"],
        max_height="100vh",
        width="100%",
    )


## Body Section
def body() -> rx.Component:
    """
    Returns the body component for the articles page.

    Returns:
        rx.Component: The body component for the articles page.
    """
    return rx.vstack(
        featured_articles(),
        rx.divider(
            width="80%",
            margin_y="3em",
        ),
        all_articles(),
        align="center",
        spacing="6",
        max_width="1400px",
        margin="0 auto",
        padding_x="2em",
    )


def get_badge_config(category: str) -> dict:
    """Get badge configuration for article categories."""
    return asset_data.article_badge_config.get(
        category, {"color_scheme": "gray", "variant": "soft"}
    )


def create_article_card(
    article_key: str, article_meta: asset_data.ArticleMeta, is_featured: bool = False
) -> rx.Component:
    """Create an enhanced article card with category and difficulty badges."""

    category = article_meta.category
    types = article_meta.types

    # Badge section
    badges = rx.hstack(
        rx.badge(category, **get_badge_config(category)),
        *[rx.badge(type, **get_badge_config(type)) for type in types],
        spacing="2",
        justify="start",
        width="100%",
    )

    # Article content
    image_section_height = "200px" if is_featured else "170px"

    image_section = rx.box(
        rx.image(
            src=article_meta.img_src,
            height="100%",
            width="100%",
            object_fit="cover",
            border_radius="md",
        ),
        height=image_section_height,
        width="100%",
        padding="1em",
    )

    header_section = rx.vstack(
        rx.center(badges),
        rx.text(
            article_meta.title_str,
            size="5" if is_featured else "4",
            color="#522181",
            text_align="center",
            line_height="1.3",
            font_weight="600",
        ),
        spacing="3",
        align="center",
        width="100%",
        min_height="96px" if is_featured else "84px",
        justify="center",
    )

    body_section = rx.box(
        read_markdown(
            article_meta.descr_src,
            component_map=styles.ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK_BODY"],
            font_size=["0.8em", "0.85em", "0.9em"]
            if is_featured
            else ["0.7em", "0.75em", "0.8em"],
        ),
        width="100%",
        height="170px" if is_featured else "150px",
        overflow="hidden",
    )

    footer_section = rx.box(
        rx.button(
            "Read Article",
            variant="soft",
            size="2",
            color_scheme="purple",
            width="fit-content",
        ),
        width="100%",
        min_height="52px",
        display="flex",
        justify_content="center",
        align_items="center",
    )

    content = rx.vstack(
        image_section,
        header_section,
        body_section,
        footer_section,
        spacing="3",
        align="center",
        width="100%",
        height="100%",
    )

    card_props = {
        "padding": "1.5em",
        "border": "1px solid #e2e8f0",
        "border_radius": "lg",
        "_hover": {
            "transform": "translateY(-4px)",
            "box_shadow": "xl" if is_featured else "lg",
            "border_color": "#522181",
        },
        "transition": "all 0.3s ease",
        "align": "center",
        "cursor": "pointer",
        # Ensure consistent sizing within grid layouts.
        "width": "100%",
        "height": "100%",
    }

    if is_featured:
        card_props.update(
            {"max_width": "400px", "min_height": "500px", "box_shadow": "md"}
        )
    else:
        card_props.update({"max_width": "350px", "min_height": "450px"})

    return rx.link(
        rx.card(content, **card_props),
        href=article_meta.href,
        text_decoration="none",
        _hover={"text_decoration": "none"},
    )


def featured_articles() -> rx.Component:
    """Display featured articles section."""

    # Featured article keys (most recent or important)
    featured_keys = ["dml2", "dml1", "tsne"]

    title = rx.heading(
        "Featured Articles",
        font_size=rx.breakpoints(initial="1.5em", md="1.8em"),
    )

    description = rx.text(
        "Highlighted pieces covering advanced topics in machine learning, optimization, and statistical methods.",
        text_align="center",
        color="gray.600",
        max_width="600px",
        padding_bottom="1em",
    )

    featured_grid = rx.box(
        rx.grid(
            *[
                create_article_card(
                    key, asset_data.ARTICLES_META_DICT[key], is_featured=True
                )
                for key in featured_keys
                if key in asset_data.ARTICLES_META_DICT
            ],
            columns=rx.breakpoints(initial="1", sm="2", lg="3"),
            spacing="6",
            width="100%",
            justify="center",
        )
    )

    return rx.vstack(
        title,
        description,
        featured_grid,
        align="center",
        spacing="6",
        width="100%",
    )


def all_articles() -> rx.Component:
    """Display all articles organized by category."""

    title = rx.heading(
        "All Articles",
        font_size=rx.breakpoints(initial="1.5em", md="1.8em"),
    )

    description = rx.text(
        "Complete collection of technical articles and tutorials covering various topics in data science and econometrics.",
        text_align="center",
        color="gray.600",
        max_width="600px",
        padding_bottom="1em",
    )

    # Group articles by category
    articles_by_category = {}
    for key, meta in asset_data.ARTICLES_META_DICT.items():
        category = meta.category
        if category not in articles_by_category:
            articles_by_category[category] = []
        articles_by_category[category].append((key, meta))

    # Create sections for each category
    category_sections = []
    for category, articles in articles_by_category.items():
        config = get_badge_config(category)

        category_header = rx.hstack(
            rx.badge(category, **config, size="3"),
            rx.text(f"({len(articles)} articles)", size="2", color="gray.500"),
            spacing="2",
            align="center",
            justify="center",
            margin_bottom="1em",
        )

        articles_grid = rx.grid(
            *[
                create_article_card(key, meta, is_featured=False)
                for key, meta in articles
            ],
            columns=rx.breakpoints(initial="1", sm="2", lg="3", xl="4"),
            spacing="5",
            width="100%",
            justify="center",
        )

        category_sections.append(
            rx.center(
                rx.vstack(
                    category_header,
                    articles_grid,
                    spacing="4",
                    align="center",
                    width="100%",
                    margin_bottom="2em",
                )
            )
        )

    return rx.center(
        rx.vstack(
            title,
            description,
            *category_sections,
            align="center",
            spacing="6",
            width="100%",
        )
    )
