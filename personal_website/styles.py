"""Styles for the app."""

import reflex as rx

LOGO_URL = "/icon.png"
NAVBAR_LOGO = "/icon.png"

border_radius = "0.375rem"
box_shadow = "0px 0px 0px 1px rgba(84, 82, 95, 0.14)"
border = "1px solid #F4F3F6"
text_color = "black"
accent_text_color = "#1A1060"
accent_color = "#F5EFFE"
hover_accent_color = {"_hover": {"color": accent_color}}
hover_accent_bg = {"_hover": {"bg": accent_color}}
content_width_vw = "90vw"
sidebar_width = "20em"


template_content_style = {
    "width": "100%",
    "align_items": "flex-start",
    "box_shadow": box_shadow,
    "border_radius": border_radius,
    "padding": "3em",
    "margin_bottom": "2em",
}

link_style = {
    "color": text_color,
    "text_decoration": "none",
    **hover_accent_color,
}

overlapping_button_style = {
    "background_color": "white",
    "border": border,
    "border_radius": border_radius,
}

base_style = {
    rx.MenuButton: {
        "width": "3em",
        "height": "3em",
        **overlapping_button_style,
    },
    rx.MenuItem: hover_accent_bg,
    "font_family": "Hack",
}

markdown_style = {
    "code": lambda text: rx.code(text, color="#1F1944", bg="#EAE4FD"),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        font_weight="bold",
        # font_family="HackBold",
        color="#03030B",
        text_decoration="underline",
        text_decoration_color="#AD9BF8",
        _hover={
            "color": "#AD9BF8",
            "text_decoration": "underline",
            "text_decoration_color": "#03030B",
        },
    ),
}


# Navigation Bar
navbar_style = {
            "bg":"rgba(255,255,255, 0.9)",
            "backdrop_filter":"blur(10px)",
            "padding_x":"2em",
            "padding_y":"1em",
            "border_bottom":"1px solid #F4F3F6",
            "width":"100%"
}

navbar_logo_style = {
    "height": "4em",
}

navbar_button_style = {
    "color": text_color,
    "font_size": "1.1em",
    "padding_x": "1em"
}

# Index Page
header_container_style = {
    "padding_top":"2em",
    "padding_bottom":"6em",
    "width":"100%",
}

intro_container_style = {
            "height":"8em",
            "width":"100%",
            "background":"radial-gradient(55.39% 67.5% at 50% 100%, rgba(188, 136, 255, 0.16) 0%, rgba(223, 216, 250, 0) 100%);",
            "opacity":"0.4;",
            "transform":"matrix(1, 0, 0, -1, 0, 0);"
}

index_page_style = {"padding_top": "2.5em", "padding_bottom":"3.5em", "padding_x":["auto", "2em"]}