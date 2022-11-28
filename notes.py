import PyPDF2
import re
pdfFileObj = open('Les Fleurs du Mal.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(3)
print(pageObj)