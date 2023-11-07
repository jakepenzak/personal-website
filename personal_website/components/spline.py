import reflex as rx
from reflex.vars import Var


# INDEX PAGE SPLINE
class Spline_Index(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = "https://prod.spline.design/kbccWev3xSCWPj50/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]


spline_index = Spline_Index.create


def spline_component_index_page():
    return rx.center(
        rx.center(
            spline_index(),
            width="20em",
            height="30em",
        ),
        width="100%",
        display=["none", "none", "none", "none", "flex", "flex"],
    )


# WAVEFORM SPLINE (ORIGINALLY FOR 404 PAGE ONLY)
class Spline_404(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = "https://prod.spline.design/1aLRYs1ebANWox51/scene.splinecode"
    is_default = True
    lib_dependencies: list[str] = ["@splinetool/runtime"]


spline_404 = Spline_404.create


def spline_component_404():
    return rx.box(
        spline_404(),
        display="flex",
        min_width="100%",
        max_width="100%",
        overflow_x="hidden",
    )
