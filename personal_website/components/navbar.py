import reflex as rx

from personal_website.styles import NAVBAR
from assets import asset_data


def navbar() -> rx.Component:
    """
    Create the navbar component.

    Returns:
        rx.Component: The created navbar component.
    """

    navbar = rx.chakra.vstack(
        rx.chakra.box(
            rx.chakra.hstack(
                navbar_logo(**NAVBAR["NAVBAR_LOGO_STYLE"]),
                rx.chakra.spacer(),
                rx.chakra.link(
                    "Articles",
                    href="/articles",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.chakra.link(
                    "Professional Resume",
                    href="/resume",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.chakra.link(
                    "Research",
                    href="/research",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.chakra.menu(
                    rx.chakra.menu_button(
                        rx.chakra.hstack(
                            rx.chakra.text(
                                "Projects", **NAVBAR["NAVAR_MENU_BUTTON_STYLE"]
                            ),
                            rx.chakra.icon(
                                tag="chevron_down",
                                **NAVBAR["NAVBAR_MENU_CHEVRON_STYLE"],
                            ),
                        ),
                        display=["none", "none", "none", "none", "flex", "flex"],
                        width="8em",
                        border="none",
                        _hover={"text_decoration": "underline"},
                    ),
                    rx.chakra.menu_list(
                        rx.chakra.link(
                            rx.chakra.menu_item(
                                "About", **NAVBAR["NAVBAR_DROPDOWN_STYLE"]
                            ),
                            href="/projects",
                        ),
                        rx.chakra.menu_divider(),
                        rx.chakra.link(
                            rx.chakra.menu_item(
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

    return navbar


def navbar_logo(**style_props) -> rx.Component:
    """
    Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.

    Returns:
        rx.Component: The logo component.
    """
    navbar_logo = rx.chakra.link(
        rx.chakra.image(
            src=asset_data.NAVBAR_LOGO,
            **style_props,
        ),
        href="/",
    )

    return navbar_logo


## For mobile & when screen is small
def menu_button() -> rx.Component:
    """The menu button on the top right of the page.

    Returns:
        rx.Component: The menu button component.
    """
    pages = ["Articles", "Resume", "Research", "Projects"]

    menu_button = rx.chakra.box(
        rx.chakra.menu(
            rx.chakra.menu_button(
                rx.chakra.icon(tag="hamburger", size="4em"),
            ),
            rx.chakra.menu_list(
                *[
                    rx.chakra.menu_item(
                        rx.chakra.link(
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

    return menu_button
