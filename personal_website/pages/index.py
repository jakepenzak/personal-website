"""The home page of the website."""

import reflex as rx

from assets import asset_data
from personal_website.components.spline import spline_component_index_page
from personal_website.components.utilities.markdown import read_markdown
from personal_website.components.website_bar import website_bar
from personal_website.structural import styles, template


# Create the Home page
@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        rx.Component: The UI for the home page.
    """

    hero_mobile_background = rx.box(
        rx.box(
            position="absolute",
            inset="0",
            opacity="0.34",
            background=styles.theme_value(
                "radial-gradient(circle at 50% 18%, rgba(82,33,129,0.22) 0%, rgba(82,33,129,0) 58%),"
                "repeating-linear-gradient(0deg, rgba(82,33,129,0.12) 0px, rgba(82,33,129,0.12) 1px, rgba(255,255,255,0) 1px, rgba(255,255,255,0) 22px),"
                "repeating-linear-gradient(90deg, rgba(82,33,129,0.12) 0px, rgba(82,33,129,0.12) 1px, rgba(255,255,255,0) 1px, rgba(255,255,255,0) 22px)",
                "radial-gradient(circle at 50% 18%, rgba(168,124,255,0.24) 0%, rgba(168,124,255,0) 58%),"
                "repeating-linear-gradient(0deg, rgba(168,124,255,0.11) 0px, rgba(168,124,255,0.11) 1px, rgba(11,17,27,0) 1px, rgba(11,17,27,0) 22px),"
                "repeating-linear-gradient(90deg, rgba(168,124,255,0.11) 0px, rgba(168,124,255,0.11) 1px, rgba(11,17,27,0) 1px, rgba(11,17,27,0) 22px)",
            ),
            background_size="220% 220%",
            animation="heroPhase 22s ease-in-out infinite",
            filter="blur(0.9px)",
            pointer_events="none",
        ),
        rx.box(
            position="absolute",
            inset="-40px",
            opacity="0.32",
            background=styles.theme_value(
                "conic-gradient(from 0deg at 50% 40%, rgba(82,33,129,0.24) 0deg, rgba(82,33,129,0) 18deg, rgba(82,33,129,0.12) 36deg, rgba(82,33,129,0) 54deg, rgba(82,33,129,0.24) 72deg, rgba(82,33,129,0) 90deg, rgba(82,33,129,0.12) 108deg, rgba(82,33,129,0) 126deg, rgba(82,33,129,0.24) 144deg, rgba(82,33,129,0) 162deg, rgba(82,33,129,0.12) 180deg, rgba(82,33,129,0) 198deg, rgba(82,33,129,0.24) 216deg, rgba(82,33,129,0) 234deg, rgba(82,33,129,0.12) 252deg, rgba(82,33,129,0) 270deg, rgba(82,33,129,0.24) 288deg, rgba(82,33,129,0) 306deg, rgba(82,33,129,0.12) 324deg, rgba(82,33,129,0) 342deg, rgba(82,33,129,0.24) 360deg),"
                "repeating-radial-gradient(circle at 50% 40%, rgba(82,33,129,0.12) 0px, rgba(82,33,129,0.12) 1px, rgba(255,255,255,0) 1px, rgba(255,255,255,0) 18px)",
                "conic-gradient(from 0deg at 50% 40%, rgba(168,124,255,0.28) 0deg, rgba(168,124,255,0) 18deg, rgba(168,124,255,0.14) 36deg, rgba(168,124,255,0) 54deg, rgba(168,124,255,0.28) 72deg, rgba(168,124,255,0) 90deg, rgba(168,124,255,0.14) 108deg, rgba(168,124,255,0) 126deg, rgba(168,124,255,0.28) 144deg, rgba(168,124,255,0) 162deg, rgba(168,124,255,0.14) 180deg, rgba(168,124,255,0) 198deg, rgba(168,124,255,0.28) 216deg, rgba(168,124,255,0) 234deg, rgba(168,124,255,0.14) 252deg, rgba(168,124,255,0) 270deg, rgba(168,124,255,0.28) 288deg, rgba(168,124,255,0) 306deg, rgba(168,124,255,0.14) 324deg, rgba(168,124,255,0) 342deg, rgba(168,124,255,0.28) 360deg),"
                "repeating-radial-gradient(circle at 50% 40%, rgba(168,124,255,0.11) 0px, rgba(168,124,255,0.11) 1px, rgba(11,17,27,0) 1px, rgba(11,17,27,0) 18px)",
            ),
            filter="blur(1.0px)",
            pointer_events="none",
            transform_origin="50% 40%",
            animation="heroRotate 30s linear infinite",
        ),
        rx.vstack(
            header(),
            intro(),
            align="center",
            position="relative",
            z_index="1",
        ),
        position="relative",
        width="calc(100% + 4em)",
        margin_x="-2em",
        overflow="hidden",
        border_radius="0px",
        padding_top="2.5em",
        padding_bottom="0.5em",
        padding_x="2em",
        display=["block", "block", "none", "none", "none", "none"],
    )

    hero_desktop = rx.vstack(
        header(),
        intro(),
        align="center",
        display=["none", "none", "flex", "flex", "flex", "flex"],
        padding_top="2.5em",
        padding_bottom="0.5em",
    )

    return rx.vstack(
        hero_mobile_background,
        hero_desktop,
        weekly_pick_section(),
        skillsets_section(),
        website_bar(),
        min_height="80vh",
        overflow_x="hidden",
        max_width="100%",
        align="center",
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
                    color=[styles.theme_value("#522181", "#CFBCFF")],
                    align="center",
                    display=["none", "none", "flex", "flex", "flex", "flex"],
                ),
            ),
            rx.spacer(),
            spline_component_index_page(),
            display=["none", "none", "flex", "flex", "flex", "flex"],
            justify="between",
            align="center",
        ),
        rx.box(
            rx.center(
                rx.heading(
                    "Jacob \n Pieniazek",
                    size="9",
                    font_family="HackBold",
                    color=[styles.theme_value("#522181", "#CFBCFF")],
                    align="center",
                    text_shadow=styles.theme_value(
                        "0 1px 0 rgba(255,255,255,0.55)", "none"
                    ),
                ),
                width="100%",
                padding_y="0.75em",
            ),
            position="relative",
            width="100%",
            padding_top="0.5em",
            display=["flex", "flex", "none", "none", "none", "none"],
        ),
        justify="between",
        padding_top="0em",
        padding_bottom="3em",
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
        rx.vstack(
            rx.heading(
                "Welcome!",
                size="6",
                font_family="HackBold",
                align="center",
                padding_top="0.5em",
            ),
            align="center",
        )
    )

    body = rx.box(
        read_markdown(
            asset_data.INDEX_INTRO,
            component_map=styles.INDEX_PAGE["MARKDOWN_STYLE"],
        ),
        width=["100%", "100%", "100%", "100%", "75%", "75%"],
    )

    avatar = rx.link(
        rx.image(
            src=asset_data.INDEX_AVATAR,
            max_height="5em",
            max_width="5em",
            align="center",
            border_radius="50%",
            border="1px solid #555",
        ),
        href=asset_data.INDEX_AVATAR_URL,
        target="_blank",
    )

    intro = rx.box(
        rx.container(**styles.INDEX_PAGE["INTRO_CONTAINER_STYLE"]),
        rx.hstack(
            rx.vstack(
                rx.image(
                    src=asset_data.INDEX_PHOTO,
                    max_height="35em",
                    max_width="35em",
                    align="center",
                    border_radius="15px 50px",
                    border="1px solid #555",
                ),
                read_markdown(asset_data.INDEX_SPOTIFY, padding_bottom="1em"),
                avatar,
                max_width="35em",
                align="center",
            ),
            rx.vstack(
                welcome,
                body,
                padding_left="1em",
                align="center",
            ),
            padding_x="3em",
            display=["none", "none", "none", "flex", "flex", "flex"],
            align_items="center",
        ),
        rx.vstack(
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.image(
                src=asset_data.INDEX_PHOTO,
                height="flex",
                width="flex",
                max_height="25em",
                max_width="25em",
                align="center",
                border_radius="15px 50px",
                border="1px solid #555",
            ),
            read_markdown(asset_data.INDEX_SPOTIFY, padding_bottom="1em"),
            rx.spacer(),
            avatar,
            rx.box(rx.vstack(welcome, body, align="center")),
            padding_x="3em",
            display=["flex", "flex", "flex", "none", "none", "none"],
            align_items="center",
        ),
    )

    return intro


def weekly_pick_section() -> rx.Component:
    """Feature the current song pick without sending visitors away from the site."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.center(
                        rx.icon(tag="music", size=22),
                        width="2.75em",
                        height="2.75em",
                        border_radius="full",
                        bg=styles.theme_value("#F0EAFE", "#2A2240"),
                        color=styles.theme_value("#522181", "#D5C3FF"),
                    ),
                    rx.heading(
                        "Weekly song pick",
                        font_size=["1.25em", "1.4em", "1.6em"],
                        line_height="1.2",
                        height="auto",
                        padding_bottom="0",
                        text_align="left",
                    ),
                    spacing="3",
                    align="center",
                    width="auto",
                ),
                rx.link(
                    "Browse picks",
                    href="https://weekly-picks.jacob-pieniazek.com/",
                    is_external=True,
                    size="2",
                    color=styles.theme_value("#522181", "#D5C3FF"),
                    text_decoration="underline",
                    text_decoration_color=styles.theme_value("#B99CE0", "#786298"),
                ),
                justify="between",
                align="center",
                width="100%",
                wrap="wrap",
                spacing="3",
            ),
            rx.text(
                "A fresh track from my weekly rotation, updated each Monday.",
                size="2",
                color=styles.theme_value("#4C4858", "#B8C2D1"),
                width="100%",
            ),
            rx.box(
                rx.el.iframe(
                    src="https://weekly-picks.jacob-pieniazek.com/embed",
                    title="Jacob's weekly song pick",
                    loading="lazy",
                    allow="autoplay; clipboard-write; encrypted-media; picture-in-picture",
                    width="100%",
                    height=["460px", "420px", "380px", "360px"],
                    border="0",
                    display="block",
                ),
                width="100%",
                overflow="hidden",
                border_radius="12px",
                border=styles.theme_value("1px solid #E2D8F4", "1px solid #39455A"),
                bg=styles.theme_value("#FFFFFF", "#101722"),
            ),
            spacing="4",
            align="start",
        ),
        width="100%",
        max_width="880px",
        margin_top=["0.75em", "1em", "1.5em", "2em"],
        margin_bottom=["1em", "1.5em", "2em"],
        padding=["1.25em", "1.5em", "1.75em", "2em"],
        border_radius="18px",
        border=styles.theme_value("1px solid #E6DFF2", "1px solid #2E3A4D"),
        bg=styles.theme_value("rgba(255,255,255,0.82)", "rgba(18,26,39,0.88)"),
        box_shadow=styles.theme_value(
            "0 18px 45px rgba(82,33,129,0.10)", "0 20px 50px rgba(0,0,0,0.28)"
        ),
    )


