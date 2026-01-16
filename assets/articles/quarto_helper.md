# Default Header
```markdown
---
title: ""
jupyter: python3
toc: true
format:
  live-html:
    theme: journal
    css: article_cover.css
execute:
  cache: true
highlight-style: github
---

``{python}
#| echo: false
#| output: asis

import sys
sys.path.insert(0, "..")

from html_helpers import parallax_split_cover

parallax_split_cover(
    cover_image="cover.webp",
    kicker="Econometrics • Regression Geometry",
    title='Controlling for "X"',
    subtitle="Understand linear regression mechanics via the Frisch–Waugh–Lovell Theorem.",
    chips=("Partialling Out", "Orthogonalization", "Interpretation"),
    takeaways=(
        '"Control for X" means removing the part of T and y explained by X.',
        "Regressing residuals y* on T* gives the same slope as full OLS.",
        "You can visualize 'all else equal' with a clean residual plot.",
    ),
    equation_latex=r"y^* = \beta\,T^* + \varepsilon",
)
``
```

# Quarto Live for Python with Pyodide

1. Install `quarto add r-wasm/quarto-live`
2. Check out quarto docs [here](https://quarto.org/docs/interactive/widgets/jupyter.html)


Example qmd file:

```markdown
---
title: Python Example
format: live-html
execute:
  cache: true
---

``{pyodide}
#| caption: "Calculating squares of numbers from 0 to 4"
for x in range(5):
  print(x ** 2)
``
```

# Code Example with code folding

```markdown
``{python}
#| code-fold: show (Can be true, false, or show)
#| code-summary: "Show the code"
import numpy as np
data = np.random.rand(5)
data.mean()
``
```
