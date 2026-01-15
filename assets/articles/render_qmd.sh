#!/bin/bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
search_dir="$script_dir"

find "$search_dir" -type f -name "*.qmd" -print0 |
while IFS= read -r -d '' file; do
    # if "_extensions" in path, skip
    if [[ "$file" == *"_extensions"* ]]; then
        echo "Skipping extension file: $file"
        echo "---"
        continue
    fi

    echo "Processing: $file"

    base_name="$(basename "$file" .qmd)"
    output_dir="$script_dir/$base_name"
    output_file_html="$output_dir/$base_name.html"

    # If HTML already exists, prompt the user. When the while-loop input comes from a pipe,
    # normal stdin is the pipe; read from /dev/tty to ensure the prompt reads from the terminal.
    if [ -f "$output_file_html" ]; then
        echo "HTML file already exists: $output_file_html"
        if [ -r /dev/tty ]; then
            # read a single char answer from the terminal
            read -r -n 1 -p "Regenerate? (y/n): " REPLY </dev/tty
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                echo "Skipping $file"
                echo "---"
                continue
            fi
        else
            # No interactive terminal available; skip by default.
            echo "No terminal available; skipping regeneration for $file"
            echo "---"
            continue
        fi
    fi

    # Render the QMD to HTML inside the output directory so supporting files are colocated.
    echo "  Rendering QMD to HTML"
    cd "$output_dir"
    rm -f "$base_name.html"
    quarto render "$base_name.qmd"

    echo "Converted $file -> $output_file_html"
    echo "---"
done
