"""The articles page."""

import reflex as rx

from assets.shared import links
from personal_website.styles import ARTICLES_PAGE
from personal_website.templates import template
from personal_website.utilities.markdown import read_markdown


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.container(
        *children,
        **kwargs,
    )


## Articles Header
def header():
    """The introduction section of the articles page."""

    heading = rx.heading(
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

    heading_mobile = rx.heading(
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

    markdown_content = rx.box(
        rx.vstack(
            read_markdown(
                "assets/articles/intro.md",
                component_map=ARTICLES_PAGE["MARKDOWN_STYLE_INTRO"],
            ),
        ),
        width="100%",
        padding_x="12em",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )

    markdown_content_mobile = rx.box(
        rx.vstack(
            read_markdown(
                "assets/articles/intro.md",
                component_map=ARTICLES_PAGE["MARKDOWN_STYLE_INTRO"],
            ),
        ),
        width="100%",
        padding_x="6em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    intro = rx.box(
        container(**ARTICLES_PAGE["HEADER_CONTAINER_STYLE"]),
        rx.vstack(heading, heading_mobile, markdown_content, markdown_content_mobile),
    )

    return intro


## Articles Body
def body():
    """The body section of the articles page."""

    # Blocks
    fwl = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
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
        href=links.FWL_URL,
        is_external=True,
    )

    logistic = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
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
        href=links.LOGISTIC_URL,
        is_external=True,
    )

    nm1 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
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
        href=links.NM1_URL,
        is_external=True,
    )

    nm2 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
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
        href=links.NM2_URL,
        is_external=True,
    )

    nm3 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
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
        href=links.NM3_URL,
        is_external=True,
    )

    tsne = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
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
        href=links.TSNE_URL,
        is_external=True,
    )

    dml1 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
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
        href=links.DML1_URL,
        is_external=True,
    )

    dml2 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
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
        href=links.DML2_URL,
        is_external=True,
    )

    intro = rx.box(
        container(**ARTICLES_PAGE["BODY_CONTAINER_STYLE"]),
        rx.hstack(
            dml2,
            dml1,
            tsne,
            display=["none", "none", "none", "none", "flex", "flex"],
            padding_bottom="5em",
            padding_x="5em",
        ),
        rx.hstack(
            nm3,
            nm2,
            nm1,
            display=["none", "none", "none", "none", "flex", "flex"],
            padding_bottom="5em",
            padding_x="5em",
        ),
        rx.center(
            rx.hstack(
                logistic,
                fwl,
                display=["none", "none", "none", "none", "flex", "flex"],
                # padding_bottom="5em",
                padding_x="10em",
            )
        ),
        rx.vstack(
            dml2,
            rx.box(dml1, padding_x="3em"),
            tsne,
            nm3,
            rx.box(nm2, padding_x="3em"),
            nm1,
            logistic,
            fwl,
            display=["flex", "flex", "flex", "flex", "none", "none"],
            padding_x="1em",
        ),
    )

    return intro


@template(route="/articles", title="Articles")
def articles() -> rx.Component:
    """The articles page.

    Returns:
        The UI for the articles page.
    """
    return rx.vstack(
        header(),
        rx.divider(width="80vh"),
        body(),
        rx.center(rx.image(src="/shared/website_bar.png", width="100%")),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )
