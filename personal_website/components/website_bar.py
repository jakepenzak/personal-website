"""Theme-aware decorative point wave used at page boundaries."""

import math

import reflex as rx

from personal_website.structural import styles


def website_bar() -> rx.Component:
    """Render a responsive point field that expands subtly on hover."""
    points = []
    point_count = 42

    for band in range(3):
        for index in range(point_count):
            progress = index / (point_count - 1)
            phase = progress * math.tau * 2.2
            center = 50 + math.sin(progress * math.tau * 1.35) * 6
            amplitude = 7 + band * 5
            top = center + math.sin(phase + band * 1.7) * amplitude
            top += math.cos(phase * 1.8 - band) * 2.5
            size = 2.2 + ((index + band * 3) % 5) * 0.32
            shift = math.sin(phase * 0.8 + band * 1.3) * (9 + band * 4)

            points.append(
                rx.box(
                    class_name="data-wave-point",
                    left=f"{progress * 100:.2f}%",
                    top=f"{top:.2f}%",
                    width=f"{size:.2f}px",
                    height=f"{size:.2f}px",
                    opacity=f"{0.42 + band * 0.18:.2f}",
                    style={
                        "--wave-shift": f"{shift:.2f}px",
                        "--wave-delay": f"{(index % 9) * 8}ms",
                    },
                )
            )

    return rx.box(
        *points,
        class_name="data-wave-bar",
        color=styles.theme_value("#522181", "#CFBCFF"),
        width="100%",
        aria_hidden="true",
    )
