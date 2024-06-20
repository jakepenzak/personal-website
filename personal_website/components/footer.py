import reflex as rx

from assets import asset_data
from personal_website.structural import styles


def footer() -> rx.Component:
    """
    Creates a footer component with links to social media profiles and contact information.

    Returns:
        rx.Component: The footer component.
    """
    footer = rx.box(
        rx.hstack(
            rx.hstack(
                rx.link(
                    rx.image(src=asset_data.LINKEDIN_LOGO, height="3em"),
                    href=asset_data.LINKEDIN_URL,
                    is_external=True,
                ),
                rx.link(
                    rx.image(src=asset_data.MEDIUM_LOGO, height="3em"),
                    href=asset_data.MEDIUM_URL,
                    is_external=True,
                ),
                rx.link(
                    rx.image(src=asset_data.GITHUB_LOGO, height="3em"),
                    href=asset_data.GITHUB_URL,
                    is_external=True,
                ),
                rx.link(
                    rx.image(src=asset_data.EMAIL_LOGO, height="3em"),
                    href=asset_data.CONTACT_URL,
                ),
                align="center",
            ),
            footer_logo(**styles.FOOTER["FOOTER_LOGO_STYLE"]),
            justify="between",
            align="center",
            **styles.FOOTER["FOOTER_STYLE"],
        ),
    )

    return footer


def footer_logo(**style_props) -> rx.Component:
    """
    Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.

    Returns:
        rx.Component: The logo component.
    """
    return rx.link(
        rx.image(
            src=asset_data.FOOTER_LOGO,
            **style_props,
        ),
        href="/",
    )