## Skillsets Section


def skillsets_section() -> rx.Component:
    """Capability-focused skills section (no tool wall)."""

    header = rx.heading(
        """
        Focus Areas
        """,
        font_size="2em",
        font_family="HackBold",
        text_align="left",
        padding_top="1em",
        padding_bottom="0.25em",
    )

    intro = rx.text(
        "A quick focus map, plus my core strengths & what I tend to build day-to-day.",
        color=styles.theme_value("#2B2A33", "#C4CEDB"),
        padding_bottom="0.75em",
    )

    focus_map_radar = rx.center(
        rx.recharts.radar_chart(
            rx.recharts.radar(
                data_key="rating",
                stroke=styles.theme_value("#522181", "#CFBCFF"),
                fill=styles.theme_value("#522181", "#CFBCFF"),
                fill_opacity=0.35,
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="subject"),
            data=asset_data.SKILLS_DATA,
            width="100%",
            height="100%",
        ),
        width="95vw",
        height=["25vh", "25vh", "30vh", "35vh", "40vh", "45vh"],
        display=["none", "none", "none", "flex", "flex", "flex"],
    )

    focus_map_mobile = rx.vstack(
        *[
            rx.hstack(
                rx.text(row["subject"], size="2", width="60%"),
                rx.box(
                    rx.box(
                        width=f"{row['rating']}%",
                        height="8px",
                        bg=styles.theme_value("#522181", "#CFBCFF"),
                        border_radius="999px",
                    ),
                    width="40%",
                    bg=styles.theme_value("#E9D5FF", "#29233A"),
                    border_radius="999px",
                    overflow="hidden",
                ),
                width="100%",
                align="center",
                spacing="3",
            )
            for row in asset_data.SKILLS_DATA
        ],
        spacing="2",
        width="100%",
        padding_top="0.5em",
        display=["flex", "flex", "flex", "none", "none", "none"],
    )

    focus_map = rx.vstack(
        focus_map_mobile,
        focus_map_radar,
        padding_bottom="1.25em",
        width="100%",
    )

    core_strengths = rx.vstack(
        rx.text(
            "Core strengths",
            font_family="HackBold",
            color=styles.theme_value("#522181", "#CFBCFF"),
        ),
        *[
            rx.badge(
                s,
                radius="full",
                size="2",
                **_focus_area_badge_props(s),
            )
            for s in asset_data.CORE_STRENGTHS
        ],
        wrap="wrap",
        spacing="2",
        align="center",
        padding_bottom="1.5em",
    )

    languages = rx.vstack(
        rx.text(
            "Languages I work in",
            font_family="HackBold",
            color=styles.theme_value("#522181", "#CFBCFF"),
        ),
        rx.hstack(
            rx.badge(
                rx.hstack(
                    rx.icon(tag="code", size=16),
                    rx.text("Python"),
                    spacing="2",
                    align="center",
                ),
                radius="full",
                variant="soft",
                color_scheme="purple",
                size="2",
            ),
            rx.badge(
                rx.hstack(
                    rx.icon(tag="database", size=16),
                    rx.text("SQL"),
                    spacing="2",
                    align="center",
                ),
                radius="full",
                variant="soft",
                color_scheme="red",
                size="2",
            ),
            rx.badge(
                rx.hstack(
                    rx.icon(tag="cpu", size=16),
                    rx.text("Rust"),
                    spacing="2",
                    align="center",
                ),
                radius="full",
                variant="soft",
                color_scheme="brown",
                size="2",
            ),
            rx.badge(
                rx.hstack(
                    rx.icon(tag="bar-chart-2", size=16),
                    rx.text("R"),
                    spacing="2",
                    align="center",
                ),
                radius="full",
                variant="soft",
                color_scheme="orange",
                size="2",
            ),
            rx.badge(
                rx.hstack(
                    rx.icon(tag="terminal", size=16),
                    rx.text("Bash"),
                    spacing="2",
                    align="center",
                ),
                radius="full",
                variant="soft",
                color_scheme="green",
                size="2",
            ),
            rx.badge(
                rx.hstack(
                    rx.icon(tag="table", size=16),
                    rx.text("Stata"),
                    spacing="2",
                    align="center",
                ),
                radius="full",
                variant="soft",
                color_scheme="blue",
                size="2",
            ),
            wrap="wrap",
            spacing="2",
            align="center",
        ),
        spacing="2",
        align="center",
        padding_bottom="1.5em",
    )

    focus_grid = rx.grid(
        *[focus_area_card(area) for area in asset_data.PROFILE_FOCUS_AREAS],
        columns=rx.breakpoints(initial="1", md="2"),
        spacing="6",
        width="100%",
    )

    skill_section = rx.box(
        rx.container(**styles.INDEX_PAGE["SKILLS_CONTAINER_STYLE"]),
        rx.vstack(
            header,
            intro,
            focus_map,
            languages,
            core_strengths,
            focus_grid,
            padding_x=["0em", "0em", "1em", "2em", "3em", "3em"],
        ),
    )

    return skill_section


