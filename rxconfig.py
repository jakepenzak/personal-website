import os

import reflex as rx

config = rx.Config(
    app_name="personal_website",
    api_url=os.environ.get("API_URL", "http://localhost:8000"),
    show_built_with_reflex=False,
)
