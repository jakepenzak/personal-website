#!/bin/bash

for file in $(find assets/notebooks -name "*.py"); do
    echo "Converting $file to HTML"
    base_name=$(basename "$file" .py)
    output_file="assets/notebooks/html/$base_name.html"
    marimo export html $file -o "$output_file"
    echo "Converted $file to HTML ($output_file)"
done
