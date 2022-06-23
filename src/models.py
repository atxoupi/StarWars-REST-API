from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    #__tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(8), nullable=False)
    favorite_user = db.relationship('Favoritos', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.user

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }    

class Personajes(db.Model):
    #__tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    lastname = db.Column(db.String(250))
    id_planeta = db.Column(db.Integer, db.ForeignKey('planetas.id'), nullable=False)
    ojos = db.Column(db.String(20))
    pelo = db.Column(db.String(20))
    altura= db.Column(db.Integer)
    peso= db.Column(db.Integer)
    favoritePersonaje = db.relationship('Favoritos', backref='personajes', lazy=True)

    def __repr__(self):
        return '<Name %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "planeta": self.id_planeta,
            "ojos": self.ojos,
            "pelo": self.pelo,
            "altura": self.altura,
            "peso": self.peso,
        }    


class Planetas(db.Model):
    #__tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db .Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    clima = db.Column(db.String(250))
    poblacion = db.Column(db.Integer)
    rotacion = db.Column(db.String(20))
    planetPersonaje = db.relationship('Personajes', backref='planetas', lazy=True)
    favoritePlanet = db.relationship('Favoritos', backref='planetas', lazy=True)

    def __repr__(self):
        return '<Name %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "clima": self.clima,
            "poblacion": self.poblacion,
            "rotacion": self.rotacion,
        }

class Vehiculos(db.Model):
    #__tablename__ = 'vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    cilindrada = db.Column(db.Integer)
    capacidad = db.Column(db.Integer)
    favoriteVehiculo = db.relationship('Favoritos', backref='vehiculos', lazy=True)
    
    def __repr__(self):
        return '<Name %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cilindrada": self.cilindrada,
            "capacidad": self.capacidad,
        }

class Favoritos(db.Model):
    #__tablename__ = 'favoritos'
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    id_personaje = db.Column(db.Integer, db.ForeignKey('personajes.id'),nullable=False)
    id_planeta = db.Column(db.Integer, db.ForeignKey('planetas.id'),nullable=False)
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('vehiculos.id'),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id_user

    def serialize(self):
        return {
            "id": self.id,
            "user": self.id_user,
            "personaje": self.id_personaje,
            "planeta": self.id_planeta,
            "vehiculo": self.id_vehiculo,
        }




# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }