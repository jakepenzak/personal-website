import reflex as rx

##NOTE: Currently not in use, but can be used for future development on backend


class State(rx.State):
    """The base state."""

    @rx.var
    def current_page(self) -> str:
        """The current page."""
        page = self.router_data.get("headers", {}).get(
            "origin", ""
        ) + self.router_data.get("asPath", "")
        return page
