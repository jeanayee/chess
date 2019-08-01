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

Manually go through out/ and move the stragglers into squares/. Discard the rest.
Then manually go through squares/ and delete any non-chess-board images.

Some pngs will have multiple chess boards in them. I manually copied and cropped
these... it took me around 15 minutes.

Then I manually cropped another 60 problematic images, which took another 15
minutes. (It was actually quite soothing.) The resulting images are in
boards.zip, if you need them.

As for actually converting these images into FEN, there's plenty of libraries
available. The most popular is probably the [Reddit chess
bot](https://github.com/Elucidation/tensorflow_chessbot) which uses fancy
convolutions etc. However, their training data looks very modern and shiny,
whereas the book images are not very crisp. So the chessbot actually couldn't
handle our examples, because they're kind of out of domain.

I found [chessputzer](https://github.com/mitchellgordon95/chessputzer), which
has training examples much closer to ours. I had to put in a tiny bit of elbow
grease to get it to work, but it did.

Finally, you can convert the output of chessputzer into a json blob indexed by page number.
```
python chessputzer_to_json.py fens.txt
```
