#!/bin/bash

find assets/articles/notebooks -name "*.py" | parallel -j 4 '
    file={}
    echo "Converting $file to HTML"
    base_name=$(basename "$file" .py)
    output_file="assets/articles/notebooks/html/$base_name.html"
    rm $output_file || true
    marimo export html "$file" -o "$output_file"
    echo "Converted $file to HTML ($output_file)"
'
