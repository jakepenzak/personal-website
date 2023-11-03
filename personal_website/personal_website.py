"""Welcome to Reflex!."""

from personal_website import styles

# Import all the pages.
from personal_website.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style, stylesheets=["/fonts/fonts.css"])
app.compile()
