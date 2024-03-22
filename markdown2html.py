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


def unordered_list(line):
    return f"\t<li>{line[2:-1]}</li>\n"

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
        i = 0
        for line in input:
            if line.startswith("#"):
                converted = converted + headings(line)

            elif line.startswith("-"):
                if not input[i - 1].startswith("-"):
                    converted = converted + "<ul>\n" + unordered_list(line)
                else:
                    converted = converted + unordered_list(line)
                try:
                    if not input[i + 1].startswith("-"):
                        converted = converted + "</ul>\n"
                except:
                    converted = converted + "</ul>\n"

            elif line.startswith("*"):
                if not input[i - 1].startswith("*"):
                    converted = converted + "<ol>\n" + unordered_list(line)
                else:
                    converted = converted + unordered_list(line)
                try:
                    if not input[i + 1].startswith("*"):
                        converted = converted + "</ol>\n"
                except:
                    converted = converted + "</ol>\n"
            i = i + 1

    with open(output_file, 'w') as output_file:
        output_file.write(converted)
