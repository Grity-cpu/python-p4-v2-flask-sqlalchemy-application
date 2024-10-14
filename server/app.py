from flask import Flask, make_response
from models import Pet  # Ensure you import the Pet model

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response(
        '<h1>Welcome to the pet directory!</h1>',
        200
    )
    return response

@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter_by(id=id).first()  # Use filter_by for simplicity
    if pet:
        response_body = f'<p>{pet.name} {pet.species}</p>'
        response_status = 200
    else:
        response_body = f'<p>Pet {id} not found</p>'
        response_status = 404
    response = make_response(response_body, response_status)
    return response

@app.route("/species/<string:species>")
def pet_by_species(species):
    pets = Pet.query.filter_by(species=species).all()
    size = len(pets)
    response_body = f'<h1>There are {size} {species}</h1>'
    for pet in pets:
        response_body += f'<p>{pet.name}</p>'
    response_status = 200
    response = make_response(response_body, response_status)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
