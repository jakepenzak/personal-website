"""The home page of the app."""

import reflex as rx

from personal_website.components.spline import spline_component_index_page
from personal_website.styles import INDEX_PAGE
from personal_website.templates import template
from personal_website.utilities.markdown import read_markdown
from assets.index.skills.skills_data import skills_data, tech_logos_dict


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )


## Header
def header() -> rx.Component:
    """The header section of the home page."""

    heading = container(
        rx.chakra.hstack(
            rx.chakra.center(
                rx.chakra.heading(
                    """
                    Jacob \n
                    Pieniazek
                    """,
                    font_size="6em",
                    font_family="HackBold",
                    color=["#522181"],
                )
            ),
            spline_component_index_page(),
            display=["none", "none", "none", "flex", "flex", "flex"],
        ),
        rx.chakra.center(
            rx.chakra.heading(
                """
                    Jacob \n
                    Pieniazek
                    """,
                font_size="4em",
                font_family="HackBold",
                color=["#522181"],
                text_align="center",
            ),
            display=["flex", "flex", "flex", "none", "none", "none"],
        ),
        **INDEX_PAGE["HEADER_CONTAINER_STYLE"],
    )

    return heading


## Introduction
def intro() -> rx.Component:
    """The introduction section of the home page."""

    welcome = rx.chakra.heading(
        """
        Welcome!
        """,
        font_size="2em",
        font_family="HackBold",
        text_align="center",
        padding_top="1em",
    )

    body = rx.chakra.box(
        rx.chakra.vstack(
            read_markdown(
                "assets/index/index_intro.md",
                component_map=INDEX_PAGE["MARKDOWN_STYLE"],
            ),
        ),
    )

    intro = rx.chakra.box(
        container(**INDEX_PAGE["INTRO_CONTAINER_STYLE"]),
        rx.chakra.center(
            rx.chakra.hstack(
                rx.chakra.image(
                    src="/index/self.jpg", max_height="35em", max_width="35em"
                ),
                rx.chakra.vstack(welcome, body, padding_left="12em"),
                padding_x="5em",
                display=["none", "none", "none", "flex", "flex", "flex"],
            ),
            rx.chakra.vstack(
                rx.chakra.image(
                    src="/index/self.jpg",
                    height="flex",
                    width="flex",
                    max_height="35em",
                    max_width="35em",
                ),
                rx.chakra.vstack(welcome, body),
                padding_x="3em",
                display=["flex", "flex", "flex", "none", "none", "none"],
            ),
        ),
    )

    return intro


def skillsets_section() -> rx.Component:
    header = rx.heading(
        """
        Skillsets
        """,
        font_size="3em",
        font_family="HackBold",
        text_align="center",
        padding_top="1em",
        padding_bottom="1em",
    )

    skills_radar = rx.center(
        rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="rating",
                stroke="#8884d8",
                fill="#8884d8",
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="subject"),
            data=skills_data,
        ),
        width="100%",
        height="50vh",
    )

    python_eco = rx.center(
        rx.vstack(
            rx.heading(
                """
            Python Libraries
            """,
                font_size="1.5em",
                font_family="HackBold",
                text_align="center",
                padding_top="1em",
            ),
            rx.text(
                """Below is a selection of some of the python libraries 
            I use or have used in my personal & professional work. This list is by no means exhaustive,
            but it does cover a subset of the core libraries I consider myself to be moderately to highly proficient in."""
            ),
        ),
        padding_x="3em",
        width="100%",
    )

    def image_link(src, href):
        return rx.link(rx.image(src=src), href=href, target="_blank")

    stack_grid = rx.center(
        rx.grid(
            *[
                image_link(tech_logos_dict[t].asset_path, tech_logos_dict[t].link)
                for t in list(tech_logos_dict.keys())
            ],
            columns="4",
            spacing="4",
            align="center",
            justify="center",
        )
    )

    tech_stack = rx.center(
        rx.vstack(
            rx.heading(
                """
            Tech Stack & Tools
            """,
                font_size="1.5em",
                font_family="HackBold",
                text_align="center",
                padding_top="1em",
            ),
            rx.text(
                """Similarly, below is a selection of some of the tech 
            stack & tools that I use or have used in my personal & professional work."""
            ),
            stack_grid,
        ),
        padding_x="3em",
        width="100%",
    )

    stack = rx.hstack(
        python_eco,
        tech_stack,
        padding_x="3em",
        width="100%",
    )

    # Used for mobile and tablet view
    skills_list = rx.unordered_list(
        *[rx.list_item(skill) for skill in [d["subject"] for d in skills_data]]
    )

    skills_tabs = rx.center(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Skills", value="Skills"),
                rx.tabs.trigger("Python Ecosystem", value="Python Ecosystem"),
                rx.tabs.trigger("Tech Stack", value="Tech Stack"),
                size="2",
            ),
            rx.tabs.content(
                skills_list,
                value="Skills",
            ),
            rx.tabs.content(
                rx.text("Python Ecosystem content"),
                value="Python Ecosystem",
            ),
            rx.tabs.content(
                stack_grid,
                value="Tech Stack",
            ),
            default_value="Skills",
        ),
        width="100%",
    )

    skill_section = rx.box(
        rx.container(**INDEX_PAGE["SKILLS_CONTAINER_STYLE"]),
        rx.vstack(
            header,
            skills_radar,
            rx.center(stack, width="100%"),
            display=["none", "none", "none", "flex", "flex", "flex"],
        ),
        rx.vstack(
            header,
            skills_tabs,
            display=["flex", "flex", "flex", "none", "none", "none"],
        ),
    )

    return skill_section


@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """

    return rx.box(
        header(),
        intro(),
        skillsets_section(),
        width="100%",
        max_width="100%",
        overflow_x="hidden",
        **INDEX_PAGE["INDEX_PAGE_STYLE"],
    )
