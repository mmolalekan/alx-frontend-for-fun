#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:

    First argument is the name of the Markdown file
    Second argument is the output file name
'''

import sys
import os.path
import re
import hashlib

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    with open(sys.argv[1]) as read:
        with open(sys.argv[2], 'w') as html:
            unordered_start, ordered_start, paragraph = False, False, False
            # bold syntax
            for line in read:
                line = line.replace('**', '<b>', 1)
                line = line.replace('**', '</b>', 1)
                line = line.replace('__', '<em>', 1)
                line = line.replace('__', '</em>', 1)

                # md5
                md5 = re.findall(r'\[\[.+?\]\]', line)
                md5_inside = re.findall(r'\[\[(.+?)\]\]', line)
                if md5:
                    line = line.replace(md5[0], hashlib.md5(
                        md5_inside[0].encode()).hexdigest())

                # remove the letter C
                remove_letter_c = re.findall(r'\(\(.+?\)\)', line)
                remove_c_more = re.findall(r'\(\((.+?)\)\)', line)
                if remove_letter_c:
                    remove_c_more = ''.join(
                        c for c in remove_c_more[0] if c not in 'Cc')
                    line = line.replace(remove_letter_c[0], remove_c_more)

                length = len(line)
                headings = line.lstrip('#')
                heading_num = length - len(headings)
                unordered = line.lstrip('-')
                unordered_num = length - len(unordered)
                ordered = line.lstrip('*')
                ordered_num = length - len(ordered)
                # headings, lists
                if 1 <= heading_num <= 6:
                    line = '<h{}>'.format(
                        heading_num) + headings.strip() + '</h{}>\n'.format(
                        heading_num)

                if unordered_num:
                    if not unordered_start:
                        html.write('<ul>\n')
                        unordered_start = True
                    line = '<li>' + unordered.strip() + '</li>\n'
                if unordered_start and not unordered_num:
                    html.write('</ul>\n')
                    unordered_start = False

                if ordered_num:
                    if not ordered_start:
                        html.write('<ol>\n')
                        ordered_start = True
                    line = '<li>' + ordered.strip() + '</li>\n'
                if ordered_start and not ordered_num:
                    html.write('</ol>\n')
                    ordered_start = False

                if not (heading_num or unordered_start or ordered_start):
                    if not paragraph and length > 1:
                        html.write('<p>\n')
                        paragraph = True
                    elif length > 1:
                        html.write('<br/>\n')
                    elif paragraph:
                        html.write('</p>\n')
                        paragraph = False

                if length > 1:
                    html.write(line)

            if unordered_start:
                html.write('</ul>\n')
            if ordered_start:
                html.write('</ol>\n')
            if paragraph:
                html.write('</p>\n')
    exit(0)

"""
Converts Markdown to HTML.
"""

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
        print(input)
        i = 0
        for line in input:
            if line.startswith("#"):
                converted += headings(line)

            elif line.startswith("-"):
                if not input[i - 1].startswith("-"):
                    converted += "<ul>\n" + unordered_list(line)
                else:
                    converted += unordered_list(line)
                try:
                    if not input[i + 1].startswith("-"):
                        converted += "</ul>\n"
                except:
                    converted += "</ul>\n"

            elif line.startswith("*"):
                if not input[i - 1].startswith("*"):
                    converted += "<ol>\n" + unordered_list(line)
                else:
                    converted += unordered_list(line)
                try:
                    if not input[i + 1].startswith("*"):
                        converted += "</ol>\n"
                except:
                    converted += "</ol>\n"

            else:
                if input[i - 1] == input[i + 1] == "\n":
                    converted += "<p>\n\t" + line + "</p>\n"
                elif input[i - 1] == "\n" and input[i + 1] != "\n":
                    converted += "<p>\n\t" + line + "<br/>"
                    if input[i + 1] == "\n":
                        converted += line + "<p>\n"
                    else:
                        converted += line + "<br/>"
            i = i + 1

    with open(output_file, 'w') as output_file:
        output_file.write(converted)
"""
