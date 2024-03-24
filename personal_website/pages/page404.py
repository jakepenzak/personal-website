import reflex as rx

from personal_website.base_state import State
from personal_website.components.footer import footer
from personal_website.components.navbar import navbar


class State404(State):
    @rx.var
    def origin_url(self) -> str:
        return self.router_data.get("asPath", "")


def _404():
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


def index404():
    # Wrap the component in the template.
    return rx.chakra.box(navbar(), _404(), rx.chakra.spacer(), footer(), width="100%")
