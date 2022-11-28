import requests
from bs4 import BeautifulSoup
import re
def joinlist(matrix):
    out=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            out.append(matrix[i][j])
    return out
def getchamplexical(cl):
    URL = f"https://www.rimessolides.com/motscles.aspx?m={cl}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_="l-black")
    champ_lexical=[]
    for i in range(len(results)):
        champ_lexical.append(re.findall(">(.*?)</a",str(results[i])))
    champ_lexical=joinlist(champ_lexical)
    return tuple(champ_lexical)
with open("lexique.py",'w') as f:
    f.write("champs_lexicaux = {\n")
    f.write(f"    {getchamplexical('mort')}:'mort',\n")
    f.write(f"    {getchamplexical('amour')}:'amour',\n")
    f.write(f"    {getchamplexical('laideur')}:'laideur',\n")
    f.write(f"    {getchamplexical('prostitution')}:'prostitution',\n")
    f.write(f"    {getchamplexical('beauté')}:'beauté',\n")
    f.write(f"    {getchamplexical('spleen')}:'spleen',\n")
    f.write(f"    {getchamplexical('art')}:'art',\n")
    f.write(f"    {getchamplexical('religion')}:'religion',\n")
    f.write("}")
print("writing done")