import reflex as rx

from personal_website.structural import styles
from assets import asset_data


def navbar() -> rx.Component:
    """
    Create the navbar component.

    Returns:
        rx.Component: The created navbar component.
    """

    navbar = rx.box(
        rx.hstack(
            navbar_logo(),
            rx.spacer(),
            rx.center(
                rx.link(
                    "Articles",
                    href="/articles",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **styles.NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.link(
                    "Professional Resume",
                    href="/resume",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **styles.NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.link(
                    "Research",
                    href="/research",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **styles.NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            rx.text("Projects", **styles.NAVBAR["NAVBAR_BUTTON_STYLE"]),
                            rx.icon("chevron_down"),
                            variant="ghost",
                            radius="full",
                        ),
                        display=["none", "none", "none", "none", "flex", "flex"],
                    ),
                    rx.menu.content(
                        rx.menu.item(navbar_link("About", "/projects")),
                        rx.divider(),
                        rx.menu.item(navbar_link("Forthcoming", "/projects")),
                    ),
                ),
                menu_button(),
            ),
            align="center",
            **styles.NAVBAR["NAVBAR_STYLE"],
        ),
    )

    return navbar


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar_logo() -> rx.Component:
    """
    Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.

    Returns:
        rx.Component: The logo component.
    """
    navbar_logo = rx.link(
        rx.image(
            src=asset_data.NAVBAR_LOGO,
            height="4em",
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

    menu_button = rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.icon("menu"),
                    weight="medium",
                    variant="ghost",
                    size="3",
                    color="#522181",
                ),
            ),
            rx.menu.content(
                *[
                    rx.menu.item(navbar_link(page, f"/{page.lower()}"))
                    for page in pages
                ],
            ),
        ),
        display=["flex", "flex", "flex", "flex", "none", "none"],
    )

    return menu_button
