import reflex as rx

from personal_website.structural import template
from personal_website.components.utilities.html_helpers import iframe_gen
from assets import asset_data


def article_page(html_path: str) -> rx.Component:
    return rx.vstack(
        rx.box(rx.html(iframe_gen(html_path)), width="100%"),
        rx.center(rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")),
        min_height="80vh",
        width="100%",
    )


@template(route="/articles/fwl", title="Controlling for 'X'?")
def fwl() -> rx.Component:
    """Article page for 'Controlling for 'X'?'

    Returns:
        The UI for the 'Controlling for 'X'? article page.
    """

    return article_page("/articles/notebooks/html/fwl.html")


@template(
    route="/articles/logistic", title="Predictive Parameterics in a Logistic Regression"
)
def logistic() -> rx.Component:
    """Article page for 'Predictive Parameterics in a Logistic Regression'

    Returns
        The UI for the 'Predictive Parameterics in a Logistic Regression' article page
    """

    return article_page("/articles/notebooks/html/logistic.html")


@template(route="/articles/tsne", title="t-SNE from Scratch (ft. NumPy)")
def tsne() -> rx.Component:
    """Article page for 't-SNE from Scratch (ft. NumPy)'

    Returns
        The UI for the 't-SNE from Scratch (ft. NumPy)' article page
    """

    return article_page("/articles/notebooks/html/tsne.html")


@template(route="/articles/dml1", title="Double Machine Learning, Simplified: Part 1")
def dml1() -> rx.Component:
    """Article page for 'Double Machine Learning, Simplified: Part 1'

    Returns
        The UI for the 'Double Machine Learning, Simplified: Part 1' article page
    """

    return article_page("/articles/notebooks/html/dml1.html")


@template(route="/articles/dml2", title="Double Machine Learning, Simplified: Part 2")
def dml2() -> rx.Component:
    """Article page for 'Double Machine Learning, Simplified: Part 2'

    Returns
        The UI for the 'Double Machine Learning, Simplified: Part 2' article page
    """

    return article_page("/articles/notebooks/html/dml2.html")


@template(
    route="/articles/nm1",
    title="Optimization, Newton's Method, & Profit Maximization: Part 1",
)
def nm1() -> rx.Component:
    """Article page for 'Optimization, Newton's Method, & Profit Maximization: Part 1'

    Returns
        The UI for the 'Optimization, Newton's Method, & Profit Maximization: Part 1' article page
    """

    return article_page("/articles/notebooks/html/nm1.html")


@template(
    route="/articles/nm2",
    title="Optimization, Newton's Method, & Profit Maximization: Part 2",
)
def nm2() -> rx.Component:
    """Article page for 'Optimization, Newton's Method, & Profit Maximization: Part 2'

    Returns
        The UI for the 'Optimization, Newton's Method, & Profit Maximization: Part 2' article page
    """

    return article_page("/articles/notebooks/html/nm2.html")


@template(
    route="/articles/nm3",
    title="Optimization, Newton's Method, & Profit Maximization: Part 3",
)
def nm3() -> rx.Component:
    """Article page for 'Optimization, Newton's Method, & Profit Maximization: Part 3'

    Returns
        The UI for the 'Optimization, Newton's Method, & Profit Maximization: Part 3' article page
    """

    return article_page("/articles/notebooks/html/nm3.html")
