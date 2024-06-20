"""The home page of the website."""
import reflex as rx
from typing import Tuple
from personal_website.components.spline import spline_component_index_page
from personal_website.structural import styles
from personal_website.structural import template
from personal_website.components.utilities.markdown import read_markdown
from assets import asset_data


# Create the Home page
@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        rx.Component: The UI for the home page.
    """

    return rx.vstack(
        header(),
        intro(),
        skillsets_section(),
        min_height="80vh",
        overflow_x="hidden",
        max_width="100%",
        align="center",
        padding_top= "2.5em",
        padding_bottom="3.5em",
        padding_x="2em",
    )


## Header Section
def header() -> rx.Component:
    """
    The header section of the home page.

    Returns:
        rx.Component: The header component.
    """

    header = rx.container(
        rx.hstack(
            rx.center(
                rx.heading(
                    "Jacob \n Pieniazek",
                    size="9",
                    font_family="HackBold",
                    color=["#522181"],
                    align="center",
                    display = ["none", "none", "flex", "flex", "flex", "flex"]
                ),
            ),
            rx.spacer(),
            spline_component_index_page(),
            display=["none", "none", "flex", "flex", "flex", "flex"],
            justify="between",
            align="center",
        ),
        rx.hstack(
            rx.heading(
                    "Jacob \n Pieniazek",
                    size="9",
                    font_family="HackBold",
                    color=["#522181"],
                    align="center",
                    display = ["flex", "flex", "none", "none", "none", "none"]
                ),
                display=["flex", "flex", "none", "none", "none", "none"],
                align="center",
                justify="center",
            ),
        justify="between",
        padding_top= "2em",
        padding_bottom= "6em",
        align="center",
        width="100%",
        height="100%",
    )

    return header


## Introduction Section
def intro() -> rx.Component:
    """
    The introduction section of the home page.

    Returns:
        rx.Component: The rendered introduction section.
    """

    welcome = rx.center(
        rx.heading(
            "Welcome!",
            size="6",
            font_family="HackBold",
            align="center",
            padding_top="1em",
            display="flex",
        )
    )

    body = read_markdown(
        asset_data.INDEX_INTRO,
        component_map=styles.INDEX_PAGE["MARKDOWN_STYLE"],
    )

    intro = rx.box(
        rx.container(**styles.INDEX_PAGE["INTRO_CONTAINER_STYLE"]),
        rx.hstack(
            rx.image(
                src=asset_data.INDEX_PHOTO,
                max_height="35em",
                max_width="35em",
                align="center",
            ),
            rx.vstack(welcome, body, padding_left="12em", align="center"),
            padding_x="5em",
            display=["none", "none", "none", "flex", "flex", "flex"],
            align_items="center",
        ),
        rx.vstack(
            rx.image(
                src=asset_data.INDEX_PHOTO,
                height="flex",
                width="flex",
                max_height="25em",
                max_width="25em",
                align="center",
            ),
            rx.box(rx.vstack(welcome, body, align="center")),
            padding_x="3em",
            display=["flex", "flex", "flex", "none", "none", "none"],
            align_items="center",
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
            data=asset_data.SKILLS_DATA,
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
        rx.container(**styles.INDEX_PAGE["SKILLS_CONTAINER_STYLE"]),
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

    libraries_intro = rx.text(asset_data.LIBRARY_INTRO_TXT)

    libraries_grid = rx.grid(
        *[
            image_link(
                asset_data.LIBRARY_LOGOS_META_DICT[lib].asset_path,
                asset_data.LIBRARY_LOGOS_META_DICT[lib].link,
            )
            for lib in list(asset_data.LIBRARY_LOGOS_META_DICT.keys())
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

    stack_intro = rx.text(asset_data.TECH_INTRO_TXT)

    stack_grid = rx.grid(
        *[
            image_link(
                asset_data.TECH_LOGOS_META_DICT[t].asset_path,
                asset_data.TECH_LOGOS_META_DICT[t].link,
            )
            for t in list(asset_data.TECH_LOGOS_META_DICT.keys())
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
        *[
            rx.list_item(skill)
            for skill in [d["subject"] for d in asset_data.SKILLS_DATA]
        ]
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
