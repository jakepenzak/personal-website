import reflex as rx
from reflex.vars import Var

# 404 Page
class Spline(rx.Component):
    """Spline component."""

    library = "@splinetool/react-spline"
    tag = "Spline"
    scene: Var[str] = "https://prod.spline.design/u5fHIlJ9qv8hrukB/scene.splinecode"
    is_default = True

    lib_dependencies: list[str] = ["@splinetool/runtime"]

def spline_component_404():
    return rx.center(
        rx.center(
            Spline().create,
            width="100%",
            height="30em",
        ),
        width="100%",
        display=["none", "none", "none", "none", "flex", "flex"],
    )