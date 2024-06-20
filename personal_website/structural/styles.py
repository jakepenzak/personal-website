"""Styles for the app."""

import reflex as rx

# COMMON STYLES
text_color = "black"

BASE_STYLE = {
    "font_family": "Hack",
    "bg": "white",
    "color": text_color,
    rx.text: {"color": text_color, "font_family": "Hack"},
    rx.menu.content: {"bg": "white"},
    rx.container: {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"]},
    rx.heading: {
        "font_size": "3em",
        "font_family": "HackBold",
        "text_align": "center",
        "color": "#522181",
        "padding_bottom": "0.5em",
        "display": ["none", "none", "flex", "flex", "flex", "flex"],
        "height": "100%",
    },
    rx.vstack: {"width": "100%", "max_width": "100%", "overflow_x": "hidden"},
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
    "NAVBAR_BUTTON_STYLE": {
        "color": text_color,
        "size": "4",
        "padding_x": "0.75em",
    },
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
    "FOOTER_LOGO_STYLE": {"height": "4em", "align": "center"},
}


#  INDEX PAGE
INDEX_PAGE = {
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
    "MARKDOWN_STYLE": {
        "a": lambda text, **props: rx.link(
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
    "MARKDOWN_STYLE_INTRO": {
        "code": lambda text: rx.code(text, color="#1F1944", bg="#EAE4FD"),
        "a": lambda text, **props: rx.link(
            text,
            **props,
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
    "MARKDOWN_STYLE_BLOCK_HEADER": {
        "p": lambda text: rx.text(text, color="#522181", font_family="HackBold")
    },
    "MARKDOWN_STYLE_BLOCK_BODY": {"p": lambda text: rx.text(text, color="black")},
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
