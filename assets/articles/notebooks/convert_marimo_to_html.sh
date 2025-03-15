#!/bin/bash

for file in $(find assets/articles/notebooks -name "*.py"); do
    echo "Converting $file to HTML"
    base_name=$(basename "$file" .py)
    output_file="assets/articles/notebooks/html/$base_name.html"
    marimo export html "$file" -o "$output_file"
    echo "Converted $file to HTML ($output_file)"
done
