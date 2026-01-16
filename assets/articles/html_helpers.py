"""Reusable article cover components for Quarto documents."""

from __future__ import annotations

import html
from typing import Iterable

from IPython.display import HTML, display

_PARALLAX_JS = """
<script>
// Lightweight parallax: ties background translate to scroll position.
(() => {
  if (window.__fwlCoverParallaxBound) return;
  window.__fwlCoverParallaxBound = true;

  const el = document.querySelector('.fwl-cover');
  if (!el) return;

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return;

  let raf = null;
  const update = () => {
    raf = null;
    const rect = el.getBoundingClientRect();
    const viewH = window.innerHeight || 1;
    const progress = (viewH - rect.top) / (viewH + rect.height);
    const clamped = Math.max(0, Math.min(1, progress));
    const offset = (clamped - 0.5) * 36;
    el.style.setProperty('--parallax', offset.toFixed(2) + 'px');
  };

  const onScroll = () => {
    if (raf) return;
    raf = window.requestAnimationFrame(update);
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  update();
})();
</script>
"""


def parallax_split_cover(
    *,
    cover_image: str,
    kicker: str,
    title: str,
    subtitle: str,
    chips: Iterable[str] = (),
    takeaways: Iterable[str] = (),
    equation_latex: str | None = None,
) -> None:
    """
    Display a parallax split cover for a Quarto article.

    Call this function in a Python code block with `#| echo: false`.
    It uses IPython.display.HTML so Quarto renders it as raw HTML.

    NOTE: You must include the shared CSS in your YAML frontmatter:
        format:
          live-html:
            css: ../article_cover.css

    Parameters
    ----------
    cover_image : str
        Relative path to the cover image (e.g., "cover.webp").
    kicker : str
        Small uppercase text above the title (e.g., "Econometrics • ML").
    title : str
        The main title text.
    subtitle : str
        Subtitle text (can include basic HTML like <strong>).
    chips : Iterable[str]
        Topic chips/tags to display below the subtitle.
    takeaways : Iterable[str]
        Key takeaway bullet points for the right panel.
    equation_latex : str, optional
        LaTeX equation to display at the bottom of the panel.
    """
    chip_html = "".join(
        f'<span class="fwl-chip">{html.escape(chip)}</span>' for chip in chips
    )

    takeaways_html = "".join(
        f'<div class="fwl-metric">'
        f'<div class="num">{i}</div>'
        f'<div class="txt">{html.escape(text)}</div>'
        f"</div>"
        for i, text in enumerate(takeaways, start=1)
    )

    eq_html = (
        f'<div class="fwl-eq">\\[\\; {equation_latex} \\;\\]</div>'
        if equation_latex
        else ""
    )

    cover_html = f"""
<div class="fwl-cover" style="--cover-url: url('{html.escape(cover_image)}');">
  <div class="fwl-grain"></div>
  <div class="fwl-cover-inner">
    <div class="fwl-lead">
      <div class="fwl-kicker">{html.escape(kicker)}</div>
      <h1 class="fwl-title">{html.escape(title)}</h1>
      <p class="fwl-subtitle"><strong>{subtitle}</strong></p>
      <div class="fwl-chiprow">{chip_html}</div>
    </div>

    <div class="fwl-panel">
      <h3>Key Takeaways</h3>
      {takeaways_html}
      {eq_html}
    </div>
  </div>
</div>
{_PARALLAX_JS}
"""

    display(HTML(cover_html))
