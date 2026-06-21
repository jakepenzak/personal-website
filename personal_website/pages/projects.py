"""The projects page."""

import reflex as rx

from assets import asset_data
from personal_website.structural import template


# Create the projects page
@template(route="/projects", title="Projects")
def projects() -> rx.Component:
    """
    The projects page.

    Returns:
        rx.Component: The UI for the projects page.
    """
    return rx.vstack(
        header(),
        rx.divider(width="25%", border_top="1px solid rgba(0, 0, 0, 0.25)"),
        rx.spacer(),
        body(),
        rx.spacer(),
        rx.center(rx.image(src=asset_data.WEBSITE_FOOTER_IMAGE, width="100%")),
        align="center",
        min_height="80vh",
    )


## Header Section
def header():
    heading = rx.heading("Projects")

    header = rx.vstack(
        heading,
        align_items="center",
        padding_top=["1em", "1em", "2em", "2em", "2em", "2em"],
        padding_x=["1em", "1em", "2em", "2em", "2em", "2em"],
        max_height="100vh",
    )

    return header


def body():
    return rx.vstack(
        open_source_and_personal_projects(),
        rx.divider(
            width="80%",
            margin_y="3em",
        ),
        research_and_presentations(),
        align="center",
        spacing="6",
        max_width="1200px",
        margin="0 auto",
        padding_x="2em",
    )


def get_status_badge_config(status: str) -> dict:
    """Get badge configuration (color_scheme and variant) for a given status."""
    # Status mappings with color schemes and variants
    status_configs = {
        "Beta": {"color_scheme": "blue", "variant": "soft"},
        "Alpha": {"color_scheme": "blue", "variant": "outline"},
        "Pre-Alpha": {"color_scheme": "blue", "variant": "outline"},
        "Stable": {"color_scheme": "jade", "variant": "soft"},
        "Inactive": {"color_scheme": "gray", "variant": "outline"},
        "Learning Project": {"color_scheme": "teal", "variant": "soft"},
        "Portfolio": {"color_scheme": "purple", "variant": "soft"},
    }

    # Return config or default if status not found
    return status_configs.get(status, {"color_scheme": "gray", "variant": "soft"})


def get_status_description(status: str) -> str:
    """Get a descriptive tooltip or additional info for a status."""
    descriptions = {
        "Beta": "Baseline feature-complete, in testing phase",
        "Alpha": "Early development phase",
        "Pre-Alpha": "Pre-release development phase",
        "Stable": "Mature and reliable release",
        "Inactive": "Project is no longer maintained",
        "Learning Project": "Project is for educational purposes",
        "Portfolio": "Project is for showcasing personal work",
    }
    return descriptions.get(status, f"Status: {status}")


def create_status_badge(status: str, show_description: bool = False) -> rx.Component:
    """Create an enhanced status badge with optional description tooltip."""
    if not status:
        return rx.fragment()

    config = get_status_badge_config(status)
    badge = rx.badge(status, **config)

    if show_description:
        description = get_status_description(status)
        return rx.tooltip(badge, content=description)

    return badge


def project_card(
    title: str,
    image_src: str,
    description: str,
    github_url: str = "",
    docs_url: str = "",
    tech_stack=None,
    status=None,
) -> rx.Component:
    """Create a project card with enhanced information."""

    # Action buttons
    buttons = rx.hstack(
        rx.cond(
            github_url,
            rx.link(
                rx.button("GitHub", variant="outline", size="2"),
                href=github_url,
                is_external=True,
            ),
        ),
        rx.cond(
            docs_url,
            rx.link(
                rx.button("Docs", size="2"),
                href=docs_url,
                is_external=True,
            ),
        ),
        spacing="2",
    )

    # Tech stack badges
    tech_badges = rx.cond(
        tech_stack,
        rx.hstack(
            *[rx.badge(tech, variant="soft", size="1") for tech in (tech_stack or [])],
            spacing="1",
        ),
    )

    status_badges = rx.cond(
        status,
        rx.hstack(
            *[
                create_status_badge(status, show_description=True)
                for status in (status or [])
            ],
            spacing="1",
        ),
    )

    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src=image_src,
                    height="120px",
                    object_fit="contain",
                    max_width="200px",
                ),
                padding="1em",
            ),
            rx.vstack(
                rx.spacer(),
                rx.text(
                    title,
                    size="6",
                    color="#522181",
                    text_align="center",
                ),
                status_badges,
                rx.text(
                    description,
                    size="2",
                    text_align="center",
                ),
                tech_badges,
                buttons,
                spacing="3",
                align="center",
            ),
            spacing="4",
            align="center",
        ),
        padding="1.5em",
        max_width="350px",
        min_height="450px",
        border="1px solid #e2e8f0",
        border_radius="lg",
        _hover={"transform": "translateY(-4px)", "box_shadow": "lg"},
        transition="all 0.3s ease",
        align="center",
    )


