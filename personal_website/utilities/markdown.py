from typing import Dict

import reflex as rx


def read_markdown(link: str, component_map: Dict = None, **kwargs) -> rx.Component:
    """Reads a markdown file and returns the reflex component."""
    with open(link, encoding="utf-8") as f:
        text = f.read()
    if component_map is None:
        return rx.markdown(text, **kwargs)
    return rx.markdown(text, component_map=component_map, **kwargs)
