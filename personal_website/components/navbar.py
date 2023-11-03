from personal_website import styles
from personal_website.state import State
from personal_website.components.logo import navbar_logo
import reflex as rx



logo = navbar_logo(**styles.navbar_logo_style)



def navbar(sidebar: rx.Component = None) -> rx.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """

    # Create the navbar component.
    return rx.box(
            rx.hstack(
                logo,
                rx.spacer(),
                rx.link(
                    "Articles",
                    href="/articles",
                    **styles.navbar_button_style
                ),
                rx.link(
                    "Professional Resume",
                    href="/resume",
                    **styles.navbar_button_style
                ),
                rx.link(
                    "Research",
                    href="/research",
                    **styles.navbar_button_style
                ),
                rx.link(
                    "Projects",
                    href="/projects",
                    **styles.navbar_button_style
                ),
            ),
            **styles.navbar_style
        )


## UNUSED

# def menu_button() -> rx.Component:
#     """The menu button on the top right of the page.

#     Returns:
#         The menu button component.
#     """
#     from reflex.page import get_decorated_pages

#     return rx.box(
#         rx.menu(
#             rx.menu_button(
#                 rx.icon(
#                     tag="hamburger",
#                     size="4em",
#                     color=styles.text_color,
#                 ),
#             ),
#             rx.menu_list(
#                 *[
#                     rx.menu_item(
#                         rx.link(
#                             page["title"],
#                             href=page["route"],
#                             width="100%",
#                         )
#                     )
#                     for page in get_decorated_pages()
#                 ],
#                 rx.menu_divider(),
#                 rx.menu_item(
#                     rx.link("About", href="https://github.com/reflex-dev", width="100%")
#                 ),
#                 rx.menu_item(
#                     rx.link("Contact", href="mailto:founders@=reflex.dev", width="100%")
#                 ),
#             ),
#         ),
#         position="fixed",
#         right="1.5em",
#         top="1.5em",
#         z_index="500",
#     )