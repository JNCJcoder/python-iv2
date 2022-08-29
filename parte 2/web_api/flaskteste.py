from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/json')
def hello_json():
    return {'chave': 'valor'}

@app.route('/<nome>')
def greet(nome):
    return f'<p style="color: red">Hello, {nome}</p>'

@app.route('/save', methods=['POST'])
def save():
    json = request.json
    return json