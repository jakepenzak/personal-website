import reflex as rx
from reflex.style import toggle_color_mode

from assets import asset_data
from personal_website.structural import styles


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
                    "Projects",
                    href="/projects",
                    display=["none", "none", "none", "none", "flex", "flex"],
                    **styles.NAVBAR["NAVBAR_BUTTON_STYLE"],
                ),
                appearance_toggle(),
                menu_button(),
            ),
            align="center",
            **styles.NAVBAR["NAVBAR_STYLE"],
        ),
    )

    return navbar


def navbar_link(text: str, url: str, **kwargs) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url, **kwargs)


def appearance_toggle() -> rx.Component:
    """Toggle the persisted light or dark appearance."""
    return rx.tooltip(
        rx.icon_button(
            rx.color_mode_cond(
                rx.icon(tag="moon", size=18), rx.icon(tag="sun", size=18)
            ),
            on_click=toggle_color_mode,
            variant="ghost",
            color=styles.theme_value("#522181", "#CFBCFF"),
            aria_label="Toggle light and dark mode",
            margin_left="0.75em",
        ),
        content=rx.color_mode_cond("Switch to dark mode", "Switch to light mode"),
    )


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
            src=rx.color_mode_cond(
                asset_data.NAVBAR_LOGO, asset_data.FOOTER_LOGO
            ),
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
    pages = ["Articles", "Resume", "Projects"]

    menu_button = rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.icon("menu"),
                    weight="medium",
                    variant="ghost",
                    size="3",
                    color=styles.theme_value("#522181", "#CFBCFF"),
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
