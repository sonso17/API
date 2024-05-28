from flask import Flask, request, url_for, render_template
import register

app = Flask(__name__)
@app.route("/")
def startapp():
    return render_template('register.html')



@app.route("/api/register/", methods=['POST'])
def api():
    #JSONRebut = request.json
    correu = request.form['email']
    resultat = register.gravarRegisterDB(correu)
    return resultat+'\n'



    

