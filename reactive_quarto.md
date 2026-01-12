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

``{python}
import numpy as np
data = np.random.rand(5)
data.mean()
``
```
