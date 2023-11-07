import reflex as rx
from reflex.vars import Var


# Index Page
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

# 404 Page
class Spline_404(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = "https://prod.spline.design/u5fHIlJ9qv8hrukB/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]

spline_404 = Spline_404.create
def spline_component_404():
    return rx.center(
        rx.center(
            spline_404(),
            width="100%",
            height="30em",
        ),
        width="100%",
        display=["flex", "flex", "flex", "flex", "flex", "flex"],
    )