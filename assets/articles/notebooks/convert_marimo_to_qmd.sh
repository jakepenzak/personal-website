#!/bin/bash

for file in $(find assets/articles/notebooks -name "*.py"); do
    echo "Converting $file to HTML"
    base_name=$(basename "$file" .py)
    output_file_ipynb="assets/articles/notebooks/$base_name.ipynb"
    output_file_qmd="assets/articles/notebooks/$base_name.qmd"
    marimo export ipynb "$file" -o "$output_file_ipynb" --force
    quarto convert "$output_file_ipynb" --output "$output_file_qmd"
    sed -i "/^jupyter: python3$/a toc: true" "$output_file_qmd"
    quarto render "$output_file_qmd" --to html --output "$base_name.html"
    mv "$base_name.html" assets/articles/notebooks/html/
    mv -r "assets/articles/notebooks/${base_name}_files" assets/articles/notebooks/html/
    echo "Converted $file to HTML at ../html/$base_name.html"
done
