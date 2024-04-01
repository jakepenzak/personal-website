import reflex as rx


def create_heading(heading_str: str, **style_props) -> rx.Component:
    """
    Create a heading component with the specified heading string and optional keyword arguments.

    Args:
        heading_str (str): The text to be displayed as the heading.
        **kwargs: Additional keyword arguments to customize the heading component.

    Returns:
        rx.Component: The created heading component.
    """

    style_props["font_size"] = (
        "4em" if "font_size" not in style_props else style_props["font_size"]
    )
    style_props["font_family"] = (
        "HackBold" if "font_family" not in style_props else style_props["font_family"]
    )
    style_props["text_align"] = (
        "center" if "text_align" not in style_props else style_props["text_align"]
    )
    style_props["color"] = (
        ["#522181"] if "color" not in style_props else style_props["color"]
    )
    style_props["padding_bottom"] = (
        "0.5em"
        if "padding_bottom" not in style_props
        else style_props["padding_bottom"]
    )
    style_props["display"] = (
        ["none", "none", "flex", "flex", "flex", "flex"]
        if "display" not in style_props
        else style_props["display"]
    )

    heading = rx.chakra.heading(
        heading_str,
        **style_props,
    )
    return heading
