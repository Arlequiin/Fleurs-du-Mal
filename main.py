import PyPDF2
import re
pdfFileObj = open('Les Fleurs du Mal.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
finaltext=''
noms_poemes=[]
for i in range(196,201,1):
    pageObj = pdfReader.getPage(i)
    for elem in pageObj.extractText().split("\n"):
            if elem.isupper() and len(pageObj.extractText())!=1:
              if any(char.isdigit() for char in elem.split(".")[0].split()):
               noms_poemes.append("λ")
              else:
               noms_poemes.append("•"+elem.split(".")[0])
for i in range(1,202,1):
    pageObj = pdfReader.getPage(i)
    finaltext+=f"== Page {i-5} ==\n"+pageObj.extractText()
pdfFileObj.close()
with open("output.txt",'w') as f:
    f.write(finaltext)
a=0
liste_pre_matrice=(''.join(noms_poemes).split("λ"))
matrice_poemes=[]
for i in range(len(liste_pre_matrice)):
    matrice_poemes.append(liste_pre_matrice[i].split("•"))
    del(matrice_poemes[i][0])
print(matrice_poemes)
print(re.search(r"AU LECTEUR(.*?)BÉNÉDICTION",finaltext, re.DOTALL))
with open("infos.txt",'w') as f:
    pass