import reflex as rx

from personal_website import styles

from personal_website.base_state import State
from personal_website.components.footer import footer
from personal_website.components.navbar import navbar


class State404(State):
    @rx.var
    def origin_url(self) -> str:
        return self.router_data.get("asPath", "")


def _404():
    return rx.center(
        rx.vstack(
            rx.heading(rx.constants.Page404.TITLE),
            rx.text(
                "Oups, the page at ",
                rx.code(State404.origin_url),
                " doesn't exist.",
            ),
            rx.spacer(),
        ),
        height="80vh",
        width="100%",
    )


def index():
    # Wrap the component in the template.
    return rx.box(
        navbar(),
        _404(),
        footer(),
        width="100%",
    )