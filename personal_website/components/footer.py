import reflex as rx

from assets.shared import links
from personal_website.styles import FOOTER

FOOTER_LOGO = "/shared/icon-inverted.png"
LINKEDIN_LOGO = "/shared/social_icons/linkedin.png"
MEDIUM_LOGO = "/shared/social_icons/medium.png"
GITHUB_LOGO = "/shared/social_icons/github.png"
EMAIL_LOGO = "/shared/social_icons/email.png"


def footer_logo(**style_props):
    """Create a Reflex logo component.

    Args:
        style_props: The style properties to apply to the component.
    """
    return rx.chakra.link(
        rx.chakra.image(
            src=FOOTER_LOGO,
            **style_props,
        ),
        href="/",
    )


def footer():
    return rx.chakra.box(
        rx.chakra.hstack(
            rx.chakra.hstack(
                rx.chakra.link(
                    rx.chakra.image(src=LINKEDIN_LOGO, height="3em"),
                    href=links.LINKEDIN_URL,
                    style=FOOTER["FOOTER_ITEM_STYLE"],
                    is_external=True,
                ),
                rx.chakra.link(
                    rx.chakra.image(src=MEDIUM_LOGO, height="3em"),
                    href=links.MEDIUM_URL,
                    style=FOOTER["FOOTER_ITEM_STYLE"],
                    is_external=True,
                ),
                rx.chakra.link(
                    rx.chakra.image(src=GITHUB_LOGO, height="3em"),
                    href=links.GITHUB_URL,
                    style=FOOTER["FOOTER_ITEM_STYLE"],
                    is_external=True,
                ),
                rx.chakra.link(
                    rx.chakra.image(src=EMAIL_LOGO, height="3em"),
                    href=links.CONTACT_URL,
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
