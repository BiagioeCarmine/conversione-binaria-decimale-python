from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def conversione():
    numero = request.args.get('n')
    if request.args.get('binodec') == "decbin":
        return tobin(numero)
    elif request.args.get('binodec') == "bindec":
        return todec(numero)
    else:
        return "Error: INVALID QUERY"

if __name__ == '__main__':
     app.run(port='5002')