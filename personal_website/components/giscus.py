import reflex as rx


class Giscus(rx.Component):
    """Giscus component."""

    # The name of the npm package.
    library = "@giscus/react"
    tag = "Giscus"

    is_default = True

    repo: rx.Var[str]
    repoId: rx.Var[str]
    category: rx.Var[str]
    categoryId: rx.Var[str]
    mapping: rx.Var[str]
    term: rx.Var[str]
    reactionsEnabled: rx.Var[str]
    emitMetadata: rx.Var[str]
    inputPosition: rx.Var[str]
    theme: rx.Var[str]
    lang: rx.Var[str]
    loading: rx.Var[str]


# Convenience function to create the Spline component.
giscus = Giscus.create
