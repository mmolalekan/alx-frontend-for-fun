#!/usr/bin/python3
"""
Converts Markdown to HTML.
"""

if __name__ == "__main__":
    import sys
    import os


    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
