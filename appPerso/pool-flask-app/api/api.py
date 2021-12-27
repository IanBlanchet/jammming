from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_data():
    return {'id':1, 'nom':'Marcel Galarneau'}
