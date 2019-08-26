from PyPDF2 import PdfFileWriter,PdfFileReader

def cropper(start,end, file):
    inputPdf = PdfFileReader(open(file,"rb"))
    outPdf=PdfFileWriter()

    outfile = open(file.split(".")[0]+"cropped"+".pdf","wb")

    while start <= end:
        outPdf.addPage(inputPdf.getPage(start))

        outPdf.write(outfile)

        start += 1
        
    outfile. close() 


