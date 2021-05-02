from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mochii007@localhost:5432/pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "applepie"

connect_db(app)
db.create_all()

@app.route("/")
def home():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add", methods = ['GET', 'POST'])
def add_post():
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data, available=form.available.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("addPet.html", form=form)

@app.route("/<pet_id>", methods = ['GET', 'POST'])
def edit(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPetForm()
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("editPet.html", form=form, pet=pet)