import reflex as rx

from personal_website import styles

from personal_website.base_state import State
from personal_website.components.footer import footer
from personal_website.components.navbar import navbar
from personal_website.components.spline import spline_component_404


class State404(State):
    @rx.var
    def origin_url(self) -> str:
        return self.router_data.get("asPath", "")


def _404():
    return rx.center(
        rx.vstack(
            rx.heading(rx.constants.Page404.TITLE),
            rx.text(
                "Oops, the page at ",
                rx.code(State404.origin_url),
                " doesn't exist.",
            ),
            rx.spacer(height="2em"),
            spline_component_404(),
        ),
        position="relative",
        min_height="80vh",
        width="100%",
        max_width="100%",
        overflow_x="hidden",
    )


def index():
    # Wrap the component in the template.
    return rx.box(navbar(), _404(), rx.spacer(), footer(), width="100%")
