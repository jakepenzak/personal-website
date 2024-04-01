import reflex as rx


def page_vstack(*children: rx.Component, **style_props) -> rx.Component:
    """
    Create a vertical stack of components for a page.

    Args:
        *children: The components to stack vertically.
        **style_props: Additional keyword arguments to customize the vertical stack.

    Returns:
        rx.Component: The vertical stack of components.
    """

    style_props["position"] = (
        "relative" if "position" not in style_props else style_props["position"]
    )
    style_props["min_height"] = (
        "80vh" if "min_height" not in style_props else style_props["min_height"]
    )
    style_props["width"] = (
        "100%" if "width" not in style_props else style_props["width"]
    )
    style_props["max_width"] = (
        "100%" if "max_width" not in style_props else style_props["max_width"]
    )
    style_props["overflow_x"] = (
        "hidden" if "overflow_x" not in style_props else style_props["overflow_x"]
    )

    return rx.chakra.vstack(*children, **style_props)
