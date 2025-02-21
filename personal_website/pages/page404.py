import reflex as rx

from personal_website.base_state import State
from personal_website.components.footer import footer
from personal_website.components.navbar import navbar
from personal_website.structural import template
from assets import asset_data


# Create a 404 page with the navbar, 404 content, spacer, and footer.
@template(route="/404", title="404 - Not Found")
def index404() -> rx.Component:
    """
    Renders the 404 page with the navbar, 404 content, spacer, and footer.

    Returns:
        rx.Component: The rendered 404 page component.
    """
    return rx.box(_404(), rx.spacer())


class State404(State):
    """
    Represents the state for a 404 page.

    Attributes:
        origin_url (str): The original URL that led to the 404 page.
    """

    @rx.var
    def origin_url(self) -> str:
        return self.router_data.get("asPath", "")


def _404() -> rx.Component:
    """
    Returns a React component for the 404 page.

    The component displays a centered layout with a heading, a text message indicating that the page doesn't exist,
    a spacer, and an image.

    Returns:
        rx.Component: The React component for the 404 page.
    """

    return rx.center(
        rx.vstack(
            rx.spacer(height="4em"),
            rx.heading(rx.constants.Page404.TITLE, display=["flex"]),
            rx.text(
                "Oops, the page at ",
                rx.code(State404.origin_url),
                " doesn't exist.",
            ),
            rx.spacer(height="4em"),
            rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%"),
            align_items="center",
        ),
        min_height="80vh",
        width="100%",
        max_width="100%",
    )
