"""The articles page."""

from personal_website.styles import ARTICLES_PAGE
from personal_website.templates import template
from personal_website.components.spline import spline_component_404

import reflex as rx


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

    with open("assets/text/articles_intro.md", encoding="utf-8") as intro:
        content = intro.read()

    markdown_content = rx.box(
        rx.vstack(
            rx.markdown(content, component_map=ARTICLES_PAGE["markdown_style_intro"]),
        ),
        width="100%",
        padding_x="12em",
        display=["none", "none", "flex", "flex", "flex", "flex"],
    )

    markdown_content_mobile = rx.box(
        rx.vstack(
            rx.markdown(content, component_map=ARTICLES_PAGE["markdown_style_intro"]),
        ),
        width="100%",
        padding_x="6em",
        display=["flex", "flex", "none", "none", "none", "none"],
    )

    intro = rx.box(
        container(**ARTICLES_PAGE["header_container_style"]),
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
                        src="/articles/fwl.png",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    rx.markdown(
                        open("assets/text/articles/fwl.md", encoding="utf-8").read(),
                        component_map=ARTICLES_PAGE["markdown_style_block"],
                    ),
                    rx.markdown(
                        """<center> Understanding Linear Regression 
                                 Mechanics via the Frisch-Waugh-Lovell Theorem </center>"""
                    ),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href="https://towardsdatascience.com/controlling-for-x-9cb51652f7ad",
        is_external=True,
    )

    logistic = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
                        src="/articles/logistic.png",
                        height="100%",
                        width="100%",
                        max_width="35em",
                        max_height="35em",
                    ),
                    rx.markdown(
                        open(
                            "assets/text/articles/logistic.md", encoding="utf-8"
                        ).read(),
                        component_map=ARTICLES_PAGE["markdown_style_block"],
                    ),
                    rx.markdown(
                        """<center> Acquire a robust understanding of logit model 
                                parameters beyond the canonical odds ratio interpretation </center>"""
                    ),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href="https://towardsdatascience.com/predictive-parameters-in-a-logistic-regression-making-sense-of-it-all-476bde9825f3",
        is_external=True,
    )

    nm1 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
                        src="/articles/nm1.gif",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    rx.markdown(
                        open("assets/text/articles/nm1.md", encoding="utf-8").read(),
                        component_map=ARTICLES_PAGE["markdown_style_block"],
                    ),
                    rx.markdown(
                        """<center> Learn how to solve and utilize Newton's Method
                                    to solve multi-dimensional optimization problems </center>"""
                    ),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href="https://towardsdatascience.com/optimization-newtons-method-profit-maximization-part-1-basic-optimization-theory-ff7c5f966565",
        is_external=True,
    )

    nm2 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
                        src="/articles/nm2.jpeg",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    rx.markdown(
                        open("assets/text/articles/nm2.md", encoding="utf-8").read(),
                        component_map=ARTICLES_PAGE["markdown_style_block"],
                    ),
                    rx.markdown(
                        """<center> Learn how to extend Newton's Method to 
                                    solve constrained optimization problems </center>"""
                    ),
                )
            ),
            # padding_x="3em", MIDDLE COLUMN
            padding_bottom="3em",
        ),
        href="https://towardsdatascience.com/optimization-newtons-method-profit-maximization-part-2-constrained-optimization-theory-dc18613c5770",
        is_external=True,
    )

    nm3 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
                        src="/articles/nm3.jpeg",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    rx.markdown(
                        open("assets/text/articles/nm3.md", encoding="utf-8").read(),
                        component_map=ARTICLES_PAGE["markdown_style_block"],
                    ),
                    rx.markdown(
                        """<center> Learn how to apply optimization & econometric techniques to 
                                    solve an applied profit maximization problem </center>"""
                    ),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href="https://towardsdatascience.com/optimization-newtons-method-profit-maximization-part-3-applied-profit-maximization-23a8c16167cd",
        is_external=True,
    )

    tsne = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
                        src="/articles/tsne.png",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    rx.markdown(
                        open("assets/text/articles/tsne.md", encoding="utf-8").read(),
                        component_map=ARTICLES_PAGE["markdown_style_block"],
                    ),
                    rx.markdown(
                        """<center> Acquire a deep understanding of the inner workings of t-SNE
                                    via implementation from scratch in python </center>"""
                    ),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href="https://towardsdatascience.com/t-sne-from-scratch-ft-numpy-172ee2a61df7",
        is_external=True,
    )

    dml1 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
                        src="/articles/dml1.png",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    rx.markdown(
                        open("assets/text/articles/dml1.md", encoding="utf-8").read(),
                        component_map=ARTICLES_PAGE["markdown_style_block"],
                    ),
                    rx.markdown(
                        """<center> Learn how to utilize DML in causal inference tasks </center>"""
                    ),
                )
            ),
            # padding_x="3em", MIDDLE COLUMN
            padding_bottom="3em",
        ),
        href="https://towardsdatascience.com/double-machine-learning-simplified-part-1-basic-causal-inference-applications-3f7afc9852ee",
        is_external=True,
    )

    dml2 = rx.link(
        rx.box(
            rx.center(
                rx.vstack(
                    rx.image(
                        src="/articles/dml2.png",
                        height="100%",
                        width="100%",
                        max_width="25em",
                        max_height="25em",
                    ),
                    rx.markdown(
                        open("assets/text/articles/dml2.md", encoding="utf-8").read(),
                        component_map=ARTICLES_PAGE["markdown_style_block"],
                    ),
                    rx.markdown(
                        """<center> Learn how to utilize DML for estimating individual
                                level treatment effects to enable data-driven targeting </center>"""
                    ),
                )
            ),
            padding_x="3em",
            padding_bottom="3em",
        ),
        href="https://medium.com/towards-data-science/double-machine-learning-simplified-part-2-extensions-the-cate-99926151cac",
        is_external=True,
    )

    intro = rx.box(
        container(**ARTICLES_PAGE["body_container_style"]),
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
            dml1,
            tsne,
            nm3,
            nm2,
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
        rx.desktop_only(rx.center(spline_component_404())),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )
