import sys
import re
import os
import json

lines = open(sys.argv[1], 'r').readlines()

page_to_boards = {}
for filename, fen in zip(lines[::2], lines[1::2]):
    basename = os.path.basename(filename)
    try:
        pagenum = re.match(r'p(\d*)-.*\.png', basename).group(1)
    except:
        print(f'Invalid filename: {basename}')

    page_to_boards[pagenum] = page_to_boards.get(pagenum, [])
    page_to_boards[pagenum].append(fen.strip())

with open('fens.json', 'w+') as file_:
    file_.write(json.JSONEncoder().encode(page_to_boards))
