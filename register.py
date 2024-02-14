import json
import secrets
from os.path import exists
import argparse
import re

# condicio si el db.json existeix si no, el creem i li inserim un diccionari
if exists('db.json'):
    with open('db.json') as fitxer:
        registres = json.load(fitxer)
else:
    registres = {}
    registres['users'] = []
    #registres = {'users': []}
#########################################################

#carreguem els paràmetres amb el correu
#correu = sys.argv[2]
parser = argparse.ArgumentParser(usage = '%(prog)s -e <correu electrònic')
parser.add_argument('-e', metavar="<correu electrònic>", required=True)#obligo a afegir el parametre -e per poder utilitzar el programa
args = parser.parse_args()
correu = args.e
###########################################################

#comprovar correu
if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', correu):
    print("correu invàlid")
    exit(0)

#crear token
token = secrets.token_urlsafe(32)
print(token)

#Afegim el nou registre a la variable registres
registres['users'].append({
    'email': correu,
    'token': token})

#guardar tot al fitxer db.json
with open('db.json', 'w') as fitxerModificat:
    json.dump(registres, fitxerModificat, indent=4)
