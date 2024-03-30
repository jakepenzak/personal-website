"""Styles for the app."""

import reflex as rx

# COMMON STYLES
text_color = "black"

BASE_STYLE = {
    rx.chakra.MenuButton: {
        "width": "3em",
        "height": "3em",
        "background_color": "white",
        "border": "1px solid #F4F3F6",
        "border_radius": "0.375rem",
    },
    rx.chakra.MenuItem: {"_hover": {"color": "#522181", "bg": "#F5EFFE"}},
    "font_family": "Hack",
}

# NAVIGATION BAR

NAVBAR = {
    "NAVBAR_STYLE": {
        "bg": "rgba(255,255,255, 0.9)",
        "backdrop_filter": "blur(10px)",
        "padding_x": "1.5em",
        "padding_y": "1em",
        "border_bottom": "2px solid #F4F3F6",
        "width": "100%",
        "min_height": "10vh",
    },
    "NAVBAR_LOGO_STYLE": {
        "height": "4em",
    },
    "NAVBAR_BUTTON_STYLE": {
        "color": text_color,
        "font_size": "1.1em",
        "padding_x": "0.75em",
    },
    "NAVAR_MENU_BUTTON_STYLE": {
        "color": text_color,
        "font_size": "1.1em",
        "padding_left": "0.75em",
        "_hover": {
            "text_decoration": "underline",
            "text_decoration_color": "#522181",
        },
    },
    "NAVBAR_MENU_CHEVRON_STYLE": {"color": text_color, "font_size": "1.1em"},
    "NAVBAR_DROPDOWN_STYLE": {"_hover": {"color": "#522181", "bg": "#F5EFFE"}},
}

# FOOTER

FOOTER = {
    "FOOTER_STYLE": {
        "box_shadow": "medium-lg",
        "border_top": "0.1em solid #F4F3F6",
        "vertical_align": "bottom",
        "padding_top": "1em",
        "padding_bottom": "1em",
        "padding_x": "1.5em",
        "bg": "#110F1F",
        "postion": "absolute",
        "bottom": "0",
        "min_height": "10vh",
    },
    "FOOTER_ITEM_STYLE": {
        "font_weight": "500",
        "_hover": {"color": "#8451EC"},
    },
    "FOOTER_LOGO_STYLE": {"height": "4em"},
}


#  INDEX PAGE

INDEX_PAGE = {
    "HEADER_CONTAINER_STYLE": {
        "padding_top": "2em",
        "padding_bottom": "6em",
        "width": "100%",
    },
    "INTRO_CONTAINER_STYLE": {
        # "height": "12em",
        "width": "100%",
        "background": "radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(223, 216, 250, 0) 100%);",  #
        "opacity": "0.4;",
        "transform": "matrix(1, 0, 0, -1, 0, 0);",
        "padding_x": "3em",
        "padding_y": "3em",
    },
    "SKILLS_CONTAINER_STYLE": {
        # "height": "12em",
        "width": "100%",
        "background": "radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(223, 216, 250, 0) 100%);",
        "opacity": "0.4;",
        "padding_x": "3em",
        "padding_y": "3em",
    },
    "INDEX_PAGE_STYLE": {
        "padding_top": "2.5em",
        "padding_bottom": "3.5em",
        "padding_x": [["auto", "2em"]],
        "position": "relative",
        "min_height": "80vh",
    },
    "MARKDOWN_STYLE": {
        "a": lambda text, **props: rx.chakra.link(
            text,
            **props,
            text_decoration="underline",
            _hover={
                "color": "#522181",
                "text_decoration": "underline",
                "text_decoration_color": "#522181",
            },
        ),
    },
}

# ARTICLES PAGE
ARTICLES_PAGE = {
    "HEADER_CONTAINER_STYLE": {
        "padding_top": "1em",
        "padding_bottom": "1em",
        "width": "100%",
    },
    "MARKDOWN_STYLE_INTRO": {
        "code": lambda text: rx.chakra.code(text, color="#1F1944", bg="#EAE4FD"),
        "a": lambda text, **props: rx.chakra.link(
            text,
            **props,
            # font_weight="bold",
            # font_family="HackBold",
            color="#03030B",
            text_decoration="underline",
            # text_decoration_color="#522181",
            _hover={
                "color": "#522181",
                "text_decoration": "underline",
                "text_decoration_color": "#522181",
            },
        ),
    },
    "BODY_CONTAINER_STYLE": {"padding_top": "3em", "padding_x": "3em", "width": "100%"},
    "MARKDOWN_STYLE_BLOCK_HEADER": {
        "p": lambda text: rx.chakra.text(text, color="#522181", font_family="HackBold")
    },
    "MARKDOWN_STYLE_BLOCK_BODY": {
        "p": lambda text: rx.chakra.text(text, color="black", font_family="Hack")
    },
    "SPLINE_CONTAINER_STYLE": {
        "padding_bottom": "5em",
        "padding_x": "3em",
        "width": "100%",
    },
}

# RESUME PAGE
RESUME_PAGE = {
    "HEADER_CONTAINER_STYLE": {
        "padding_top": "1em",
        "padding_bottom": "1em",
        "width": "100%",
    },
    "BODY_CONTAINER_STYLE": {"padding_x": "3em", "width": "100%"},
}

# RESEARCH PAGE
RESEARCH_PAGE = {
    "HEADER_CONTAINER_STYLE": {
        "padding_top": "1em",
        "padding_bottom": "1em",
        "width": "100%",
    },
    "BODY_CONTAINER_STYLE": {
        "width": "100%",
        "background": "radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(223, 216, 250, 0) 100%);",  #
        "opacity": "0.4;",
        "transform": "matrix(1, 0, 0, -1, 0, 0);",
        "padding_x": "2em",
        "padding_y": "2em",
    },
}

# PROJECTS PAGE
PROJECTS_PAGE = {
    "HEADER_CONTAINER_STYLE": {
        "padding_top": "1em",
        "padding_bottom": "1em",
        "width": "100%",
    }
}


## UNUSED

# MARKDOWN = {
#     "code": lambda text: rx.chakra.code(text, color="#1F1944", bg="#EAE4FD"),
#     "a": lambda text, **props: rx.chakra.link(
#         text,
#         **props,
#         # font_weight="bold",
#         # font_family="HackBold",
#         color="#03030B",
#         text_decoration="underline",
#         # text_decoration_color="#522181",
#         _hover={
#             "color": "#522181",
#             "text_decoration": "underline",
#             "text_decoration_color": "#522181",
#         },
#     ),
# }
