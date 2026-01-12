# Default Header
```markdown
---
title: ""
jupyter: python3
toc: true
format:
  live-html:
    theme: journal
    include-in-header:
      - text: |
          <style>
          .quarto-title-block, .quarto-title-banner {
            display: none !important;
          }
          </style
execute:
  cache: true
highlight-style: github
---
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