def _focus_area_badge_props(title: str) -> dict:
    """Return literal-friendly badge props for Reflex."""
    if title == "Causal Inference, Causal ML, & Econometrics":
        return {"color_scheme": "purple", "variant": "soft"}
    if title == "Statistical Learning, ML, & AI":
        return {"color_scheme": "blue", "variant": "soft"}
    if title == "MLOps / DevOps & Delivery / Package Development":
        return {"color_scheme": "orange", "variant": "soft"}
    if title == "Data Platforms & Analytics Engineering":
        return {"color_scheme": "green", "variant": "soft"}
    return {"color_scheme": "purple", "variant": "soft"}


def _focus_area_border_color(title: str):
    if title == "Causal Inference, Causal ML, & Econometrics":
        return styles.theme_value("#522181", "#CFBCFF")
    if title == "Statistical Learning, ML, & AI":
        return styles.theme_value("#2563eb", "#93C5FD")
    if title == "MLOps / DevOps & Delivery / Package Development":
        return styles.theme_value("#f97316", "#FDBA74")
    if title == "Data Platforms & Analytics Engineering":
        return styles.theme_value("#16a34a", "#86EFAC")
    return styles.theme_value("#522181", "#CFBCFF")


def focus_area_card(area: dict) -> rx.Component:
    badge_props = _focus_area_badge_props(area["title"])

    tools = rx.hstack(
        *[
            rx.badge(
                str(tool),
                radius="full",
                **badge_props,
            )
            for tool in area.get("tools", [])
        ],
        wrap="wrap",
        spacing="2",
        align="center",
    )

    highlights = rx.unordered_list(
        *[rx.list_item(h) for h in area.get("highlights", [])],
        padding_left="1.25em",
        margin_top="0.75em",
    )

    return rx.box(
        rx.vstack(
            rx.badge(
                area["title"],
                radius="full",
                size="3",
                **badge_props,
            ),
            rx.heading(
                area["title"],
                font_size="1.35em",
                font_family="HackBold",
                text_align="left",
                padding_bottom="0.25em",
            ),
            rx.text(area["tagline"], color=styles.theme_value("#2B2A33", "#C4CEDB")),
            highlights,
            rx.text(
                "Representative tools:",
                font_family="HackBold",
                color=styles.theme_value("#522181", "#CFBCFF"),
                padding_top="0.75em",
            ),
            tools,
            align="start",
        ),
        padding="1.5em",
        border=styles.theme_value("1px solid #e2e8f0", "1px solid #2E3A4D"),
        border_radius="lg",
        bg=styles.theme_value("rgba(255,255,255,0.75)", "rgba(18,26,39,0.88)"),
        box_shadow="sm",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-4px)",
            "box_shadow": "lg",
            "border_color": _focus_area_border_color(area["title"]),
        },
        width="100%",
    )
