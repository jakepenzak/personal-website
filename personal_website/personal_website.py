import reflex as rx

from personal_website.structural import styles

# Import the pages so their decorators are evaluated, and expose the custom 404
# component for explicit registration below.
from personal_website.pages import index404

# Create the app and compile it.
app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=["/shared/fonts/fonts.css"],
    theme=rx.theme(accent_color="violet"),
)

# Register the custom 404 page once. Reflex materializes 404 components during
# registration, so decorating it causes duplicate components on worker startup.
app.add_page(index404, route="/404", title="404 - Not Found")
