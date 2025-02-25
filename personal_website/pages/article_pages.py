import reflex as rx

from personal_website.structural import template
from personal_website.components.utilities.html_helpers import iframe_gen
from assets import asset_data


@template(route="/articles/fwl", title="Controlling for 'X'?")
def fwl() -> rx.Component:
    """Article page for 'Controlling for 'X'?'

    Returns:
        The UI for the 'Controlling for 'X'? article page.
    """

    return rx.vstack(
        rx.box(rx.html(iframe_gen("/notebooks/fwl.html")), width="100%"),
        rx.center(rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")),
        min_height="80vh",
        width="100%",
    )


@template(
    route="/articles/logistic", title="Predictive Parameterics in a Logistic Regression"
)
def logistic() -> rx.Component:
    """Article page for 'Predictive Parameterics in a Logistic Regression'

    Returns
        The UI for the 'Predictive Parameterics in a Logistic Regression' article page
    """

    return rx.vstack(
        rx.box(rx.html(iframe_gen("/notebooks/logistic.html")), width="100%"),
        rx.center(rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")),
        min_height="80vh",
        width="100%",
    )


@template(route="/articles/tsne", title="t-SNE from Scratch (ft. NumPy)")
def tsne() -> rx.Component:
    """Article page for 't-SNE from Scratch (ft. NumPy)'

    Returns
        The UI for the 't-SNE from Scratch (ft. NumPy)' article page
    """

    return rx.vstack(
        rx.box(rx.html(iframe_gen("/notebooks/tsne.html")), width="100%"),
        rx.center(rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")),
        min_height="80vh",
        width="100%",
    )
