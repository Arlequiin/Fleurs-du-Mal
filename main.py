import PyPDF2
import re
import lexique
pdfFileObj = open('Les Fleurs du Mal.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
finaltext=''
noms_poemes=[]
for i in range(196,201,1):
    pageObj = pdfReader.getPage(i)
    for elem in pageObj.extractText().split("\n"):
            if elem.isupper() and len(pageObj.extractText())!=1:
              if any(char.isdigit() for char in elem.split(".")[0].split()):
               noms_poemes.append("λ")
               #print(elem)
              else:
               noms_poemes.append("•"+elem.split(".")[0])
for i in range(1,202,1):
    pageObj = pdfReader.getPage(i)
    finaltext+=f"== Page {i-5} ==\n"+pageObj.extractText()[:-1]
pdfFileObj.close()
with open("output.txt",'w') as f:
    f.write(finaltext.replace('’',"'"))
a=0
liste_pre_matrice=(''.join(noms_poemes).split("λ"))
matrice_poemes=[]
for i in range(len(liste_pre_matrice)):
    matrice_poemes.append(liste_pre_matrice[i].replace('’',"'").split("•"))
    del(matrice_poemes[i][0])
def findpoem(poem1,n=0):
 #poem1+=' '
 try:
  poem2=joinlist(matrice_poemes)[joinlist(matrice_poemes).index(poem1)+1]
 except:
    poem2="---"
 print("Poème :",poem1,"\nPoème suivant :",poem2)
 with open("output.txt") as f:
    content=f.readlines()
 #for i in range(len(content)):
 #   if content[i][:-1]+' ' in joinlist(matrice_poemes):
 #       print(content[i])
 result=''
 i=1
 try:
  while content[content.index(poem1[:-1].replace("UNE MARTYR","UNE MARTYRE").replace("LE CRAN","LE CRANE")+"\n")+i][:-1]+' ' not in joinlist(matrice_poemes):
   if '==' not in content[content.index(poem1[:-1]+"\n")+i]:
    result+=content[content.index(poem1[:-1]+"\n")+i].replace("Les ﬂeurs du mal",'\n')
   i+=1
 except:
    i=0
    while 'Table des matières' not in content[content.index(poem1[:-1]+'\n')+i][:-1]:
         result+=content[content.index(poem1[:-1]+"\n")+i].replace("Les ﬂeurs du mal",'\n')
         i+=1
         #i+=1
 return result
def joinlist(matrix):
    out=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            out.append(matrix[i][j])
    return out

with open("README.md",'w') as f:
    f.write(f"# Au lecteur ({len(matrice_poemes[0])} poème)\n"+' - '+'\n - '.join(matrice_poemes[0])+"\n")
    f.write(f"# I Spleen et Idéal ({len(matrice_poemes[1])} poèmes)\n"+' - '+'\n - '.join(matrice_poemes[1])+"\n")
    f.write(f"# II Tableaux Parisiens ({len(matrice_poemes[2])} poèmes)\n"+' - '+'\n - '.join(matrice_poemes[2])+"\n")
    f.write(f"# III Le vin ({len(matrice_poemes[3])} poèmes)\n"+' - '+'\n - '.join(matrice_poemes[3])+"\n")
    f.write(f"# IV Fleurs du Mal ({len(matrice_poemes[4])} poèmes)\n"+' - '+'\n - '.join(matrice_poemes[4])+"\n")
    f.write(f"# V Révolte ({len(matrice_poemes[5])} poèmes)\n"+' - '+'\n - '.join(matrice_poemes[5])+"\n")
    f.write(f"# VI La Mort ({len(matrice_poemes[6])} poèmes)\n"+' - '+'\n - '.join(matrice_poemes[6])+"\n")


with open("output_notes.txt") as f:
    notes=f.readlines()
notes_poemes=[]
for element in notes:
    if any(word in element.upper() for word in joinlist(matrice_poemes)):
        if '.' in element:
         notes_poemes.append(element)
        else:
            pass
def getnotes(poeme):
    result=''
    for i in range(len(notes_poemes)):
        if notes_poemes[i].split(".")[1][1:][:-2].lower()==poeme.lower():
            for j in range(1,10):
                prov=notes[notes.index(notes_poemes[i])+j]
                if prov in notes_poemes:
                    break
                result+=notes[notes.index(notes_poemes[i])+j]
    return result
with open("table.md",'w') as f:
    f.write('''<table style="width:100%;border:1px solid black;border-radius:10px;"><tr><th>Poème</th><th>Thèmes</th><th>Notes</th></tr>''')
    for element in joinlist(matrice_poemes):
        f.write("<tr>")
        poeme=findpoem(element)
        f.write(f"<td>{element}</td>")
        f.write("<td>")
        for lists in lexique.champs_lexicaux.keys():
            if any(word.lower() in poeme for word in lists):
                f.write(f"- {lexique.champs_lexicaux[lists]}<br>")
        f.write("</td>")
        f.write(f"<td>{getnotes(element[:-1])}</td>")
        f.write("</tr>")
    f.write("</table>")
print(notes_poemes)
print(getnotes("LE MAUVAIS MOINE"))