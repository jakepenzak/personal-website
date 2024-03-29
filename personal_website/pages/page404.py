import reflex as rx

from personal_website.base_state import State
from personal_website.components.footer import footer
from personal_website.components.navbar import navbar


# Create a 404 page with the navbar, 404 content, spacer, and footer.
def index404() -> rx.Component:
    """
    Renders the 404 page with the navbar, 404 content, spacer, and footer.

    Returns:
        rx.Component: The rendered 404 page component.
    """
    return rx.chakra.box(navbar(), _404(), rx.chakra.spacer(), footer(), width="100%")


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
    return rx.chakra.center(
        rx.chakra.vstack(
            rx.chakra.heading(rx.constants.Page404.TITLE),
            rx.chakra.text(
                "Oops, the page at ",
                rx.chakra.code(State404.origin_url),
                " doesn't exist.",
            ),
            rx.chakra.spacer(height="4em"),
            rx.chakra.image(src="/shared/website_bar.png", width="100%"),
        ),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )
