Instructions for parsing the chess board images in the PDF into FEN notation. 

I don't really expect anyone to do this again for Reassess Your Chess, since the
FENs should be published somewhere else in this repo. However, if someone wants
to do different book, these steps might be useful.


Install the requirements 
```
pip install -r requirements.txt
```

Parse all the images in the pdf into pngs (into out/)
```
python pymupdf.py
```

Move all the square-ish images into a different directory (squares/)
```
python squares.py
```

Manually go through out/ and move the stragglers into squares. Discard the rest.
Then manually go through squares/ and delete any non-chess-board images.

Some pngs will have multiple chess boards in them. I manually copied and cropped
these... it took me around 15 minutes.
