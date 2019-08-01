# Copied from stack overflow:
# https://stackoverflow.com/a/47877930/1405370
import fitz
import os
doc = fitz.open("reassess-chess.pdf")

os.mkdir('out')

for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("out/p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("out/p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None
