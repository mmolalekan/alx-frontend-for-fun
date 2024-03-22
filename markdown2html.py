#!/usr/bin/python3
"""
Converts Markdown to HTML.
"""


def headings(line):
    count = 0
    for i in line:
        if i == "#":
            count = count + 1
    return f"<h{count}>{line[count + 1:-1]}</h{count}>\n"


if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    converted = ""
    with open(markdown_file, 'r') as input_file:
        input = input_file.readlines()
        for line in input:
            if line.startswith("#"):
                converted = converted + headings(line)

    with open(output_file, 'w') as output_file:
        output_file.write(converted)
