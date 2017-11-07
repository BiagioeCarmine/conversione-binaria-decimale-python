from flask import Flask, request
from flask_restful import Resource, Api
from conversione import tobin,todec
app = Flask(__name__)
api = Api(app)

def errore(errname):
    return "Errore: "+errname;

def mostravalore(err,errname,valore):
    if err:
        return errore(errname)
    return valore

@app.route('/')
def conversione():
    return "Questo non è un sito web"

if __name__ == '__main__':
     app.run(port='5002')

@app.route('/bindec/')
def bindec():
    numero = int(request.args.get('n'))
    calcolo = todec(numero,mostravalore)
    return str(calcolo)

@app.route('/decbin/')
def decbin():
    numero = int(request.args.get('n'))
    calcolo = tobin(numero,mostravalore)
    return str(calcolo)