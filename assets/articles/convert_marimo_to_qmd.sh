#!/bin/bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
search_dir="$script_dir"

find "$search_dir" -type f -name "*.py" -print0 |
while IFS= read -r -d '' file; do
    echo "Processing: $file"

    base_name="$(basename "$file" .py)"
    output_dir="$script_dir/$base_name"
    output_file_ipynb="$output_dir/$base_name.ipynb"
    output_file_qmd="$output_dir/$base_name.qmd"

    if [ -f "$output_file_qmd" ]; then
        echo "qmd file already exists: $output_file_qmd"
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


    echo "  Exporting to ipynb: $output_file_ipynb"
    # Use the exact path to the source file (do NOT prepend an extra slash)
    marimo export ipynb "$file" -o "$output_file_ipynb" --force

    echo "  Converting ipynb to qmd: $output_file_qmd"
    quarto convert "$output_file_ipynb" --output "$output_file_qmd"


    echo "Converted $file -> $output_file_qmd"
    echo "---"
done
