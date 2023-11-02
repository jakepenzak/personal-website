from personal_website import styles
from personal_website.state import State

import reflex as rx

def navbar(sidebar: rx.Component = None) -> rx.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """

    # Create the navbar component.
    return rx.vstack(
        rx.box(
                rx.hstack(
                    rx.image(
                    src="/icon.svg",
                    height="2em",
                    ),
                    rx.link(
                        "Home",
                        href="/",
                        # style=styles.base_style,
                        # display=["none", "none", "none", "flex", "flex", "flex"],
                    ),
                    rx.link(
                        "Dashboard",
                        href="/dashboard",
                        # style=styles.base_style,
                        # display=["none", "none", "none", "flex", "flex", "flex"],
                    ),
                    rx.link(
                        "Settings",
                        href="/settings",
                        # style=styles.base_style,
                        # display=["none", "none", "none", "none", "flex", "flex"],
                    )
                ),
        ),
    )

    #                 rx.menu(
    #                     rx.menu_button(
    #                         rx.hstack(
    #                             rx.text("Resources", style=styles.NAV_TEXT_STYLE),
    #                             rx.icon(
    #                                 tag="chevron_down", style=styles.NAV_TEXT_STYLE
    #                             ),
    #                             cursor="pointer",
    #                             display=[
    #                                 "none",
    #                                 "none",
    #                                 "none",
    #                                 "flex",
    #                                 "flex",
    #                                 "flex",
    #                             ],
    #                         )
    #                     ),
    #                     rx.menu_list(
    #                         rx.link(
    #                             rx.menu_item(
    #                                 "Changelog", style=styles.NAV_DROPDOWN_STYLE
    #                             ),
    #                             href="/changelog",
    #                         ),
    #                         rx.link(
    #                             rx.menu_item(
    #                                 "Roadmap", style=styles.NAV_DROPDOWN_STYLE
    #                             ),
    #                             href=constants.ROADMAP_URL,
    #                         ),
    #                         rx.link(
    #                             rx.menu_item("FAQ", style=styles.NAV_DROPDOWN_STYLE),
    #                             href="/faq",
    #                         ),
    #                         rx.menu_divider(),
    #                         rx.link(
    #                             rx.menu_item(
    #                                 "Contribute to Open Source",
    #                                 style=styles.NAV_DROPDOWN_STYLE,
    #                             ),
    #                             href=constants.CONTRIBUTING_URL,
    #                         ),
    #                         rx.link(
    #                             rx.menu_item(
    #                                 "Report A Bug",
    #                                 style=styles.NAV_DROPDOWN_STYLE,
    #                             ),
    #                             href=constants.REPORT_A_BUG_URL,
    #                         ),
    #                     ),
    #                 ),
    #                 spacing="2em",
    #             ),
    #             rx.hstack(
    #                 search_bar(),
    #                 # inkeep(
    #                 #     is_open=NavbarState.search_modal,
    #                 #     on_close=NavbarState.change_search,
    #                 # ),
    #                 github_button(),
    #                 discord_button(),
    #                 rx.icon(
    #                     tag="hamburger",
    #                     on_click=NavbarState.toggle_sidebar,
    #                     width="1.5em",
    #                     height="1.5em",
    #                     _hover={
    #                         "cursor": "pointer",
    #                         "color": styles.ACCENT_COLOR,
    #                     },
    #                     display=["flex", "flex", "flex", "none", "none", "none"],
    #                 ),
    #                 height="full",
    #             ),
    #             justify="space-between",
    #             padding_x=styles.PADDING_X,
    #         ),
    #         bg="rgba(255,255,255, 0.9)",
    #         backdrop_filter="blur(10px)",
    #         padding_y=["0.8em", "0.8em", "0.5em"],
    #         border_bottom="1px solid #F4F3F6",
    #         width="100%",
    #     ),
    #     rx.drawer(
    #         rx.drawer_overlay(
    #             rx.drawer_content(
    #                 rx.hstack(
    #                     logo,
    #                     rx.icon(
    #                         tag="close",
    #                         on_click=NavbarState.toggle_sidebar,
    #                         width="4em",
    #                         _hover={
    #                             "cursor": "pointer",
    #                             "color": styles.ACCENT_COLOR,
    #                         },
    #                     ),
    #                     justify="space-between",
    #                     margin_bottom="1.5em",
    #                 ),
    #                 sidebar if sidebar is not None else rx.text("Sidebar"),
    #                 padding_x="2em",
    #                 padding_top="2em",
    #                 bg="rgba(255,255,255, 0.97)",
    #             ),
    #             bg="rgba(255,255,255, 0.5)",
    #         ),
    #         placement="left",
    #         is_open=NavbarState.sidebar_open,
    #         on_close=NavbarState.toggle_sidebar,
    #         bg="rgba(255,255,255, 0.5)",
    #     ),
    #     search_modal(),
    #     position="sticky",
    #     z_index="999",
    #     top="0",
    #     width="100%",
    #     spacing="0",
    # )