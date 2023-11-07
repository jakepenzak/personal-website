from personal_website import styles
from personal_website.base_state import State
from personal_website.components.logo import navbar_logo
import reflex as rx


logo = navbar_logo(**styles.navbar_logo_style)


def navbar(sidebar: rx.Component = None) -> rx.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """

    # Create the navbar component.
    return rx.vstack(
        rx.box(
            rx.hstack(
                logo,
                rx.spacer(),
                rx.link(
                    "Articles",
                    href="/articles",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **styles.navbar_button_style,
                ),
                rx.link(
                    "Professional Resume",
                    href="/resume",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **styles.navbar_button_style,
                ),
                rx.link(
                    "Research",
                    href="/research",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **styles.navbar_button_style,
                ),
                rx.menu(
                    rx.menu_button(
                        rx.hstack(
                            rx.text("Projects", **styles.navbar_menu_button_style),
                            rx.icon(
                                tag="chevron_down", **styles.navbar_menu_chevron_style
                            ),
                        ),
                        display=["none", "none", "none", "none", "flex", "flex"],
                        width="8em",
                        border="none",
                        _hover={"text_decoration": "underline"},
                    ),
                    rx.menu_list(
                        rx.link(
                            rx.menu_item("About", **styles.navbar_dropdown_style),
                            href="/projects",
                        ),
                        rx.menu_divider(),
                        rx.link(
                            rx.menu_item("Forthcoming", **styles.navbar_dropdown_style),
                            href="/projects",
                        ),
                    ),
                ),
                menu_button(),
            ),
            **styles.navbar_style,
        ),
        position="sticky",
        top="0",
        z_index="999",
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
                rx.icon(
                    tag="hamburger",
                    size="4em",
                    color=styles.text_color,
                ),
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
