import PyPDF2
import re
import lexique
pdfFileObj = open('fleurs-du-mal.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
finaltext=''
for i in range(0,10,1):
    pageObj = pdfReader.getPage(i)
    finaltext+=f"== Page {i-5} ==\n"+pageObj.extractText()[:-1]
pdfFileObj.close()
with open("output_notes.txt",'w') as f:
    f.write(finaltext.replace('’',"'"))