import reflex as rx

from personal_website.base_state import State
from personal_website.styles import NAVBAR

NAVBAR_LOGO = "/shared/icon.png"


def navbar_logo(**style_props):
    """Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.
    """
    return rx.link(
        rx.image(
            src=NAVBAR_LOGO,
            **style_props,
        ),
        href="/",
    )


## For mobile & when screen is small
pages = ["Articles", "Resume", "Research", "Projects"]


def menu_button() -> rx.Component:
    """The menu button on the top right of the page.

    Returns:
        The menu button component.
    """
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.menu(
            rx.menu_button(
                rx.icon(tag="hamburger", size="4em"),
            ),
            rx.menu_list(
                *[
                    rx.menu_item(
                        rx.link(
                            page,
                            href=f"/{page.lower()}",
                            width="100%",
                        )
                    )
                    for page in pages
                ],
            ),
        ),
        display=["flex", "flex", "flex", "flex", "none", "none"],
    )


def navbar(sidebar: rx.Component = None) -> rx.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """

    # Create the navbar component.
    return rx.vstack(
        rx.box(
            rx.hstack(
                navbar_logo(**NAVBAR["NAVBAR_LOGO_STYLE"]),
                rx.spacer(),
                rx.link(
                    "Articles",
                    href="/articles",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.link(
                    "Professional Resume",
                    href="/resume",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.link(
                    "Research",
                    href="/research",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.menu(
                    rx.menu_button(
                        rx.hstack(
                            rx.text("Projects", **NAVBAR["NAVAR_MENU_BUTTON_STYLE"]),
                            rx.icon(
                                tag="chevron_down",
                                **NAVBAR["NAVBAR_MENU_CHEVRON_STYLE"],
                            ),
                        ),
                        display=["none", "none", "none", "none", "flex", "flex"],
                        width="8em",
                        border="none",
                        _hover={"text_decoration": "underline"},
                    ),
                    rx.menu_list(
                        rx.link(
                            rx.menu_item("About", **NAVBAR["NAVBAR_DROPDOWN_STYLE"]),
                            href="/projects",
                        ),
                        rx.menu_divider(),
                        rx.link(
                            rx.menu_item(
                                "Forthcoming", **NAVBAR["NAVBAR_DROPDOWN_STYLE"]
                            ),
                            href="/projects",
                        ),
                    ),
                ),
                menu_button(),
            ),
            **NAVBAR["NAVBAR_STYLE"],
        ),
        position="sticky",
        top="0",
        z_index="999",
    )
