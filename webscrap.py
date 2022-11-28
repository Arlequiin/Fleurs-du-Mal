import requests
from bs4 import BeautifulSoup
from main import joinlist
import re
def getchamplexical(cl):
    URL = f"https://www.rimessolides.com/motscles.aspx?m={cl}"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(class_="l-black")
    champ_lexical=[]
    for i in range(len(results)):
        champ_lexical.append(re.findall(">(.*?)</a",str(results[i])))
    champ_lexical=joinlist(champ_lexical)
    return champ_lexical
with open("champs_lexicaux.py",'w') as f:
    f.write("from webscrap import getchamplexical\n")
    f.write("champ_lexical_mort=getchamplexical('mort')\n")
    f.write("champ_lexical_amour=getchamplexical('amour')\n")
    f.write("champ_lexical_laideur=getchamplexical('laideur')\n")
    f.write("champ_lexical_prostitution=getchamplexical('prostitution')\n")
    f.write("champ_lexical_beaute=getchamplexical('beauté')\n")
    f.write("champ_lexical_spleen=getchamplexical('spleen')\n")
    f.write("champ_lexical_art=getchamplexical('art')\n")
    f.write("champ_lexical_religion=getchamplexical('religion')\n")