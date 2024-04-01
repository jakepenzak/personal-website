import reflex as rx


def container(*children, **kwargs) -> rx.Component:
    """
    A function that creates a container component with optional customizations.

    Args:
        *children: Variable-length argument list of child components.
        **kwargs: Keyword arguments for customizing the container component.

    Returns:
        rx.Component: An instance of the container component.
    """
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return rx.chakra.container(
        *children,
        **kwargs,
    )
