import reflex as rx

from personal_website.structural import styles

# Import all the pages.
from personal_website.pages import *  # noqa: F403

# Create the app and compile it.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=["/shared/fonts/fonts.css"],
    theme=rx.theme(accent_color="violet"),
)
