"""The Reflex logo component."""

import reflex as rx

from personal_website import styles


def navbar_logo(**style_props):
    """Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.
    """
    return rx.link(
        rx.image(
            src=styles.NAVBAR_LOGO,
            **style_props,
        ),
        href="/",
    )


def footer_logo(**style_props):
    """Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.
    """
    return rx.link(
        rx.image(
            src=styles.FOOTER_LOGO,
            **style_props,
        ),
        href="/",
    )
