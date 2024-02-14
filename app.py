from flask import Flask, request, url_for
import register

app = Flask(__name__)

@app.route("/api/register/", methods=['POST'])
def api():
    JSONRebut = request.json
    correu = JSONRebut['email']
    resultat = register.gravarRegisterDB(correu)
    return resultat+'\n'


    

