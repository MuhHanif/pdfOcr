import pytesseract as ocr
import sys
from PIL import Image
from pdf2image import convert_from_path


class readPdf(object):
    """docstring for readPdf."""

    def __init__(self, pdfDir):
        #set class variable

        self.dir = pdfDir

        pass

    def toImg(self):

        poppler_path = r"C:\poppler-20.09.0\bin"

        #read pdf to img as grayscale
        pages = convert_from_path(self.dir, dpi=200, grayscale=True, poppler_path = poppler_path)

        #img counter
        count = 0

        for page in pages:

            #save img
            img = "page_" + str(count) + ".jpg"

            #save as jpg
            page.save(img, "JPEG")

            #add counter
            count = count + 1

            pass

        return(count)


class ocrRead(object):
    """docstring for ocr."""

    def __init__(self):

        pass

    def scanImg(self, outputNames, numb):

        #create output file
        output = outputNames

        #append ocr'ed text
        textAppend = open(output, "a")

        #read all image
        for image in range(numb):

            #img file name
            imgFileName = "page_" + str(image) + ".jpg"
            #open image
            img = Image.open(imgFileName)

            #ocr using pytesseract
            text = ocr.image_to_string(img)
            text = str(text)
            print(text)

            pass


        pass


int = readPdf("HPS Area Malang.pdf").toImg()
int = ocrRead().scanImg("a",2)
