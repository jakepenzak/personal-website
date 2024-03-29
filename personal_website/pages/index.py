"""The home page of the website."""
import reflex as rx
from typing import Tuple
from personal_website.components.spline import spline_component_index_page
from personal_website.styles import INDEX_PAGE
from personal_website.templates import template
from personal_website.utilities.markdown import read_markdown
from assets.asset_data import (
    skills_data,
    tech_logos_dict,
    library_logos_dict,
)
from personal_website.utilities.container import container


# Create the Home page
@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        rx.Component: The UI for the home page.
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


## Helper functions
def image_link(src: str, href: str) -> rx.Component:
    """
    Creates a link with an image.

    Args:
        src (str): The source URL of the image.
        href (str): The URL that the link should navigate to.

    Returns:
        rx.Component: The link component with the specified image source and target URL.
    """
    return rx.link(rx.image(src=src), href=href, target="_blank")


## Header Section
def header() -> rx.Component:
    """
    The header section of the home page.

    Returns:
        rx.Component: The header component.
    """

    header = container(
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

    return header


## Introduction Section
def intro() -> rx.Component:
    """
    The introduction section of the home page.

    Returns:
        rx.Component: The rendered introduction section.
    """

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


## Skillsets Section
def skillsets_section() -> rx.Component:
    """
    Returns a component representing the skillsets section of the personal website.

    This section includes a heading, a radar chart displaying skill ratings,
    a section for libraries, and a section for the tech stack. The layout of
    the sections is responsive, adapting to different screen sizes.

    Returns:
        rx.Component: The skillsets section component.
    """
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

    (
        libraries_header,
        libraries_intro,
        libraries_grid,
        libraries,
    ) = create_libraries_section()

    stack_header, stack_intro, stack_grid, tech_stack = create_tech_stack_section()

    # Used for mobile and tablet view
    skills_tabs = create_skills_tabs(
        **{
            "libraries_intro": libraries_intro,
            "libraries_grid": libraries_grid,
            "stack_intro": stack_intro,
            "stack_grid": stack_grid,
        }
    )

    skill_section = rx.box(
        rx.container(**INDEX_PAGE["SKILLS_CONTAINER_STYLE"]),
        rx.vstack(
            header,
            skills_radar,
            rx.hstack(
                libraries,
                tech_stack,
                padding_x="3em",
                width="100%",
            ),
            display=["none", "none", "none", "flex", "flex", "flex"],
        ),
        rx.vstack(
            header,
            skills_tabs,
            display=["flex", "flex", "flex", "none", "none", "none"],
        ),
    )

    return skill_section


def create_libraries_section() -> Tuple[rx.Component]:
    """
    Creates a section for displaying Python libraries.

    Returns:
        Tuple[rx.Component]: A tuple containing the header, intro, grid, and the entire libraries section.
    """
    libraries_header = rx.heading(
        """
            Python Libraries
            """,
        font_size="1.5em",
        font_family="HackBold",
        text_align="center",
        padding_top="1em",
    )

    libraries_intro = rx.text(
        """Below is a selection of some of the python libraries 
                I use or have used in my personal & professional work. This list is by no means exhaustive,
                but it does cover a subset of the core libraries I consider myself to be moderately to highly proficient in."""
    )

    libraries_grid = rx.grid(
        *[
            image_link(library_logos_dict[lib].asset_path, library_logos_dict[lib].link)
            for lib in list(library_logos_dict.keys())
        ],
        columns="6",
        spacing="4",
        align="center",
        justify="center",
        padding_y="2em",
    )

    libraries = rx.center(
        rx.vstack(
            libraries_header,
            libraries_intro,
            libraries_grid,
        ),
        padding_x="3em",
        width="100%",
    )

    return libraries_header, libraries_intro, libraries_grid, libraries


def create_tech_stack_section() -> Tuple[rx.Component]:
    """
    Create a section displaying the tech stack and tools used.

    Returns:
        Tuple[rx.Component]: A tuple containing the components of the tech stack section.
    """
    stack_header = rx.heading(
        """
            Tech Stack & Tools
            """,
        font_size="1.5em",
        font_family="HackBold",
        text_align="center",
        padding_top="1em",
    )

    stack_intro = rx.text(
        """Similarly, below is a selection of some of the tech
                stack & tools that I use or have used in my personal & professional work."""
    )

    stack_grid = rx.grid(
        *[
            image_link(tech_logos_dict[t].asset_path, tech_logos_dict[t].link)
            for t in list(tech_logos_dict.keys())
        ],
        columns="5",
        spacing="4",
        align="center",
        justify="center",
        padding_y="4em",
    )

    tech_stack = rx.center(
        rx.vstack(
            stack_header,
            stack_intro,
            stack_grid,
        ),
        padding_x="3em",
        width="100%",
    )

    return stack_header, stack_intro, stack_grid, tech_stack


def create_skills_tabs(**kwargs) -> rx.Component:
    """
    Creates a tabbed component for displaying skills, Python libraries, and tech stack.

    Args:
        **kwargs: Additional keyword arguments to pass to the tabbed component.

    Returns:
        rx.Component: The tabbed component for displaying skills, Python libraries, and tech stack.
    """

    libraries_intro = kwargs.get("libraries_intro")
    libraries_grid = kwargs.get("libraries_grid")
    stack_intro = kwargs.get("stack_intro")
    stack_grid = kwargs.get("stack_grid")

    ## Used for mobile and tablet view
    skills_list = rx.unordered_list(
        *[rx.list_item(skill) for skill in [d["subject"] for d in skills_data]]
    )

    skills_tabs = rx.center(
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Skills", value="Skills"),
                rx.tabs.trigger("Python Libraries", value="Python Libraries"),
                rx.tabs.trigger("Tech Stack", value="Tech Stack"),
                size="2",
            ),
            rx.tabs.content(
                skills_list,
                padding_y="1em",
                value="Skills",
            ),
            rx.tabs.content(
                libraries_intro,
                libraries_grid,
                padding_y="1em",
                value="Python Libraries",
            ),
            rx.tabs.content(
                stack_intro,
                stack_grid,
                padding_y="1em",
                value="Tech Stack",
            ),
            default_value="Skills",
        ),
        width="100%",
    )

    return skills_tabs
