from flask import Flask, render_template, redirect, url_for
from models import db, Pet
from forms import PetForm


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)