def research_card(
    title: str,
    year: str,
    type_: str,
    link: str = "",
    repo: str = "",
    abstract: str = "",
) -> rx.Component:
    """Create a research publication card."""

    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.badge(
                    type_,
                    variant="soft",
                    color_scheme="blue",
                ),
                rx.badge(year, variant="outline"),
                spacing="2",
                justify="between",
                width="100%",
            ),
            rx.text(
                title,
                size="4",
                color="#522181",
                text_align="left",
                width="100%",
            ),
            rx.cond(
                abstract,
                rx.text(abstract, size="2", color="gray"),
            ),
            rx.cond(
                link or repo,
                rx.hstack(
                    rx.cond(
                        link,
                        rx.link(
                            rx.button("View PDF", variant="ghost", size="2"),
                            href=link,
                            is_external=True,
                        ),
                    ),
                    rx.cond(
                        link and repo,
                        rx.spacer(),
                    ),
                    rx.cond(
                        repo,
                        rx.link(
                            rx.button("GitHub", variant="ghost", size="2"),
                            href=repo,
                            is_external=True,
                        ),
                    ),
                ),
            ),
        ),
        padding="1.5em",
        border="1px solid #e2e8f0",
        border_radius="lg",
        width="100%",
        max_width="800px",
        _hover={"transform": "translateY(-4px)", "box_shadow": "lg"},
        transition="all 0.3s ease",
        align="center",
    )


def open_source_and_personal_projects() -> rx.Component:
    title = rx.heading(
        "Open Source & Personal Projects",
        font_size=rx.breakpoints(initial="1.5em", md="1.8em"),
    )

    description = rx.text(
        "Various projects, including open-source libraries and miscellaneuos personal projects.",
        text_align="center",
        color="gray.600",
        max_width="600px",
        padding_bottom="1em",
    )

    # Project cards in a grid
    # TODO: Move metadata to asset_data like articles.
    projects_grid = rx.box(
        rx.grid(
            project_card(
                title="CaML",
                image_src="https://raw.githubusercontent.com/jakepenzak/caml/main/docs/assets/main_logo.svg",
                description="A comprehensive Python library for causal machine learning, providing easy-to-use implementations of cutting-edge & traditional causal inference/econometric methods.",
                github_url="https://github.com/jakepenzak/caml",
                docs_url="https://caml-docs.com",
                tech_stack=["Python", "Causal Inference/Econometrics", "ML"],
                status=["Pre-Alpha"],
            ),
            project_card(
                title="NetBeat",
                image_src="https://raw.githubusercontent.com/jakepenzak/netbeat/main/docs/assets/netbeat.webp",
                description="A high-performance network speed testing tool written in Rust, designed for real-time network analysis and diagnostics.",
                github_url="https://github.com/jakepenzak/netbeat",
                docs_url="https://crates.io/crates/netbeat",
                tech_stack=["Rust", "Networking", "CLI"],
                status=["Beta", "Learning Project"],
            ),
            project_card(
                title="Personal Website",
                image_src=asset_data.NAVBAR_LOGO,
                description="A modern personal website built with Reflex framework, featuring responsive design, dynamic content management, and interactive components.",
                github_url="https://github.com/jakepenzak/personal-website",
                tech_stack=["Python", "Reflex", "Markdown", "Marimo"],
                status=["Portfolio"],
            ),
            project_card(
                title="LiteLLM Pulse",
                image_src="https://raw.githubusercontent.com/jakepenzak/litellm-pulse/main/assets/litellm-pulse.svg",
                description="A lightweight metrics exporter for LiteLLM that scrapes Prometheus metrics, stores time-series data in SQLite, and exposes clean JSON via a REST API for dashboard and home-automation widgets.",
                github_url="https://github.com/jakepenzak/litellm-pulse",
                tech_stack=["Python", "FastAPI", "SQLite", "Docker"],
                status=["Beta"],
            ),
            columns=rx.breakpoints(initial="1", md="2"),
            spacing="6",
            width="100%",
            justify="center",
        )
    )

    return rx.vstack(
        title,
        description,
        projects_grid,
        align="center",
        spacing="6",
        width="100%",
    )


def research_and_presentations() -> rx.Component:
    title = rx.heading(
        "Research & Formal Presentations",
        font_size=rx.breakpoints(initial="1.5em", md="1.8em"),
    )

    description = rx.text(
        "Formal research papers and presentations in academic and industry settings.",
        text_align="center",
        color="gray.600",
        max_width="600px",
        padding_bottom="1em",
    )

    # Research cards
    research_items = rx.vstack(
        rx.spacer(),
        research_card(
            title="Causal Machine Learning in Practice: Estimating Average and Heterogeneous Effects for Personalized Treatment.",
            year="2026",
            type_="Seminar Talk",
            link=asset_data.BROWN_BAG_PATH,
            repo="https://github.com/jakepenzak/causal-ml-brown-bag",
            abstract='A "brown-bag" talk that builds from classical econometrics intuition (Frisch-Waugh-Lovell, potential outcomes) through modern semi-parametric methods (Double/Debiased ML, meta-learners) and CATE estimation techniques, and landing on practical marketing applications like audience selection and coupon targeting. The goal is to make these methods feel like a natural extension of what an econometrics-trained student already knows.',
        ),
        research_card(
            title="High, But Not Happy? The Impact of Cannabis Consumption on Mental Health",
            year="2022",
            type_="Master's Thesis",
            link=asset_data.THESIS_LINK,
            abstract="An econometric analysis examining the causal relationship between cannabis consumption and mental health outcomes using advanced econometric techniques and longitudinal data analysis.",
        ),
        research_card(
            title="Particule Happiness: How Air Pollution is Effecting Our Mental Health",
            year="2021",
            type_="Undergraduate Thesis",
            abstract="A comprehensive study investigating the impact of air pollution on mental health outcomes using econometric modeling and environmental data analysis with geospatial techniques.",
        ),
        spacing="4",
        width="100%",
        align="center",
    )

    return rx.vstack(
        title,
        description,
        research_items,
        align="center",
        spacing="6",
        width="100%",
    )
