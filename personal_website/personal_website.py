"""Welcome to Reflex!."""

import reflex as rx

from personal_website import styles

# Import all the pages.
from personal_website.pages import *

# Create the app and compile it.
app = rx.App(style=styles.BASE_STYLE, stylesheets=["/shared/fonts/fonts.css"])
app.add_custom_404_page(page404.index)
app.compile()
