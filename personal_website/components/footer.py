import reflex as rx
from personal_website import constants, styles
from personal_website.components.logo import inverted_logo
from personal_website.pages.index import index
from personal_website import styles


def footer():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.link(
                    rx.image(src="/icons/linkedin.png", height="3em"),
                    href=constants.LINKEDIN_URL,
                    style=styles.footer_item_style,
                    is_external=True,
                ),
                rx.link(
                    rx.image(src="/icons/medium.png", height="3em"),
                    href=constants.MEDIUM_URL,
                    style=styles.footer_item_style,
                    is_external=True,
                ),
                rx.link(
                    rx.image(src="/icons/github.png", height="3em"),
                    href=constants.GITHUB_URL,
                    style=styles.footer_item_style,
                    is_external=True,
                ),
                rx.link(
                    rx.image(src="/icons/email.png", height="3em"),
                    href=constants.CONTACT_URL,
                    style=styles.footer_item_style,
                ),
            ),
            inverted_logo(**styles.footer_logo_style),
            justify="space-between",
            color="#94a3b8",
            align_items="top",
            min_width="100%",
        ),
        **styles.footer_style,
    )
