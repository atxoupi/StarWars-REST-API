"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User , Personajes, Planetas, Vehiculos, Favoritos
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


#GET USERs, lista todos los usuarios
@app.route('/user', methods=['GET'])
def handle_hello():

    users=User.query.all()
    ulist=list(map(lambda p: p.serialize(), users))
    print(ulist)
    response_body = {
        "results": ulist
    }

    return jsonify(response_body), 200

#[GET] /people Listar todos los registros de people en la base de datos
@app.route('/personajes', methods=['GET'])
def get_personajes():

    personajes=Personajes.query.all()
    plist=list(map(lambda p: p.serialize(), personajes))
    print(plist)
    response_body = {
        "results": plist
    }

    return jsonify(response_body), 200

#[GET] /people/<int:people_id> Listar la información de una sola people
@app.route('/personajes/<int:id>', methods=['GET'])
def get_personaje(id):

    personaje=Personajes.query.filter_by(id=id).first()
    response_body = {
        "results": personaje.serialize()
    }

    return jsonify(response_body), 200

#[GET] /planets Listar los registros de planets en la base de datos
@app.route('/planetas', methods=['GET'])
def get_planetas():

    planetas=Planetas.query.all()
    plist=list(map(lambda p: p.serialize(), planetas))
    print(plist)
    response_body = {
        "results": plist
    }

    return jsonify(response_body), 200

#[GET] /planets/<int:planet_id> Listar la información de un solo planet
@app.route('/planetas/<int:id>', methods=['GET'])
def get_planeta(id):    

    planeta=Planetas.query.filter_by(id=id).first()
    response_body = {
        "results": planeta.serialize()
    }

    return jsonify(response_body), 200

#[GET] /users/favorites Listar todos los favoritos que pertenecen al usuario actual.
@app.route('/favoritos/<int:id_user>', methods=['GET'])
def get_favoritos_user(id_user):

    favoritos=Favoritos.query.filter_by(id_user=id_user)
    plist=list(map(lambda p: p.serialize(), favoritos))
    response_body = {
        "results": plist
    }

    return jsonify(response_body), 200

#[POST] /favorite/planet/<int:planet_id> Añade un nuevo planet favorito al usuario actual con el planet id = planet_id.
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def set_favoritos_planeta(planet_id):

    body=json.loads(request.data)
    fav=Favoritos(id_user=body["id_user"], id_planeta=planet_id)
    db.session.add(fav)
    db.session.commit()

    response_body = {
        "result":fav.serialize()
    }

    return jsonify(response_body), 200

#[POST] /favorite/people/<int:people.id> Añade una nueva people favorita al usuario actual con el people.id = people_id.
@app.route('/favorite/personajes/<int:id_personaje>', methods=['POST'])
def set_favoritos_personaje(id_personaje):

    body=json.loads(request.data)
    fav=Favoritos(id_user=body["id_user"], id_personaje=id_personaje)
    db.session.add(fav)
    db.session.commit()

    response_body = {
        "result":fav.serialize()
    }

    return jsonify(response_body), 200

#[DELETE] /favorite/planet/<int:planet_id> Elimina un planet favorito con el id = planet_id`.
#aquí eliminamos un planeta favorito
@app.route('/favorite/<int:id_usuario>/planet/<int:planet_id>', methods=['DELETE'])
def del_favoritos_planeta(planet_id, id_usuario):

    planetfav=Favoritos.query.filter_by(id_user=id_usuario).filter_by(id_planeta=planet_id).first()
    print(planetfav)
    db.session.delete(planetfav)
    db.session.commit()

    response_body = {
        "result":"Planet Deleted"
    }

    return jsonify(response_body), 200

#[DELETE] /favorite/people/<int:people_id> Elimina una people favorita con el id = people_id.
@app.route('/favorite/<int:id_usuario>/personaje/<int:personaje_id>', methods=['DELETE'])
def del_favoritos_personaje(personaje_id, id_usuario):

    personajefav=Favoritos.query.filter_by(id_user=id_usuario).filter_by(id_personaje=personaje_id).first()
    db.session.delete(personajefav)
    db.session.commit()

    response_body = {
        "result":"Personaje Deleted"
    }

    return jsonify(response_body), 200


#obtenemos los vehiculos
@app.route('/vehiculos', methods=['GET'])
def get_vehiculos():

    vehiculos=Vehiculos.query.all()
    plist=list(map(lambda p: p.serialize(), vehiculos))
    print(plist)
    response_body = {
        "results": plist
    }

    return jsonify(response_body), 200

#obtenemos todos los favoritos
@app.route('/favoritos', methods=['GET'])
def get_favoritos():

    favoritos=Favoritos.query.all()
    plist=list(map(lambda p: p.serialize(), favoritos))
    print(plist)
    response_body = {
        "results": plist
    }

    return jsonify(response_body), 200

#Añadir planetas

@app.route('/planetas', methods=['POST'])
def set_planetas():

    body=json.loads(request.data)
    planet=Planetas(name=body["name"], clima=body["clima"], poblacion=body["poblacion"], rotacion=body["rotacion"])
    db.session.add(planet)
    db.session.commit()

    response_body = {
        "result": planet.serialize()
    }

    return jsonify(response_body), 200
#añadir personajes
@app.route('/personajes', methods=['POST'])
def set_personajes():

    body=json.loads(request.data)
    person=Personajes(name=body["name"], lastname=body["lastname"], id_planeta=body["id_planeta"], ojos=body["ojos"], pelo=body["pelo"], altura=body["altura"], peso=body["peso"])
    db.session.add(person)
    db.session.commit()

    response_body = {
        "results":person.serialize()
    }

    return jsonify(response_body), 200

#añadir vehículos
@app.route('/vehiculos', methods=['POST'])
def set_vehiculos():

    body=json.loads(request.data)
    veh=Vehiculos(name=body["name"], cilindrada=body["cilindrada"], capacidad=body["capacidad"])
    db.session.add(veh)
    db.session.commit()

    response_body = {
        "results": veh.serialize()
    }

    return jsonify(response_body), 200

#añadir favoritos
@app.route('/favoritos', methods=['POST'])
def set_favoritos():

    body=json.loads(request.data)
    fav=Favoritos(id_user=body["id_user"], id_personaje=body["id_personaje"], id_planeta=body["id_planeta"], id_vehiculo=body["id_vehiculo"])
    db.session.add(fav)
    db.session.commit()

    response_body = {
        "result":fav.serialize()
    }

    return jsonify(response_body), 200

#añadir usuarios

@app.route('/user', methods=['POST'])
def add_user():

    body=json.loads(request.data)
    users=User(name=body["name"], password=body["password"])
    db.session.add(users)
    db.session.commit()

    response_body = {
        "result": users.serialize()
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
