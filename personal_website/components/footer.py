import reflex as rx

from assets import asset_data
from personal_website.styles import FOOTER


def footer() -> rx.Component:
    """
    Creates a footer component with links to social media profiles and contact information.

    Returns:
        rx.Component: The footer component.
    """
    footer = rx.chakra.box(
        rx.chakra.hstack(
            rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.image(src=asset_data.LINKEDIN_LOGO, height="3em"),
                    href=asset_data.LINKEDIN_URL,
                    style=FOOTER["FOOTER_ITEM_STYLE"],
                    is_external=True,
                ),
                rx.chakra.link(
                    rx.chakra.image(src=asset_data.MEDIUM_LOGO, height="3em"),
                    href=asset_data.MEDIUM_URL,
                    style=FOOTER["FOOTER_ITEM_STYLE"],
                    is_external=True,
                ),
                rx.chakra.link(
                    rx.chakra.image(src=asset_data.GITHUB_LOGO, height="3em"),
                    href=asset_data.GITHUB_URL,
                    style=FOOTER["FOOTER_ITEM_STYLE"],
                    is_external=True,
                ),
                rx.chakra.link(
                    rx.chakra.image(src=asset_data.EMAIL_LOGO, height="3em"),
                    href=asset_data.CONTACT_URL,
                    style=FOOTER["FOOTER_ITEM_STYLE"],
                ),
            ),
            footer_logo(**FOOTER["FOOTER_LOGO_STYLE"]),
            justify="space-between",
            color="#94a3b8",
            align_items="top",
            min_width="100%",
        ),
        **FOOTER["FOOTER_STYLE"],
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
    return rx.chakra.link(
        rx.chakra.image(
            src=asset_data.FOOTER_LOGO,
            **style_props,
        ),
        href="/",
    )
