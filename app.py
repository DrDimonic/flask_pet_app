from flask import Flask, render_template, redirect, url_for
from models import db, Pet
from forms import PetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SECRET_KEY'] = '8f81176d4b15a77cb8cbf472903c610436346e3af4d4b98c'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()  # Create tables in the in-memory databas

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PetForm()
    if form.validate_on_submit():
        # Mock database insertion logic
        pass
    # Mock list of pets
    pets = [
        {'name': 'Buddy', 'age': 3, 'type': 'Dog'},
        {'name': 'Whiskers', 'age': 2, 'type': 'Cat'}
    ]
    return render_template('view_pets.html', form=form, pets=pets)

if __name__ == '__main__':
    app.run(debug=True)