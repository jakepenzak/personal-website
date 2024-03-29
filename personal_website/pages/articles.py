"""The articles page."""
import reflex as rx

from assets import asset_data
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
        rx.chakra.center(rx.chakra.image(src="/shared/website_bar.png", width="100%")),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )


## Header Section
def header():
    """The introduction section of the articles page."""

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
                "assets/articles/intro.md",
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
                "assets/articles/intro.md",
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
def body():
    """The body section of the articles page."""

    # Blocks
    fwl = rx.chakra.link(
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.vstack(
                    rx.chakra.image(
                        src="/articles/fwl/cover.png",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    read_markdown(
                        "assets/articles/fwl/title.md",
                        component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK"],
                    ),
                    read_markdown("assets/articles/fwl/description.md"),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href=asset_data.FWL_URL,
        is_external=True,
    )

    logistic = rx.chakra.link(
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.vstack(
                    rx.chakra.image(
                        src="/articles/logistic/cover.png",
                        height="100%",
                        width="100%",
                        max_width="35em",
                        max_height="35em",
                    ),
                    read_markdown(
                        "assets/articles/logistic/title.md",
                        component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK"],
                    ),
                    read_markdown("assets/articles/logistic/description.md"),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href=asset_data.LOGISTIC_URL,
        is_external=True,
    )

    nm1 = rx.chakra.link(
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.vstack(
                    rx.chakra.image(
                        src="/articles/nm1/cover.gif",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    read_markdown(
                        "assets/articles/nm1/title.md",
                        component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK"],
                    ),
                    read_markdown("assets/articles/nm1/description.md"),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href=asset_data.NM1_URL,
        is_external=True,
    )

    nm2 = rx.chakra.link(
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.vstack(
                    rx.chakra.image(
                        src="/articles/nm2/cover.jpeg",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    read_markdown(
                        "assets/articles/nm2/title.md",
                        component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK"],
                    ),
                    read_markdown("assets/articles/nm2/description.md"),
                )
            ),
            # padding_x="3em", MIDDLE COLUMN
            padding_bottom="3em",
        ),
        href=asset_data.NM2_URL,
        is_external=True,
    )

    nm3 = rx.chakra.link(
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.vstack(
                    rx.chakra.image(
                        src="/articles/nm3/cover.jpeg",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    read_markdown(
                        "assets/articles/nm3/title.md",
                        component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK"],
                    ),
                    read_markdown("assets/articles/nm3/description.md"),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href=asset_data.NM3_URL,
        is_external=True,
    )

    tsne = rx.chakra.link(
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.vstack(
                    rx.chakra.image(
                        src="/articles/tsne/cover.png",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    read_markdown(
                        "assets/articles/tsne/title.md",
                        component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK"],
                    ),
                    read_markdown("assets/articles/tsne/description.md"),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href=asset_data.TSNE_URL,
        is_external=True,
    )

    dml1 = rx.chakra.link(
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.vstack(
                    rx.chakra.image(
                        src="/articles/dml1/cover.png",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    read_markdown(
                        "assets/articles/dml1/title.md",
                        component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK"],
                    ),
                    read_markdown("assets/articles/dml1/description.md"),
                )
            ),
            # padding_x="3em", MIDDLE COLUMN
            padding_bottom="3em",
        ),
        href=asset_data.DML1_URL,
        is_external=True,
    )

    dml2 = rx.chakra.link(
        rx.chakra.box(
            rx.chakra.center(
                rx.chakra.vstack(
                    rx.chakra.image(
                        src="/articles/dml2/cover.png",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    read_markdown(
                        "assets/articles/dml2/title.md",
                        component_map=ARTICLES_PAGE["MARKDOWN_STYLE_BLOCK"],
                    ),
                    read_markdown("assets/articles/dml2/description.md"),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href=asset_data.DML2_URL,
        is_external=True,
    )

    body = rx.chakra.box(
        container(**ARTICLES_PAGE["BODY_CONTAINER_STYLE"]),
        rx.chakra.hstack(
            dml2,
            dml1,
            tsne,
            display=["none", "none", "none", "none", "flex", "flex"],
            padding_bottom="5em",
            padding_x="5em",
        ),
        rx.chakra.hstack(
            nm3,
            nm2,
            nm1,
            display=["none", "none", "none", "none", "flex", "flex"],
            padding_bottom="5em",
            padding_x="5em",
        ),
        rx.chakra.center(
            rx.chakra.hstack(
                logistic,
                fwl,
                display=["none", "none", "none", "none", "flex", "flex"],
                # padding_bottom="5em",
                padding_x="10em",
            )
        ),
        rx.chakra.vstack(
            dml2,
            rx.chakra.box(dml1, padding_x="3em"),
            tsne,
            nm3,
            rx.chakra.box(nm2, padding_x="3em"),
            nm1,
            logistic,
            fwl,
            display=["flex", "flex", "flex", "flex", "none", "none"],
            padding_x="1em",
        ),
    )

    return body
