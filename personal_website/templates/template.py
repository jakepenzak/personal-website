"""Common templates used between pages in the app."""

from __future__ import annotations

from personal_website import styles
from typing import Callable
import reflex as rx

# Meta tags for the app.
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=yes, initial-scale=1",
    },
]


def template(
    route: str | None = None,
    title: str | None = None,
    image: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    """The template for each page of the app.

    Args:
        route: The route to reach the page.
        title: The title of the page.
        image: The favicon of the page.
        description: The description of the page.
        meta: Additionnal meta to add to the page.
        on_load: The event handler(s) called when the page load.
        script_tags: Scripts to attach to the page.

    Returns:
        The template with the page content.
    """

    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """The template for each page of the app.

        Args:
            page_content: The content of the page.

        Returns:
            The template with the page content.
        """
        # Get the meta tags for the page.
        all_meta = [*default_meta, *(meta or [])]

        @rx.page(
            route=route,
            title=title,
            image=image,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def templated_page():
            from personal_website.components.navbar import navbar
            from personal_website.components.footer import footer

            return rx.box(
                navbar(),
                page_content(),
                footer()
                # align_items="flex-start",
                # transition="left 0.5s, width 0.5s",
                # position="relative"
            )

        return templated_page

    return decorator
